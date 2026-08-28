import io
import base64

SUPPORTED_LANGS = {
    "en-IN": "English",
    "te-IN": "Telugu",
    "hi-IN": "Hindi",
}

# gTTS / speech recognition language codes
_TTS_MAP = {
    "en-IN": "en",
    "te-IN": "te",
    "hi-IN": "hi",
}

_SR_MAP = {
    "en-IN": "en-IN",
    "te-IN": "te-IN",
    "hi-IN": "hi-IN",
}


def transcribe(wav_bytes, lang_code="en-IN"):
    """Convert recorded WAV audio bytes to text.

    Returns the recognized text, or an empty string on any failure
    (so the app never crashes because of voice input).
    """
    if not wav_bytes:
        return ""
    try:
        import speech_recognition as sr

        recognizer = sr.Recognizer()
        audio_file = io.BytesIO(wav_bytes)
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)

        sr_lang = _SR_MAP.get(lang_code, "en-IN")
        text = recognizer.recognize_google(audio_data, language=sr_lang)
        return (text or "").strip()
    except Exception as e:
        print("Transcribe error:", e)
        return ""


def speak_html(text, lang_code="en-IN"):
    """Convert text to speech and return an <audio> HTML snippet.

    Uses gTTS (Google Text-to-Speech), embeds the MP3 as base64 so it
    plays directly in the browser. Returns '' on any failure.
    """
    if not text:
        return ""
    try:
        from gtts import gTTS

        safe_text = str(text).replace("*", "").replace("#", "")[:900]
        if not safe_text.strip():
            return ""

        tts_lang = _TTS_MAP.get(lang_code, "en")
        tts = gTTS(text=safe_text, lang=tts_lang)

        buf = io.BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)
        b64 = base64.b64encode(buf.read()).decode()

        html = (
            '<audio controls style="width:100%;max-width:420px;height:36px;">'
            '<source src="data:audio/mp3;base64,' + b64 + '" '
            'type="audio/mp3">Your browser does not support audio.'
            "</audio>"
        )
        return html
    except Exception as e:
        print("TTS error:", e)
        return ""
