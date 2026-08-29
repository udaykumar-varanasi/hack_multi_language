"""ArogyaMitra engine - multilingual (Telugu/Hindi/English)."""

import os
import re

GEMINI_KEY = os.environ.get("GEMINI_API_KEY", "") or os.environ.get("GOOGLE_API_KEY", "")
_gem = None
if GEMINI_KEY:
    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_KEY)
        _gem = genai.GenerativeModel("gemini-1.5-flash")
    except Exception as e:
        print("Gemini init failed, offline KB used:", e)

SYSTEMPT = (
    "You are ArogyaMitra, a rural health info assistant in Andhra Pradesh, "
    "India. General non-diagnostic info only; never diagnose or prescribe. "
    "Advise the nearest PHC and 108/112 for emergencies. IMPORTANT: reply "
    "in the SAME language the user used - Telugu question = full Telugu "
    "answer, Hindi = Hindi, English = English. Keep answers short."
)

_URGENT = [
    "chest pain", "breathless", "unconscious", "seizure", "fits",
    "heavy bleeding", "poison", "snake bite", "snakebite", "scorpion",
    "suicide", "stroke", "paralysis", "not breathing", "heart attack",
    "ఛాతి నొప్పి", "స్పృహ లేదు", "మూర్ఛ", "పాము", "విషము",
    "सीने में दर्द", "सांस नहीं", "बेहोश", "दौरा", "खून", "जहर", "सांप",
]

URGENT_MSG = {
    "en": "🚨 This sounds URGENT. Call 108 / 112 NOW.",
    "te": "🚨 ఇది తీవ్రమైన పరిస్థితి కావచ్చు. వెంటనే 108 / 112 కు కాల్ చేయండి.",
    "hi": "🚨 यह गंभीर स्थिति हो सकती है। तुरंत 108 / 112 पर कॉल करें।",
}

FALLBACK = {
    "en": "I am not fully sure about that. Please visit your nearest PHC "
          "or call 104 (health hel). For emergencies call 108 / 112.",
    "te": "దీని గురించి నాకు పూర్తిగా తెలియదు. దయచేసి మీ దగ్గరి PHC ని "
          "సందర్శించండి లేదా 104 (ఆరోగ్య హెల్ప్‌లైన్) కు కాల్ చేయండి. "
          "అత్యవసర పరిస్థితులకు 108 / 112.",
    "hi": "इस बारे में मुझे पूरी जानकारी नहीं है। कृपया नज़दीकी PHC जाएँ या "
          "104 (स्वास्थ्य हेल्पलाइन) पर कॉल करें। आपात स्थिति में 108 / 112.",
}

TOPICS = {
    "headache": ["headache", "head pain", "తలనొప్పి", "सिरदर्द"],
    "fever": ["fever", "జ్వరం", "జ్వర", "बुखार"],
    "cough_cold": ["cough", "cold", "throat", "దగ్గు", "జలుబు", "గొంతు", "जुकाम", "खांसी"],
    "loose_motion": ["loose motion", "diarrhea", "విరోచనాలు", "दस्त"],
    "vomiting": ["vomit", "వాంతులు", "వాంత", "उल्टी"],
    "stomach_pain": ["stomach", "belly", "కడుపు", "पेट"],
    "dengue": ["dengue", "డెంగ్యూ", "డెంగు", "डेंगू"],
    "diabetes": ["diabetes", "sugar", "షుగర్", "మధుమేహం", "शुगर"],
    "bp": ["blood pressure", "బీపీ", "बीपी"],
    "wound": ["wound", "injury", "గాయం", "ज़ख्म", "जख्म"],
    "burn": ["burn", "కాలిన", "మంట", "जला"],
    "dog_bite": ["dog bite", "కుక్క కాటు", "कुत्ते"],
    "snake_bite": ["snake bite", "snakebite", "పాము", "सांप"],
    "acidity": ["acidity", "gas", "యాసిడిటీ", "గ్యాస్", "एसिडिटी"],
    "toothache": ["tooth", "teeth", "పళ్ల", "దంత", "दांत"],
    "ear_pain": ["ear", "చెవి", "చెవుల", "कान"],
    "eye": ["eye", "కళ్లు", "కన్ను", "కళ్ళ", "आंख"],
    "jaundice": ["jaundice", "కామెర్లు", "पीलिया"],
    "periods": ["period", "menstrual", "నెలసరి", "माहवारी"],
    "pregnancy": ["pregnan", "గర్భిణీ", "గర్భ", "गर्भ"],
    "child_health": ["child", "baby", "vaccin", "పిల్లల", "టీకా", "बच्चे"],
    "stress": ["stress", "anxiety", "depression", "ఒత్తిడి", "तनाव"],
    "allergy": ["allergy", "itching", "rash", "skin", "దద్దుర్లు", "దురద", "खुजली"],
}

OFFLINE_HINTS = {
    "headache": "Rest in a quiet dark room, drink water, wet cloth on the "
                "forehead. See a doctor if it lasts over 2-3 days.",
    "fever": "Drink fluids (ORS/water), rest. Paracetamol helps. See a "
             "doctor if fever lasts over 3 days or with rash/severe pain "
             "(could be dengue - free test at PHC).",
    "cough_cold": "Warm fluids, steam twice a day, salt-water gargling. "
                  "See a doctor if cough lasts over 2 weeks (free TB test "
                  "at PHC).",
    "loose_motion": "Most important: ORS - one packet in 1 litre clean "
                    "water, sip continuously. Light food. See a doctor if "
                    "over 6 motions a day or blood in stool.",
    "vomiting": "Sip ORS/water slowly in small sips. Avoid oily/spicy "
                "food. See a doctor if it lasts over 24 hours or has "
                "blood.",
    "snake_bite": "Keep the person calm and still, limb below heart "
                  "level. Do NOT cut or tie tightly. Go to hospital "
                  "IMMEDIATELY - call 108 now.",
    "dog_bite": "Wash the wound with soap and running water for 15 "
                "minutes NOW. Go to the PHC today for anti-rabies vaccine "
                "- do not delay.",
}


def detect_lang(text):
    if re.search(r"[\u0C00-\u0C7F]", text):
        return "te"
    if re.search(r"[\u0900-\u097F]", text):
        return "hi"
    return "en"


def is_urgent(text):
    t = text.lower()
    return any(w in t for w in _URGENT)


def emergency_block(text):
    """Return (urgent_bool, advice_text)."""
    urgent = is_urgent(text)
    if urgent:
        return True, (URGENT_MSG["en"] + "\n\nGo to the nearest hospital "
                      "immediately. Do not wait.")
    return False, ("No emergency signs detected. For helplines see the "
                   "Emergency page. Ambulance: 108 | National: 112 | "
                   "Health: 104.")


def _match_topic(text):
    t = text.lower()
    for topic, words in TOPICS.items():
        if any(w in t for w in words):
            return topic
    return None


def _offline_answer(text):
    lang = detect_lang(text)
    topic = _match_topic(text)
    if topic:
        hint_en = OFFLINE_HINTS.get(topic, "")
        if hint_en:
            if lang == "te":
                return ("ఇది సాధారణ సమాచారం మాత్రమే. " + hint_en +
                        " ఖచ్చితమైన నిర్ధారణ కోసం దగ్గరి PHC ని సందర్శించండి. "
                        "అత్యవసరంగా 108 / 112 కు కాల్ చేయండి.")
            if lang == "hi":
                return ("यह केवल सामान्य जानकारी है। " + hint_en +
                        " सही जाँच के लिए नज़दीकी PHC जाएँ। आपात स्थिति में "
                        "108 / 112 पर कॉल करें।")
            return ("General information only: " + hint_en +
                    " For proper diagnosis visit your nearest PHC. "
                    "Emergencies: 108 / 112.")
    return FALLBACK[lang]


def stream_response(history, query):
    """Yield response chunks for the chat page."""
    lang = detect_lang(query)
    urgent = is_urgent(query)

    reply = None
    if _gem is not None:
        try:
            msgs = []
            for m in history[-6:]:
                role = "user" if m["role"] == "user" else "model"
                msgs.append({"role": role, "parts": [m["text"]]})
            msgs.append({"role": "user",
                         "parts": [query + "\n\n(Reply fully in " +
                                   {"te": "Telugu", "hi": "Hindi",
                                        "en": "English"}[lang] + ")"]})
            resp = _gem.generate_content(msgs, safety_settings=None)
            reply = (resp.text or "").strip() or None
        except Exception as e:
            print("Gemini error:", e)
            reply = None

    if reply is None:
        reply = _offline_answer(query)

    if urgent:
        reply = URGENT_MSG[lang] + "\n\n" + reply

    stream_response.last_urgent = urgent
    stream_response.last_full_text = reply

    # yield in small chunks to simulate streaming
    step = 4
    for i in range(0, len(reply), step):
        yield reply[i:i + step]
