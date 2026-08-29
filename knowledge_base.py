"""ArogyaMitra knowledge base - basic needs + diseases (EN/TE/HI)."""

DISCLAIMER = (
    "⚕️ ArogyaMitra gives general health information only. It does NOT "
    "diagnose or replace a doctor. For any health concern visit your "
    "nearest PHC. Emergency: 108 / 112."
)

EMERGENCY_CONTACTS = {
    "Ambulance": "108",
    "National Emergency": "112",
    "Health Helpline": "104",
}

TOPICS = {
    # basic needs
    "clean_water": ["water", "నీరు", "తాగు", "पानी"],
    "hygiene": ["hygiene", "wash hands", "soap", "పరిశుభ్రత", "చేతులు",
                "सफ़ाई", "हाथ धो"],
    "nutrition": ["nutrition", "diet", "food", "పోషణ", "ఆహారం",
                  "पोषण", "आहार", "खाना"],
    "sleep_rest": ["sleep", "rest", "నిద్ర", "విశ్రాంతి", "नींद", "आराम"],
    "first_aid": ["first aid", "kit", "bandage", "ప్రాథమిక", "పట్టీ",
                  "प्राथमिक", "पट्टी"],
    "sanitation": ["toilet", "garbage", "శౌచం", "చెత్త", "शौच", "कचरा"],
    # diseases
    "fever": ["fever", "జ్వరం", "జ్వర", "बुखार"],
    "cold_cough": ["cough", "cold", "throat", "దగ్గు", "జలుబు",
                   "గొంతు", "खांसी", "जुकाम"],
    "headache": ["headache", "head pain", "తలనొప్పి", "सिरदर्द",
                 "सिर दर्द"],
    "stomach_pain": ["stomach", "belly", "abdominal", "కడుపు", "पेट"],
    "chest_pain": ["chest pain", "heart pain", "heart attack", "ఛాతి",
                   "గుండె", "सीने में दर्द", "सीना", "हार्ट", "छाती"],
    "fracture": ["fracture", "broken bone", "bone", "ఎముక", "విరుపు",
                 "ఒత్తు", "हड्डी", "टूट"],
    "bleeding": ["bleeding", "blood", "రక్తస్రావం", "రక్తం", "కట్",
                 "खून", "रक्त"],
}

KB = {
    "clean_water": {
        "en": "**Safe water:** Boil 10 min or use chlorine tablets; "
              "store covered. Unsafe water causes diarrhea, typhoid, "
              "jaundice.",
        "te": "**తాగునీరు:** 10 నిమిషాలు మరిగించండి లేదా క్లోరిన్ టాబ్లెట్లు "
              "వాడండి; మూసిన పాత్రలో నిల్వ. శుభ్రం కాని నీరు విరోచనాలు, "
              "టైఫాయిడ్, కామెర్లకు కారణం.",
        "hi": "**पीने का पानी:** 10 मिनट उबालें या क्लोरीन टैबलेट डालें; "
              "ढककर रखें। दूषित पानी से दस्त, टाइफाइड, पीलिया होता है।",
    },
    "hygiene": {
        "en": "**Hygiene:** Wash hands with soap before eating, after "
              "toilet and animals. Bathe daily, trim nails. Prevents "
              "stomach and skin infections.",
        "te": "**పరిశుభ్రత:** తినే ముందు, శౌచం తర్వాత, జంతువులను తాకిన తర్వాత "
              "సబ్బుతో చేతులు కడగండి. రోజూ స్నానం, గోరు చిన్నగా. కడుపు, చర్మ "
              "వ్యాధులు తగ్గుతాయి.",
        "hi": "**सफ़ाई:** खाने से पहले, शौच के बाद, जानवर छूने के बाद "
              "साबुन से हाथ धोएँ। रोज़ नहाएँ, नाख़ून काटें। पेट और त्वचा "
              "रोग रुकते हैं।",
    },
    "nutrition": {
        "en": "**Nutrition:** Rice/roti + dal + vegetables + curd. "
              "Pregnant women and children need iron (greens, jaggery) "
              "and protein (eggs, dal). Free food at Anganwadi.",
        "te": "**పోషణ:** బియ్యం/రొట్టె + పప్పు + కూరగాయలు + పెరుగు. గర్భిణీ "
              "స్త్రీలు, పిల్లలకు ఇనుము (ఆకుకూరలు, బెల్లం), ప్రోటీన్ (గుడ్లు, "
              "పప్పు) కావాలి. ఆంగన్‌వాడీలో ఉచిత ఆహారం.",
        "hi": "**पोषण:** चावल/रोटी + दाल + सब्ज़ियाँ + दही। गर्भवती "
              "महिलाओं और बच्चों को आयरन (हरी सब्ज़ी, गुड़) और प्रोटीन "
              "(अंडे, दाल) चाहिए। आंगनवाड़ी में मुफ़्त भोजन।",
    },
    "sleep_rest": {
        "en": "**Sleep & rest:** 7-8 hours daily. Lack of sleep causes "
              "headache, BP and stress.",
        "te": "**నిద్ర, విశ్రాంతి:** రోజుకు 7-8 గంటలు. నిద్ర లేమి వల్ల తలనొప్పి, "
              "బీపీ, ఒత్తిడి వస్తాయి.",
        "hi": "**नींद और आराम:** रोज़ 7-8 घंटे। कम नींद से सिरदर्द, बीपी, "
              "तनाव होता है।",
    },
    "first_aid": {
        "en": "**First-aid kit:** Keep bandage, cotton, antiseptic, ORS "
              "packets, paracetamol. Cuts: wash and press with clean "
              "cloth. Burns: cool water 10 min - never toothpaste/ghee.",
        "te": "**కిట్:** పట్టీలు, పత్తి, ఆంటిసెప్టిక్, ORS, పారాసిటమాల్ ఉంచండి. "
              "కట్లకు: కడిగి శుభ్ర గుడ్డతో నొక్కండి. కాలినవి: 10 నిమిషాలు చల్ల "
              "నీరు - టూత్‌పేస్ట్/నెయ్యి వద్దు.",
        "hi": "**किट:** पट्टी, रुई, एंटीसेप्टिक, ORS, पैरासिटामोल रखें। "
              "कटने पर: धोकर साफ़ कपड़े से दबाएँ। जलने पर 10 मिनट ठंडा "
              "पानी - टूथपेस्ट/घी नहीं।",
    },
    "sanitation": {
        "en": "**Sanitation:** Use the toilet, never open fields near "
              "water. Dispose garbage away from home. Prevents "
              "diarrhea, cholera, worms.",
        "te": "**పారిశుధ్యం:** శౌచాలయం వాడండి, నీటి దగ్గర బహిరంగంగా చేయవద్దు. "
              "చెత్త దూరంగా పారవేయండి. విరోచనాలు, కలరా, పురుగులు తగ్గుతాయి.",
        "hi": "**स्वच्छता:** शौचालय का उपयोग करें, पानी के पास खुले में "
              "न जाएँ। कचरा दूर फेंकें। दस्त, हैजा, कीड़े रुकते हैं।",
    },
    "fever": {
        "en": "**Fever:** Rest, drink fluids, paracetamol

> ⚠️ The response reached the length limit. Reply **continue** to get the rest.
