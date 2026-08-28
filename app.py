import hashlib

import streamlit as st
from datetime import datetime, date
from engine import stream_response
from locator import search_facilities
from knowledge_base import EMERGENCY_CONTACTS, DISCLAIMER
from voice import transcribe, speak_html, SUPPORTED_LANGS

import pandas as pd

# ===================== PAGE SETUP =====================
st.set_page_config(
    page_title="ArogyaMitra - Rural Health Assistant",
    page_icon="⚕️",
    layout="centered",
    initial_sidebar_state="expanded",
)

CURSOR = " ▌"

URGENT_BANNER_HTML = (
    '<div style="background:#b00020;color:#fff;padding:12px 16px;'
    'border-radius:10px;font-weight:bold;margin-bottom:8px;">'
    '🚨 This sounds URGENT. Call 108 / 112 NOW, then follow the first-aid '
    'steps below while help arrives.</div>'
)

AUDIO_EXPANDER_HTML = (
    '<details style="margin-top:4px;"><summary style="cursor:pointer;'
    'font-size:0.85em;">🔊 Listen to this answer</summary>'
    '<div>{audio}</div></details>'
)

# ===================== SIDEBAR =====================
with st.sidebar:
    st.title("⚕️ ArogyaMitra")
    st.caption("Rural Health Assistant - AP")
    page = st.radio(
 "Go to",
        ["💬 Health Info Chat", "📍 Find Facilities", "ℹ️ About"],
        label_visibility="collapsed",
    )
    st.divider()

    st.subheader("🌐 Voice language")
    voice_lang = st.selectbox(
        "For speech input / output",
        list(SUPPORTED_LANGS.keys()),
        format_func=lambda k: SUPPORTED_LANGS[k],
        label_visibility="collapsed",
    )

    st.divider()
    st.subheader("🚨 Emergency numbers")
    for label, num in EMERGENCY_CONTACTS.items():
        st.markdown(f"**{label}:** `{num}`")

    st.divider()
    st.caption(
        "Non-diagnostic, non-prescribing platform. "
        "Not a substitute for a doctor."
    )

st.session_state.setdefault("chat_history", [])
st.session_state.setdefault("voice_lang", voice_lang)
st.session_state["voice_lang"] = voice_lang

st.info(DISCLAIMER, icon="ℹ️")

# ===================== PAGE 1: CHAT =====================
if page == "💬 Health Info Chat":
    st.title("Health Information Assistant")
    st.caption(
        "Type below, or press the record button and just speak — "
        "Telugu, Hindi and English supported."
    )

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            if msg.get("urgent") and msg["role"] == "assistant":
                st.markdown(URGENT_BANNER_HTML, unsafe_allow_html=True)
            st.markdown(msg["text"])
            audio = msg.get("audio")
            if audio:
                with st.expander("🔊 Listen"):
                    st.markdown(audio, unsafe_allow_html=True)

    # ---- voice input ----
    wav_bytes = None
    recorder_available = True
    try:
        from audio_recorder_streamlit import audio_recorder
        wav_bytes = audio_recorder(
            text="🎙️ Speak (click to record)",
            recording_color="#e74c3c",
            neutral_color="#6c757d",
            icon_size="2x",
            key="voice_recorder",
            return_bytes="wav",
        )
    except Exception:
        try:
            from streamlit_audiorecorder import st_audiorecorder
            wav_bytes = st_audiorecorder("🎙️ Speak", key="voice_recorder2")
        except Exception:
            recorder_available = False

    if not recorder_available:
        st.caption("🎙️ Voice input unavailable - please type your question.")

    spoken_text = ""
    if wav_bytes:
        audio_sig = hashlib.md5(wav_bytes).hexdigest()
        if audio_sig != st.session_state.get("last_audio_sig"):
            st.session_state["last_audio_sig"] = audio_sig
            with st.spinner("Understanding your speech..."):
                spoken_text = transcribe(wav_bytes, st.session_state["voice_lang"])
            if spoken_text:
                st.toast("Heard you!", icon="✅")

    # ---- text input ----
    typed_text = st.chat_input("Type your health question here...")

    user_query = spoken_text or typed_text or ""

    needs_reply = False
    if user_query:
        st.session_state.chat_history.append(
            {"role": "user", "text": user_query}
        )
        with st.chat_message("user"):
            st.markdown(user_query)
        needs_reply = True

    if needs_reply:
        latest = st.session_state.chat_history[-1]["text"]
        history_so_far = st.session_state.chat_history[:-1]

        with st.chat_message("assistant"):
            urgent_banner = st.empty()
            placeholder = st.empty()
            audio_slot = st.empty()

            result = stream_response(history_so_far, latest)
            reply_text = result.get("text", "")
            urgent = result.get("urgent", False)

            # simple typewriter effect
            shown = ""
            for i in range(0, len(reply_text), 6):
                shown = reply_text[: i + 6]
                placeholder.markdown(shown + CURSOR)
            placeholder.markdown(reply_text)

            if urgent:
                urgent_banner.markdown(URGENT_BANNER_HTML, unsafe_allow_html=True)

            audio_html = speak_html(reply_text, st.session_state["voice_lang"])
            if audio_html:
                audio_slot.markdown(
                    AUDIO_EXPANDER_HTML.format(audio=audio_html),
                    unsafe_allow_html=True,
                )

        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "text": reply_text,
                "urgent": urgent,
                "audio": audio_html,
            }
        )
        st.rerun()

# ===================== PAGE 2: FACILITY LOCATOR =====================
elif page == "📍 Find Facilities":
    st.title("Find Health Facilities Near You")
    st.caption("Demo database covering the Tekkali area,rikakulam district.")

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
            st.warning(
                "No facilities found for that filter. Try the "
                "distance or choosing 'Any'."
            )
        else:
            rows = []
            for f in results:
                rows.append(
                    {
                        "Facility": f["name"],
                        "Type": f["type"],
                        "Distance (km)": round(f["_km"], 1),
                        "Services": f["services"],
                        "Phone": f["phone"],
                    }
                )
            st.data(pd.DataFrame(rows), use_container_width=True)

            st.markdown("##### Map")
            map_df = pd.DataFrame(
                {
                    "lat": [f["lat"] for f in results] + [lat],
                    "lon": [f["lon"] for f in results] + [lon],
                }
            )
            st.map(map_df)

    st.divider()
    st.markdown("##### ☎️ Quick emergency dialing")
    for label, num in EMERGENCY_CONTACTS.items():
        st.markdown(f"- **{label}:** {num}")

# ===================== PAGE 3: ABOUT =====================
else:
    st.title("About ArogyaMitra")
    st.markdown(
        """
**ArogyaMitra** is a multilingual (Telugu / Hindi / English) rural health
accessibility assistant built for the Google GenAI Exchange Hackathon.

**What it does**
- 💬 Answers everyday health questions with safe, general information
  (powered by Gemini, with an offline knowledge base as fallback).
- 🎙️ Accepts **voice input** and reads answers **aloud** — designed for
  low-literacy users.
- 📍 Helps locate nearby PHCs / hospitals and shows emergency numbers.
- 🚨 Detects urgent symptoms and immediately surfaces 108 / 112 guidance.

**What it does NOT do**
- Does **not** diagnose diseases.
- Does **not** prescribe prescription medicines.
- Always recommends confirming with a doctor, PHC, ASHA worker or
  pharmacist.

**Privacy:** conversations are session-only; voice is processed only to
transcribe your question.
        """
    )

    st.divider()
    st.caption(f"Last deployed check: {datetime.now().strftime('%d %b %Y')}")
