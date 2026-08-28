
## 📄 File 2: `engine.py` (complete replacement — Gemini first, KB fallback)

```python
"""
ArogyaMitra answer engine.
Gemini handles natural conversation (in any language) with the OTC-aware
system prompt; the local knowledge base is the offline fallback.
"""

import os
import json
from knowledge_base import (
    KB_ENTRIES, FALLBACK_ANSWER, URGENT_KEYWORDS, SYSTEM_PROMPT, search_kb,
)

# ---------- Gemini setup (lazy) ----------
_client = None
_gemini_ready = False


def _get_gemini():
    global _client, _gemini_ready
    if _gemini_ready:
        return _client
    try:
        from google import genai
        api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            _gemini_ready = False
            return None
        _client = genai.Client(api_key=api_key)
        _gemini_ready = True
    except Exception:
        _gemini_ready = False
    return _client


class stream_response:
    """Callable generator; exposes .last_full_text and .last_urgent."""
    last_full_text = ""
    last_urgent = False

    def __init__(self):
        pass

    def __call__(self, history, query):
        stream_response.last_urgent = _is_urgent(query)
        reply = ""

        model_reply = _ask_gemini(history, query)
        if model_reply:
            reply = model_reply
        else:
            score, entry = search_kb(query)
            if score >= 2:
                reply = entry["answer"]
            else:
                reply = FALLBACK_ANSWER

        # Stream the reply in small chunks for the typing effect
        for i in range(0, len(reply), 4):
            yield reply[i:i + 4]

        stream_response.last_full_text = reply


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
            config={"system_instruction": SYSTEM_PROMPT,
                    "temperature": 0.4,
                    "max_output_tokens": 400},
        )
        text = (resp.text or "").strip() if hasattr(resp, "text") else ""
        return text or None
    except Exception as e:
        print("Gemini error:", e)
        return None
