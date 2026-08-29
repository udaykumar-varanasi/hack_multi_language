import io
import base64
import subprocess
import tempfile
import os

SUPPORTED_LANGS = {
    "en-IN": "English",
    "te-IN": "Telugu",
    "hi-IN": "Hindi",
}

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


def _convert_to_wav(raw_bytes, fmt=""):
    """Convert any audio (webm/ogg/mp3) to WAV bytes. None on failure."""
    if raw_bytes[:4] == b"RIFF":
        return raw_bytes

    # Path A: pydub + ffmpeg
    try:
        from pydub import AudioSegment
        try:
            seg = AudioSegment.from_file(io.BytesIO(raw_bytes))
        except Exception:
            seg = AudioSegment.from_file(io.BytesIO(raw_bytes), codec="opus")
        buf = io.BytesIO()
        seg.export(buf, format="wav")
        buf.seek(0)
        print("Convert: pydub OK, source format:", fmt)
        return buf.read()
    except Exception as e:
        print("Convert: pydub failed:", e)

    # Path B: direct ffmpeg subprocess via temp files
    try:
        fmt_low = (fmt or "").lower()
        if "webm" in fmt_low:
            in_ext = "webm"
        elif "ogg" in fmt_low:
            in_ext = "ogg"
        elif "mp4" in fmt_low or "m4a" in fmt_low:
            in_ext = "m4a"
        else:
            in_ext = "webm"
        tmp_in = tempfile.NamedTemporaryFile(suffix="." + in_ext, delete=False)
        tmp_out = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        tmp_in.write(raw_bytes)
        tmp_in.close()
        tmp_out.close()
        subprocess.run(
            ["ffmpeg", "-y", "-i", tmp_in.name, "-ar", "16000",
             "-ac", "1", tmp_out.name],
            check=True, capture_output=True,
        )
        with open(tmp_out.name, "rb") as f:
            wav = f.read()
        os.unlink(tmp_in.name)
        os.unlink(tmp_out.name)
        print("Convert: ffmpeg subprocess OK")
        return wav
    except Exception as e:
        print("Convert: ffmpeg subprocess failed:", e)

    return None


def transcribe_any(raw_bytes, fmt=""):
    """Handle any audio format: convert to wav, then transcribe.
    Returns '' on failure."""
    if not raw_bytes:
        return ""
    print("Mic audio received:", len(raw_bytes), "bytes, format:", fmt)
    wav = _convert_to_wav(raw_bytes, fmt)
    if wav is None:
        print("Convert: ALL methods failed - is ffmpeg installed?")
        return ""
    return transcribe(wav)


def transcribe(wav_bytes, lang_code="en-IN"):
    """Convert WAV audio bytes to text. Returns '' on any failure."""
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
    """Convert text to speech, return an <audio> HTML snippet. '' on failure."""
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
