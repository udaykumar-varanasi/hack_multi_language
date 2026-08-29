import hashlib

import streamlit as st
from datetime import datetime, date, time as dtime
from engine import stream_response, emergency_block
from locator import search_facilities
from knowledge_base import EMERGENCY_CONTACTS, DISCLAIMER
from voice import transcribe, transcribe_any, speak_html, SUPPORTED_LANGS

import pandas as pd

st.set_page_config(
    page_title="ArogyaMitra - Rural Health Assistant",
    page_icon="⚕️",
    layout="centered",
    initial_sidebar_state="expanded",
)

URGENT_BANNER_HTML = (
    '<div style="background:#b00020;color:#ffffff;padding:14px 18px;'
    'border-radius:10px;font-weight:bold;font-size:18px;margin-bottom:8px;">'
    '🚨 This sounds URGENT. Call 108 / 112 NOW.</div>'
)

# ---------------- session state defaults ----------------
st.session_state.setdefault("chat_history", [])
st.session_state.setdefault("appointments", [])
st.session_state.setdefault("reminders", [])
st.session_state.setdefault("records", [])
st.session_state.setdefault("escalations", [])

# ---------------- sidebar ----------------
with st.sidebar:
    st.title("⚕️ ArogyaMitra")
    st.caption("Rural Health Assistant - AP")
    page = st.radio(
        "Go to",
        [
            "💬 Health Chat",
            "📅 Appointments",
            "⏰ Reminders",
            "📁 Health Records",
            "📍 Find Facilities",
            "🚨 Emergency",
            "ℹ️ About",
        ],
        label_visibility="collapsed",
    )
    st.divider()
    st.subheader("🌐 Voice language")
    voice_lang = st.selectbox(
        "For speech input and output",
        list(SUPPORTED_LANGS.keys()),
        format_func=lambda k: SUPPORTED_LANGS[k],
        label_visibility="collapsed",
    )
    st.divider()
    st.subheader("🚨 Emergency numbers")
    for label, num in EMERGENCY_CONTACTS.items():
        st.markdown("**" + label + ":** `" + num + "`")
    st.divider()
    st.caption("Non-diagnostic platform. Not a substitute for a doctor.")

st.session_state["voice_lang"] = voice_lang

# ---------------- mic component ----------------
mic_recorder = None
try:
    from streamlit_mic_recorder import mic_recorder
except Exception as e:
    print("streamlit_mic_recorder import failed:", e)


def voice_input_box():
    """Render mic button; return recognized text (empty if none)."""
    if mic_recorder is None:
        st.caption("Voice input unavailable - please type.")
        return ""
    col_mic, col_hint = st.columns([1, 4])
    with col_mic:
        result = mic_recorder(
            start_prompt="🎤",
            stop_prompt="⏹️",
            just_once=True,
            use_container_width=True,
            key="mic_btn",
        )
    with col_hint:
        st.caption("Tap 🎤, allow microphone, speak, tap ⏹️.")
    if result and result.get("bytes"):
        raw = result["bytes"]
        sig = hashlib.md5(raw).hexdigest()
        if sig != st.session_state.get("last_audio_sig"):
            st.session_state["last_audio_sig"] = sig
            with st.spinner("Understanding your speech..."):
                text = transcribe_any(raw, result.get("format", ""))
            if text:
                st.toast("Heard you!", icon="✅")
                return text
            st.warning("Could not understand. Try again or type.")
    return ""


def esc_row(when, question, reason):
    st.session_state.escalations.append({
        "when": when,
        "question": question,
        "reason": reason,
    })


# ============================================================
# PAGE 1: HEALTH CHAT
# ============================================================
if page == "💬 Health Chat":
    st.title("Health Information Assistant")
    st.caption("Multilingual chat with voice - Telugu, Hindi, English.")
    st.info(DISCLAIMER, icon="ℹ️")

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            if msg.get("urgent") and msg["role"] == "assistant":
                st.markdown(URGENT_BANNER_HTML, unsafe_allow_html=True)
            st.markdown(msg["text"])
            audio = msg.get("audio")
            if audio:
                with st.expander("🔊 Listen"):
                    st.markdown(audio, unsafe_allow_html=True)

    spoken = voice_input_box()
    typed = st.chat_input("Type your health question here...")
    user_query = spoken or typed or ""

    if user_query:
        st.session_state.chat_history.append(
            {"role": "user", "text": user_query}
        )
        with st.chat_message("user"):
            st.markdown(user_query)

        latest = st.session_state.chat_history[-1]["text"]
        history_so_far = st.session_state.chat_history[:-1]

        with st.chat_message("assistant"):
            urgent_banner = st.empty()
            placeholder = st.empty()
            audio_slot = st.empty()
            shown = ""
            for chunk in stream_response(history_so_far, latest):
                shown += chunk
                placeholder.markdown(shown + " |")
            placeholder.markdown(shown)
            urgent = bool(getattr(stream_response, "last_urgent", False))
            full_text = getattr(stream_response, "last_full_text", "") or shown
            if urgent:
                urgent_banner.markdown(
                    URGENT_BANNER_HTML, unsafe_allow_html=True
                )
                esc_row(
                    datetime.now().strftime("%d %b %Y %H:%M"),
                    latest,
                    "Urgent symptoms detected - advised 108/112",
                )
            audio_html = speak_html(full_text, voice_lang)
            if audio_html:
                audio_slot.markdown(audio_html, unsafe_allow_html=True)

        st.session_state.chat_history.append(
            {"role": "assistant", "text": full_text,
             "urgent": urgent, "audio": audio_html}
        )
        st.rerun()

# ============================================================
# PAGE 2: APPOINTMENTS
# ============================================================
elif page == "📅 Appointments":
    st.title("📅 Appointment / Request Management")
    st.caption("Request a visit at a facility. PHC staff or ASHA workers "
               "can confirm it. All data stays in this session.")

    with st.form("appt_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            pname = st.text_input("Patient name *")
            facility = st.selectbox(
                "Facility",
                ["Tekkali PHC", "Srikakulam Area Hospital",
                 "CHC Santabommali", "Nearest PHC (auto-locate)"],
            )
            need_type = st.selectbox(
                "Purpose",
                ["General checkup", "Fever", "BP / Sugar check",
                 "Pregnancy checkup (ANC)", "Child vaccination",
                 "Lab test", "Wound / injury", "Other"],
            )
        with c2:
            adate = st.date_input("Preferred date", min_value=date.today())
            atime = st.time_input("Preferred time", value=dtime(10, 0))
            phone = st.text_input("Contact number (optional)")
        notes = st.text_area("Notes for the doctor (symptoms, etc.)")
        submit = st.form_submit_button("📩 Submit request", type="primary")

    if submit:
        if not pname.strip():
            st.error("Please enter the patient name.")
        else:
            st.session_state.appointments.append({
                "name": pname.strip(),
                "facility": facility,
                "purpose": need_type,
                "date": adate.strftime("%d %b %Y"),
                "time": atime.strftime("%I:%M %p"),
                "phone": phone,
                "notes": notes,
                "status": "Requested",
                "created": datetime.now().strftime("%d %b %Y %H:%M"),
            })
            st.success("✅ Request saved! An ASHA worker / PHC will "
                       "confirm. You can view it below.")

    st.divider()
    st.markdown("### 📋 My appointment requests")
    appts = st.session_state.appointments
    if not appts:
        st.info("No appointment requests yet.")
    else:
        for idx in range(len(appts) - 1, -1, -1):
            a = appts[idx]
            title = ("🎫 " + a["name"] + " - " + a["purpose"]
                     + " - " + a["date"] + " (" + a["status"] + ")")
            with st.expander(title):
                lines = (
                    "**Facility:** " + a["facility"] + "  \n"
                    "**When:** " + a["date"] + " at " + a["time"] + "  \n"
                    "**Contact:** " + (a["phone"] or "-") + "  \n"
                    "**Notes:** " + (a["notes"] or "-")
                )
                st.markdown(lines)
                c1, c2 = st.columns(2)
                if c1.button("✔️ Mark Confirmed", key="conf" + str(idx)):
                    st.session_state.appointments[idx]["status"] = "Confirmed"
                    st.rerun()
                if c2.button("❌ Cancel", key="canc" + str(idx)):
                    st.session_state.appointments[idx]["status"] = "Cancelled"
                    st.rerun()

# ============================================================
# PAGE 3: REMINDERS
# ============================================================
elif page == "⏰ Reminders":
    st.title("⏰ Medicine and Appointment Reminders")
    st.caption("Set reminders for medicines, checkups and vaccination "
               "doses. Reminders show while the app is open.")

    tab1, tab2 = st.tabs(["💊 Medicine reminder", "📅 Visit reminder"])

    with tab1:
        with st.form("med_form", clear_on_submit=True):
            mname = st.text_input("Medicine name *")
            mdose = st.text_input("Dose (e.g. 1 tablet)", value="1 tablet")
            mfreq = st.selectbox(
                "How often?",
                ["Once a day", "Twice a day", "Three times a day",
                 "Weekly"],
            )
            mtimes = st.text_input("Time(s) (24h, comma separated)",
                                   value="08:00, 20:00")
            mdays = st.number_input("For how many days?", 1, 365, 7)
            m_start = st.date_input("Starting from", key="msd",
                                    min_value=date.today())
            if st.form_submit_button("➕ Add medicine reminder"):
                if mname.strip():
                    st.session_state.reminders.append({
                        "type": "💊 Medicine",
                        "name": mname.strip(),
                        "detail": mdose + " - " + mfreq,
                        "times": mtimes,
                        "days": int(mdays),
                        "start": m_start.strftime("%d %b %Y"),
                        "done": False,
                    })
                    st.success("✅ Reminder added!")
                else:
                    st.error("Enter the medicine name.")

    with tab2:
        with st.form("visit_form", clear_on_submit=True):
            vname = st.selectbox(
                "Visit type",
                ["PHC checkup", "Pregnancy (ANC) checkup",
                 "Child vaccination", "Lab test", "Follow-up visit"],
            )
            vdate = st.date_input("Visit date", key="vdt",
                                  min_value=date.today())
            vtime = st.time_input("Visit time", value=dtime(10, 0))
            if st.form_submit_button("➕ Add visit reminder"):
                st.session_state.reminders.append({
                    "type": "📅 Visit",
                    "name": vname,
                    "detail": (vdate.strftime("%d %b %Y") + " at "
                               + vtime.strftime("%I:%M %p")),
                    "times": vtime.strftime("%H:%M"),
                    "days": 1,
                    "start": vdate.strftime("%d %b %Y"),
                    "done": False,
                })
                st.success("✅ Visit reminder added!")

    st.divider()
    st.markdown("### 🔔 Active reminders")
    rems = st.session_state.reminders
    if not rems:
        st.info("No reminders yet.")
    else:
        for i in range(len(rems)):
            r = rems[i]
            if r["done"]:
                continue
            c1, c2 = st.columns([5, 1])
            with c1:
                lines = (r["type"] + " **" + r["name"] + "**  \n"
                         "🕒 " + r["times"] + " | 📆 from " + r["start"]
                         + " | " + r["detail"]
                         + " (" + str(r["days"]) + " day(s))")
                st.markdown(lines)
            with c2:
                if st.button("✔️", key="rdone" + str(i),
                             help="Mark taken or done"):
                    st.session_state.reminders[i]["done"] = True
                    st.rerun()
        done_count = len([r for r in rems if r["done"]])
        if done_count:
            st.caption("✅ " + str(done_count) + " reminder(s) completed.")

# ============================================================
# PAGE 4: HEALTH RECORDS
# ============================================================
elif page == "📁 Health Records":
    st.title("📁 Patient Health Record Organization")
    st.caption("Keep visits, readings and prescriptions organised in one "
               "place. Session-only: data closes when the app closes.")

    with st.form("rec_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            rname = st.text_input("Patient name *")
            rtype = st.selectbox(
                "Record type",
                ["🩺 Visit note", "💊 Medicine given",
                 "🧪 Lab result", "🌡️ Reading (BP/sugar/weight)",
                 "💉 Vaccination"],
            )
        with c2:
            rdate = st.date_input("Date", key="rdate",
                                  max_value=date.today())
            rdoctor = st.text_input("Doctor / PHC (optional)")
        rvalue = st.text_area(
            "Details * (e.g. BP 140/90; sugar 180; fever 2 days)"
        )
        if st.form_submit_button("💾 Save record"):
            if rname.strip() and rvalue.strip():
                st.session_state.records.append({
                    "name": rname.strip(),
                    "type": rtype,
                    "date": rdate.strftime("%d %b %Y"),
                    "doctor": rdoctor or "-",
                    "details": rvalue.strip(),
                })
                st.success("✅ Record saved!")
            else:
                st.error("Patient name and details are required.")

    st.divider()
    st.markdown("### 🗂️ All records")
    recs = st.session_state.records
    if not recs:
        st.info("No records yet.")
    else:
        filter_name = st.text_input("🔎 Filter by patient name")
        rows = [
            {
                "Patient": r["name"],
                "Type": r["type"],
                "Date": r["date"],
                "Doctor/PHC": r["doctor"],
                "Details": r["details"],
            }
            for r in recs
            if filter_name.lower() in r["name"].lower()
        ]
        if rows:
            st.dataframe(pd.DataFrame(rows), use_container_width=True)
        else:
            st.warning("No records match that name.")

        st.markdown("### ⬇️ Download all records (CSV)")
        all_rows = [
            {
                "Patient": r["name"], "Type": r["type"],
                "Date": r["date"], "Doctor/PHC": r["doctor"],
                "Details": r["details"],
            }
            for r in recs
        ]
        st.download_button(
            "📥 Download CSV",
            data=pd.DataFrame(all_rows).to_csv(index=False)
            .encode("utf-8"),
            file_name="health_records.csv",
            mime="text/csv",
        )

# ============================================================
# PAGE 5: FACILITY LOCATOR
# ============================================================
elif page == "📍 Find Facilities":
    st.title("Find Health Facilities Near You")
    st.caption("Demo database covering the Tekkali area, Srikakulam "
               "district.")

    col1, col2 = st.columns(2)
    with col1:
        need = st.selectbox(
            "What do you need?",
            ["Any", "emergency", "maternity", "pediatric", "lab",
             "vaccination", "specialist", "surgery", "general"],
        )
    with col2:
        max_km = st.slider("Within distance (km)", 1, 100, 30)

    st.markdown("#### Your location")
    lat = st.number_input("Latitude", value=18.6063, format="%.4f")
    lon = st.number_input("Longitude", value=84.2460, format="%.4f")

    if st.button("🔎 Search", type="primary"):
        results = search_facilities(lat, lon, need=need, max_km=max_km)
        if not results:
            st.warning("No facilities found. Try widening the distance "
                       "or choosing 'Any'.")
        else:
            rows = [{
                "Facility": f["name"],
                "Type": f["type"],
                "Distance (km)": round(f["distance_km"], 1),
                "Services": f["services"],
                "Phone": f["phone"],
            } for f in results]
            st.dataframe(pd.DataFrame(rows), use_container_width=True)
            st.markdown("##### Map")
            map_df = pd.DataFrame({
                "lat": [f["lat"] for f in results] + [lat],
                "lon": [f["lon"] for f in results] + [lon],
            })
            st.map(map_df)

            st.markdown("##### 📅 Request an appointment at one of these")
            with st.form("loc_appt", clear_on_submit=True):
                fc = st.selectbox("Facility",
                                  [f["name"] for f in results])
                la1, la2 = st.columns(2)
                with la1:
                    lp = st.text_input("Patient name *")
                with la2:
                    ld = st.date_input("Preferred date",
                                       min_value=date.today(),
                                       key="ldappt")
                if st.form_submit_button("📩 Submit request"):
                    if lp.strip():
                        st.session_state.appointments.append({
                            "name": lp.strip(),
                            "facility": fc,
                            "purpose": need,
                            "date": ld.strftime("%d %b %Y"),
                            "time": "10:00 AM",
                            "phone": "",
                            "notes": "Requested from locator",
                            "status": "Requested",
                            "created": datetime.now().strftime(
                                "%d %b %Y %H:%M"),
                        })
                        st.success("✅ Request saved! See the "
                                   "Appointments page.")
                    else:
                        st.error("Enter the patient name.")

# ============================================================
# PAGE 6: EMERGENCY  (high-contrast redesign)
# ============================================================
elif page == "🚨 Emergency":
    st.title("🚨 Emergency Help")

    st.markdown(
        '<div style="background:#7a0013;color:#ffffff;padding:16px 20px;'
        'border-radius:12px;font-size:20px;font-weight:bold;'
        'text-align:center;">'
        '🚨 In a life-threatening situation, call immediately</div>',
        unsafe_allow_html=True,
    )
    st.write("")

    # Big white number cards - readable in BOTH light and dark theme
    ICONS = {
        "Ambulance": "🚑",
        "National Emergency": "🆘",
        "Health Helpline": "📞",
    }
    for label, num in EMERGENCY_CONTACTS.items():
        icon = ICONS.get(label, "📞")
        card = (
            '<div style="background:#b00020;color:#ffffff;'
            'border-radius:12px;padding:18px 22px;margin:10px 0;'
            'box-shadow:0 2px 8px rgba(0,0,0,0.4);">'
            '<span style="font-size:26px;font-weight:800;'
            'letter-spacing:0.5px;">'
            + icon + " " + label + " &nbsp;→&nbsp; " + num
            + "</span></div>"
        )
        st.markdown(card, unsafe_allow_html=True)

    st.write("")
    st.markdown("##### Tap to call from a mobile phone")
    bcols = st.columns(len(EMERGENCY_CONTACTS))
    for col, (label, num) in zip(bcols, EMERGENCY_CONTACTS.items()):
        with col:
            st.markdown(
                '<a href="tel:' + num + '"><button style="'
                'background:#ffffff;color:#b00020;border:2px solid #b00020;'
                'border-radius:10px;padding:10px 18px;font-size:18px;'
                'font-weight:bold;cursor:pointer;">📞 ' + num
                + "</button></a>",
                unsafe_allow_html=True,
            )

    st.divider()
    st.markdown("### 🗣️ Tell us what happened (voice or text)")
    spoken = voice_input_box()
    manual = st.text_area("Or type the situation")
    situation = spoken or manual

    if st.button("🚑 Analyze and log emergency", type="primary"):
        if situation.strip():
            urgent, advice = emergency_block(situation)
            if urgent:
                st.markdown(URGENT_BANNER_HTML, unsafe_allow_html=True)
            st.markdown(advice)
            esc_row(
                datetime.now().strftime("%d %b %Y %H:%M"),
                situation.strip(),
                "Emergency page - "
                + ("URGENT flags matched" if urgent
                   else "non-urgent guidance given"),
            )
            audio_html = speak_html(advice, voice_lang)
            if audio_html:
                st.markdown(audio_html, unsafe_allow_html=True)
        else:
            st.warning("Speak or type what happened first.")

    st.divider()
    st.markdown("### 📈 Escalation log")
    st.caption("Cases where the app escalated to professional care - "
               "useful for ASHA workers reviewing follow-ups.")
    if not st.session_state.escalations:
        st.info("No escalations logged this session.")
    else:
        st.dataframe(pd.DataFrame(st.session_state.escalations),
                     use_container_width=True)

# ============================================================
# PAGE 7: ABOUT
# ============================================================
else:
    st.title("About ArogyaMitra")
    st.markdown(
        "**ArogyaMitra** is a multilingual (Telugu / Hindi / English) "
        "non-diagnostic rural health assistance platform.\n\n"
        "**Features**\n"
        "- 💬 Multilingual conversational interface (text + voice).\n"
        "- 🩺 Basic health-information guidance with an offline "
        "knowledge base and Gemini-powered answers.\n"
        "- 📍 Nearby hospital / health-center locator with map.\n"
        "- 📅 Appointment / request management.\n"
        "- ⏰ Medicine and appointment reminders.\n"
        "- 🚨 Emergency contact functionality with escalation log.\n"
        "- 📁 Patient health-record organization (with CSV download).\n"
        "- 🎙️ Voice-based interaction for users with limited literacy.\n"
        "- 📈 Automatic escalation when urgent symptoms are detected.\n\n"
        "**What it does NOT do**\n"
        "- Does not diagnose diseases or replace doctors.\n"
        "- Does not prescribe prescription medicines.\n\n"
        "**Privacy:** all data stays in this browser session only."
    )
    st.divider()
    st.caption("Deployed: " + datetime.now().strftime("%d %b %Y"))
