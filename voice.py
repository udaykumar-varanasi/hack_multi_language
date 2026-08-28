"""Voice layer for Rural Health Assistant.
STT: SpeechRecognition (free Google endpoint, multilingual — your engine.py
     already handles Telugu/Hindi via langdetect + Gemini translation).
TTS: gTTS — speaks the reply back in the user's language."""

from __future__ import annotations

import base64
import io
import tempfile

SUPPORTED_LANGS = {
    "English": "en-IN",
    "తెలుగు (Telugu)": "te-IN",
    "हिन्दी (Hindi)": "hi-IN",
}


# ---------------- Speech → Text ----------------
def transcribe(audio_bytes: bytes, lang_code: str = "en-IN") -> str | None:
    """Convert recorded mic audio to text. Returns None on any failure
    (app stays fully usable by typing — graceful degradation)."""
    if not audio_bytes:
        return None
    try:
        import speech_recognition as sr

        wav_bytes = _ensure_wav(audio_bytes)

        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            f.write(wav_bytes)
            path = f.name

        r = sr.Recognizer()
        with sr.AudioFile(path) as source:
            r.adjust_for_ambient_noise(source, duration=0.3)
            audio_data = r.record(source)
        return r.recognize_google(audio_data, language=lang_code)
    except Exception:
        return None


def _ensure_wav(audio_bytes: bytes) -> bytes:
    """Browser mic gives wav via audiorecorder; convert anything else via pydub."""
    if audio_bytes[:4] == b"RIFF":          # already WAV
        return audio_bytes
    try:
        from pydub import AudioSegment
        seg = AudioSegment.from_file(io.BytesIO(audio_bytes))
        buf = io.BytesIO()
        seg.export(buf, format="wav")
        return buf.getvalue()
    except Exception:
        return audio_bytes


# ---------------- Text → Speech ----------------
def speak_html(text: str, lang_code: str = "en-IN") -> str:
    """Returns an <audio controls autoplay> HTML block for the reply."""
    try:
        from gtts import gTTS
        tts_lang = "te" if lang_code.startswith("te") else (
                   "hi" if lang_code.startswith("hi") else "en")
        clean = (text or "").replace("*", "").replace("#", "").replace("`", "")
        clean = clean[:1800]  # keep TTS fast
        if not clean.strip():
            return ""
        buf = io.BytesIO()
        gTTS(text=clean, lang=tts_lang).write_to_fp(buf)
        b64 = base64.b64encode(buf.getvalue()).decode()
        return (f'<audio autoplay controls style="width:100%" '
                f'src="data:audio/mp3;base64,{b64}"></audio>')
    except Exception:
        return ""
