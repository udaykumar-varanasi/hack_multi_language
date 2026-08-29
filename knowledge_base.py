"""ArogyaMitra knowledge base - basic needs (EN/TE/HI)."""

DISCLAIMER = (
    "⚕️ Arogyaitra gives general health information only. It does NOT "
    "diagnose or replace a doctor. For any health concern visit your "
    "nearest PHC. Emergency: 108 / 112."
)

EMERGENCY_CONTACTS = {
    "Ambulance": "108",
    "National Emergency": "112",
    "Health Helpline": "104",
}

TOPICS = {
    "clean_water": ["water", "నీరు", "తాగు", "पानी"],
    "hygiene": ["hygiene", "wash hands", "soap", "పరిశుభ్రత", "చేతులు",
                "सफ़ाई", "हाथ धो"],
    "nutrition": ["nutrition", "diet", "food", "పోషణ", "ఆహారం",
                  "पोषण", "आहार", "खाना"],
    "sleep_rest": ["sleep", "rest", "నిద్ర", "విశ్రాంతి", "नींद", "आराम"],
    "first_aid": ["first aid", "kit", "bandage", "ప్రాథమిక", "పట్టీ",
                  "प्राथमिक", "पट्टी"],
    "sanitation": ["toilet", "latrine", "garbage", "శౌచం", "చెత్త",
                   "शौच", "कचरा"],
}

KB = {
    "clean_water": {
        "en": "**Safe drinking water:** Boil water 10 minutes or use "
              "chlorine tablets. Store in a closed clean container. "
              "Unsafe water causes diarrhea, typhoid, jaundice.",
        "te": "**తాగునీరు:** నీటిని 10 నిమిషాలు మరిగించండి లేదా క్లోరిన్ "
              "టాబ్లెట్లు వాడండి. మూసిన శుభ్ర పాత్రలో నిల్వ చేయండి. "
              "శుభ్రం కాని నీరు విరోచనాలు, టైఫాయిడ్, కామెర్లకు కారణం.",
        "hi": "**पीने का पानी:** पानी 10 मिनट उबालें या क्लोरीन टैबलेट "
              "डालें। ढके साफ़ बर्तन में रखें। दूषित पानी से दस्त, "
              "टाइफाइड, पीलिया होता है।",
    },
    "hygiene": {
        "en": "**Hygiene:** Wash hands with soap before eating, after "
              "toilet and after touching animals. Bathe daily, keep "
              "nails short. Prevents most stomach and skin infections.",
        "te": "**పరిశుభ్రత:** తినే ముందు, శౌచం తర్వాత, జంతువులను తాకిన "
              "తర్వాత సబ్బుతో చేతులు కడగండి. రోజూ స్నానం, గోరు చిన్నగా. "
              "ఇది చాలా కడుపు, చర్మ వ్యాధులను నివారిస్తుంది.",
        "hi": "**सफ़ाई:** खाने से पहले, शौच के बाद, जानवर छूने के बाद "
              "साबुन से हाथ धोएँ। रोज़ नहाएँ, नाख़ून छोटे रखें। इससे "
              "ज़्यादातर पेट और त्वचा रोग रुकते हैं।",
    },
    "nutrition": {
        "en": "**Nutrition:** Eat rice/roti + dal + vegetables + curd. "
              "Pregnant women and children need extra iron (greens, "
              "jaggery) and protein (eggs, dal). Free nutritious food "
              "at Anganwadi.",
        "te": "**పోషణ:** బియ్యం/రొట్టె + పప్పు + కూరగాయలు + పెరుగు "
              "తినండి. గర్భిణీ స్త్రీలు, పిల్లలకు ఎక్కువ ఇనుము "
              "(ఆకుకూరలు, బెల్లం), ప్రోటీన్ (గుడ్లు, పప్పు) కావాలి. "
              "ఆంగన్‌వాడీలో ఉచిత పోషకాహారం.",
        "hi": "**पोषण:** चावल/रोटी + दाल + सब्ज़ियाँ + दही खाएँ। गर्भवती "
              "महिलाओं और बच्चों को आयरन (हरी सब्ज़ी, गुड़) और प्रोटीन "
              "(अंडे, दाल) चाहिए। आंगनवाड़ी में मुफ़्त पौष्टिक भोजन।",
    },
    "sleep_rest": {
        "en": "**Sleep & rest:** 7-8 hours of sleep daily. Lack of "
              "sleep causes headache, high BP and stress.",
        "te": "**నిద్ర, విశ్రాంతి:** రోజుకు 7-8 గంటలు నిద్ర. నిద్ర లేమి "
              "వల్ల తలనొప్పి, బీపీ, ఒత్తిడి వస్తాయి.",
        "hi": "**नींद और आराम:** रोज़ 7-8 घंटे सोएँ। नींद की कमी से "
              "सिरदर्द, बीपी, तनाव होता है।",
    },
    "first_aid": {
        "en": "**First-aid kit:** Keep bandage, cotton, antiseptic, ORS "
              "packets and paracetamol at home. Cuts: wash, press with "
              "clean cloth. Burns: cool water 10 min - never apply "
              "toothpaste or ghee.",
        "te": "**ప్రాథమిక చికిత్స కిట్:** ఇంట్లో పట్టీలు, పత్తి, "
              "ఆంటిసెప్టిక్, ORS సంచులు, పారాసిటమాల్ ఉంచండి. కట్లకు: "
              "కడగండి, శుభ్ర గుడ్డతో నొక్కండి. కాలిన గాయాలకు: 10 నిమిషాలు "
              "చల్ల నీరు - టూత్‌పేస్ట్/నెయ్యి వేయవద్దు.",
        "hi": "**प्राथमिक चिकित्सा किट:** घर पर पट्टी, रुई, एंटीसेप्टिक, "
              "ORS, पैरासिटामोल रखें। कटने पर: धोएँ, साफ़ कपड़े से "
              "दबाएँ। जलने पर: 10 मिनट ठंडा पानी - टूथपेस्ट/घी न लगाएँ।",
    },
    "sanitation": {
        "en": "**Sanitation:** Use the toilet, never open fields near "
              "water sources. Dispose garbage away from the house. "
              "Prevents diarrhea, cholera and worms.",
        "te": "**పారిశుధ్యం:** శౌచాలయం వాడండి, నీటి వనరుల దగ్గర బహిరంగ "
              "ప్రదేశాలలో చేయవద్దు. చెత్తను ఇంటి నుండి దూరంగా పారవేయండి. "
              "ఇది విరోచనాలు, కలరా, పురుగులను నివారిస్తుంది.",
        "hi": "**स्वच्छता:** शौचालय का उपयोग करें, पानी के स्रोत के पास "
              "खुले में न जाएँ। कचरा घर से दूर फेंकें। इससे दस्त, हैजा, "
              "कीड़े रुकते हैं।",
    },
}


def detect_lang(text):
    """Return 'te', 'hi' or 'en' based on script."""
    import re
    if re.search(r"[\u0C00-\u0C7F]", text):
        return "te"
    if re.search(r"[\u0900-\u097F]", text):
        return "hi"
    return "en"


def get_answer(query, lang=None):
    """Match a query to a basic-needs topic; return answer string or None."""
    q = query.lower()
    lang = lang or detect_lang(query)
    for topic, words in TOPICS.items():
        if any(w in q for w in words):
            return KB[topic].get(lang) or KB[topic]["en"]
    return None
