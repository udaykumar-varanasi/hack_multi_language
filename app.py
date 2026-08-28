"""
Rural Health Assistant — HackSprint 2.0
Non-diagnostic healthcare accessibility platform with voice support.
"""

import io
import hashlib
import streamlit as st
from datetime import datetime, date
from engine import stream_response
from locator import search_facilities
from knowledge_base import EMERGENCY_CONTACTS, DISCLAIMER
from voice import transcribe, speak_html, SUPPORTED_LANGS

st.set_page_config(page_title="Rural Health Assistant", page_icon="⚕️", layout="wide")

st.markdown("""
<style>
    .block-container { padding-top: 1.5rem; max-width: 900px; }
    [data-testid="stChatMessage"] { padding: 0.25rem 0; }
    .urgent-banner {
        background: #fee2e2; border: 1px solid #fca5a5; color: #7f1d1d;
        padding: 0.9rem 1.1rem; border-radius: 10px; margin-bottom: 0.6rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

URGENT_BANNER_HTML = (
    "<div class='urgent-banner'>🚨 This may be urgent — call 108 (Ambulance) "
    "or 112 (Emergency) now, or go to the nearest hospital.</div>"
)

# ---------- session state ----------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "reminders" not in st.session_state:
    st.session_state.reminders = []
if "records" not in st.session_state:
    st.session_state.records = []

# ---------- sidebar ----------
with st.sidebar:
    st.markdown("## ⚕️ Rural Health Assistant")
    st.caption("Non-diagnostic healthcare accessibility platform")

    st.markdown("### 🚨 Emergency Contacts")
    for name, number in EMERGENCY_CONTACTS.items():
        st.markdown(f"**{name}:** `{number}`")

    st.divider()
    page = st.radio(
        "Navigate",
        ["💬 Health Info Chat", "🏥 Find Healthcare", "⏰ Reminders", "📋 My Health Notes"],
        label_visibility="collapsed",
    )

    if page == "💬 Health Info Chat" and st.session_state.chat_history:
        st.divider()
        if st.button("🗑️ New chat", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

    st.divider()
    st.caption("Built for HackSprint 2.0 — Dept. of CSE, AITAM")

st.info(DISCLAIMER, icon="⚕️")

# ================= PAGE 1: CHAT (with voice) =================
if page == "💬 Health Info Chat":
    st.title("Health Information Assistant")
    st.caption("Type below, or 🎙️ press record and just speak — Telugu, Hindi or English.")

    # Voice language selector (controls both listening and spoken reply)
    v1, _v2 = st.columns([1, 2])
    voice_lang_name = v1.selectbox("🗣️ Voice language", list(SUPPORTED_LANGS.keys()))
    voice_lang = SUPPORTED_LANGS[voice_lang_name]
    st.session_state["voice_lang"] = voice_lang

    # ---- Welcome + quick topics (first visit only) ----
    if not st.session_state.chat_history:
        st.success(
            "👋 **Welcome!** I'm here to give you general health information. "
            "Type a question, press 🎙️ to speak, or tap a topic."
        )
        st.caption("Quick topics")
        suggestions = ["Fever", "Cough and cold", "Loose motions", "Headache",
                       "Feeling stressed", "Child health", "Pregnancy care", "Snake bite"]
        cols = st.columns(4)
        clicked = None
        for i, s in enumerate(suggestions):
            with cols[i % 4]:
                if st.button(s, use_container_width=True, key=f"sugg_{i}"):
                    clicked = s
        if clicked:
            st.session_state.chat_history.append({"role": "user", "text": clicked})
            st.rerun()

    # ---- Render chat history (with spoken-reply audio) ----
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            with st.chat_message("user", avatar="🧑"):
                st.markdown(msg["text"])
        else:
            with st.chat_message("assistant", avatar="⚕️"):
                if msg.get("urgent"):
                    st.markdown(URGENT_BANNER_HTML, unsafe_allow_html=True)
                st.markdown(msg["text"])
                if msg.get("audio"):
                    st.markdown(msg["audio"], unsafe_allow_html=True)

    # ---- Generate reply for latest user message ----
    needs_reply = (
        st.session_state.chat_history
        and st.session_state.chat_history[-1]["role"] == "user"
    )
    if needs_reply:
        latest = st.session_state.chat_history[-1]["text"]
        history_so_far = st.session_state.chat_history[:-1]
        with st.chat_message("assistant", avatar="⚕️"):
            placeholder = st.empty()
            urgent_placeholder = st.empty()
            audio_slot = st.empty()
            full_text = ""
            urgent_shown = False
            for chunk in stream_response(history_so_far, latest):
                if stream_response.last_urgent and not urgent_shown:
                    urgent_placeholder.markdown(URGENT_BANNER_HTML, unsafe_allow_html=True)
                    urgent_shown = True
                full_text += chunk
                placeholder.markdown(full_text + "▌")
            placeholder.markdown(full_text)
            audio_html = speak_html(full_text, st.session_state.get("voice_lang", "en-IN"))
            if audio_html:
                audio_slot.markdown(audio_html, unsafe_allow_html=True)
        st.session_state.chat_history.append({
            "role": "assistant",
            "text": stream_response.last_full_text or full_text,
            "urgent": stream_response.last_urgent,
            "audio": audio_html,
        })
        st.rerun()

    # ---- 🎙️ VOICE INPUT: record → transcribe → confirm → send ----
    try:
        from streamlit_audiorecorder import audiorecorder
        has_recorder = True
    except ImportError:
        has_recorder = False
        st.warning("🎙️ Voice needs `streamlit-audiorecorder` in requirements.txt — "
                   "add it and redeploy to enable the mic.")

    if has_recorder:
        st.markdown("##### 🎙️ Or speak your question")
        audio = audiorecorder("🎙️ Tap to record", "⏹️ Tap to stop", key="mic")

        if audio is not None and len(audio) > 0:
            buf = io.BytesIO()
            try:
                audio.export(buf, format="wav")
                wav_data = buf.getvalue()
            except Exception:
                wav_data = bytes(audio)

            sig = hashlib.md5(wav_data).hexdigest()
            if st.session_state.get("last_rec_sig") != sig:
                st.session_state.last_rec_sig = sig
                with st.spinner("Understanding your speech…"):
                    heard = transcribe(wav_data, st.session_state.get("voice_lang", "en-IN"))
                if heard and heard.strip():
                    st.session_state.heard_text = heard.strip()
                else:
                    st.session_state.pop("heard_text", None)
                    st.warning("Sorry, I couldn't understand that. "
                               "Try again closer to the mic, or type below.")
                st.rerun()

        # Confirm what was heard (protects against accents/misrecognition)
        if st.session_state.get("heard_text"):
            st.success(f"🗣️ I heard: **{st.session_state['heard_text']}**")
            c1, c2 = st.columns(2)
            if c1.button("✅ Send this", type="primary", use_container_width=True):
                q = st.session_state.pop("heard_text")
                st.session_state.chat_history.append({"role": "user", "text": q})
                st.rerun()
            if c2.button("❌ Discard", use_container_width=True):
                st.session_state.pop("heard_text", None)
                st.rerun()

    # ---- Typed input (always visible) ----
    with st.form("chat_form", clear_on_submit=True):
        query = st.text_input(
            "Your question",
            placeholder="e.g. I have fever since 2 days…",
            label_visibility="collapsed",
        )
        submitted = st.form_submit_button("Send ➤", type="primary", use_container_width=True)
    if submitted and query and query.strip():
        st.session_state.chat_history.append({"role": "user", "text": query.strip()})
        st.rerun()

# ================= PAGE 2: LOCATOR =================
elif page == "🏥 Find Healthcare":
    st.title("Find Nearby Healthcare")
    st.caption("Demo dataset near Tekkali, AP. Distances are approximate "
               "unless you share your location below.")

    use_loc = st.checkbox("📍 Use my location for accurate distances")
    user_coords = None
    if use_loc:
        lc1, lc2 = st.columns(2)
        lat = lc1.number_input("Latitude", value=18.62, format="%.4f")
        lon = lc2.number_input("Longitude", value=84.05, format="%.4f")
        user_coords = (lat, lon)

    search_q = st.text_input("Search by need (e.g. 'emergency', 'maternity', 'pediatric')", "")
    results = search_facilities(search_q, user_coords=user_coords)

    for f in results:
        with st.container(border=True):
            c1, c2 = st.columns([3, 1])
            with c1:
                st.markdown(f"### {f['name']}")
                st.markdown(f"**Type:** {f['type']}  |  **Services:** {f['services']}")
                st.markdown(f"📞 {f['phone']}")
            with c2:
                st.metric("Distance", f"{f['distance_km']} km")

# ================= PAGE 3: REMINDERS =================
elif page == "⏰ Reminders":
    st.title("Medicine & Appointment Reminders")

    with st.form("add_reminder", clear_on_submit=True):
        c1, c2, c3 = st.columns([3, 2, 2])
        with c1:
            r_title = st.text_input("What (medicine / appointment)")
        with c2:
            r_date = st.date_input("Date", min_value=date.today())
        with c3:
            r_time = st.time_input("Time")
        submitted = st.form_submit_button("Add Reminder", type="primary")
        if submitted and r_title.strip():
            st.session_state.reminders.append({
                "title": r_title, "date": str(r_date), "time": str(r_time),
                "added": datetime.now().strftime("%Y-%m-%d %H:%M"),
            })
            st.success(f"Reminder added: {r_title} on {r_date} at {r_time}")

    st.divider()
    if not st.session_state.reminders:
        st.caption("No reminders yet.")
    else:
        sorted_reminders = sorted(st.session_state.reminders,
                                  key=lambda r: (r["date"], r["time"]))
        for i, r in enumerate(sorted_reminders):
            c1, c2 = st.columns([5, 1])
            with c1:
                st.markdown(f"**{r['title']}** — {r['date']} at {r['time']}")
            with c2:
                if st.button("✕", key=f"del_{i}"):
                    st.session_state.reminders.remove(r)
                    st.rerun()

# ================= PAGE 4: HEALTH NOTES =================
elif page == "📋 My Health Notes":
    st.title("My Health Notes")
    st.caption(
        "A private, local space to jot down symptoms, visit summaries, or "
        "questions to ask your doctor. Not a medical record; not shared."
    )

    with st.form("add_note", clear_on_submit=True):
        note = st.text_area("New note")
        submitted = st.form_submit_button("Save Note", type="primary")
        if submitted and note.strip():
            st.session_state.records.append({
                "text": note, "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            })
            st.success("Note saved.")

    st.divider()
    if not st.session_state.records:
        st.caption("No notes yet.")
    else:
        for rec in reversed(st.session_state.records):
            with st.container(border=True):
                st.caption(rec["date"])
                st.write(rec["text"])
