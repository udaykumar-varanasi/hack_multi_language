import os

from knowledge_base import (
    KB_ENTRIES, FALLBACK_ANSWER, URGENT_KEYWORDS, SYSTEM_PROMPT,
    EMERGENCY_CONTACTS, search_kb,
)

_client = None
_gemini_ready = False


def _get_gemini():
    global _client, _gemini_ready
    if _gemini_ready:
        return _client
    try:
        from google import genai
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            return None
        _client = genai.Client(api_key=api_key)
        _gemini_ready = True
    except Exception as e:
        print("Gemini init error:", e)
        _gemini_ready = False
    return _client


def _is_urgent(text):
    t = (text or "").lower()
    return any(k in t for k in URGENT_KEYWORDS)


def _ask_gemini(history, query):
    client = _get_gemini()
    if client is None:
        return None
    try:
        contents = []
        for msg in history[-8:]:
            role = "user" if msg["role"] == "user" else "model"
            contents.append({"role": role, "parts": [{"text": msg["text"]}]})
        contents.append({"role": "user", "parts": [{"text": query}]})
        resp = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=contents,
            config={
                "system_instruction": SYSTEM_PROMPT,
                "temperature": 0.4,
                "max_output_tokens": 400,
            },
        )
        text = ""
        if hasattr(resp, "text"):
            text = (resp.text or "").strip()
        if text:
            return text
        return None
    except Exception as e:
        print("Gemini error:", e)
        return None


def _build_reply(history, query):
    """Get the full reply text (Gemini first, offline KB fallback)."""
    reply = _ask_gemini(history, query)
    if not reply:
        score, entry = search_kb(query)
        if score >= 2 and entry is not None:
            reply = entry["answer"]
        else:
            reply = FALLBACK_ANSWER
    return reply


def stream_response(history, query):
    """Generator that yields reply chunks. After it finishes,
    .last_urgent and .last_full_text hold the final values."""
    stream_response.last_urgent = _is_urgent(query)
    full_text = _build_reply(history, query)
    stream_response.last_full_text = full_text
    step = 24
    for i in range(0, len(full_text), step):
        yield full_text[i:i + step]


stream_response.last_urgent = False
stream_response.last_full_text = ""


def emergency_block():
    """Return a formatted string of emergency numbers."""
    lines = ["Emergency numbers:"]
    for label, num in EMERGENCY_CONTACTS.items():
        lines.append("- " + label + ": " + num)
    return "\n".join(lines)
