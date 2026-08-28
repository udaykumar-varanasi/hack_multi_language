import io

SUPPORTED_LANGS = {
    "en-IN": "English",
    "te-IN": "తెలుగు (Telugu)",
    "hi-IN": "हिन्दी (Hindi)",
}

_LANG_MAP = {
    "en-IN": "en-US",
    "te-IN": "te-IN",
    "hi-IN": "hi-IN",
}


def transcribe(wav_bytes, lang_code="en-IN"):
    """Convert recorded WAV audio bytes to text. Returns '' on failure."""
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        audio_file = io.BytesIO(wav_bytes)
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
        sr_lang = _LANG_MAP.get(lang_code, "-US")
        text = recognizer.recognize_google(audio_data, language=sr_lang)
        return text.strip()
    except Exception as e:
        print("Transcribe error:", e)
        return ""


def speak_html(text, lang_code="en-IN"):
    """Return an <audio> HTML snippet that speaks the text, or ''."""
    try:
        from gtts import gTTS
        import base64
        safe_text = (text or "")[:900]
        sr_lang = _LANG_MAP.get(lang_code, "en-US")
        tts = gTTS(text=safe_text, lang=sr_lang)
        buf = io.BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)
        b64 = base64.b64encode(buf.read()).decode()
        html = (
            '<audio controls style="width:100%;height:36px;">'
            '<source src="data:audio/mp3;base64,' + b64 + '" '
            'type="audio/mp3"></audio>'
        )
        return html
    except Exception as e:
        print("TTS error:", e)
        return ""
