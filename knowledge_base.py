"""ArogyaMitra knowledge base - EN/TE/HI."""

DISCLAIMER = (
    "⚕️ ArogyaMitra gives general health information only. It does NOT "
    "replace a doctor. Visit your nearest PHC. Emergency: 108 / 112."
)

EMERGENCY_CONTACTS = {
    "Ambulance": "108",
    "National Emergency": "112",
    "Health Helpline": "104",
}

TOPICS = {
    "clean_water": ["water", "నీరు", "पानी"],
    "hygiene": ["hygiene", "wash hands", "soap", "పరిశుభ్రత", "सफ़ाई"],
    "nutrition": ["nutrition", "food", "diet", "పోషణ", "ఆహారం", "पोषण", "खाना"],
    "first_aid": ["first aid", "kit", "ప్రాథమిక", "प्राथमिक"],
    "fever": ["fever", "జ్వరం", "बुखार"],
    "cold_cough": ["cough", "cold", "దగ్గు", "జలుబు", "खांसी", "जुकाम"],
    "headache": ["headache", "తలనొప్పి", "सिरदर्द"],
    "stomach_pain": ["stomach", "కడుపు", "पेट"],
    "chest_pain": ["chest pain", "heart", "ఛాతి", "గుండె", "हार्ट"],
    "fracture": ["fracture", "bone", "ఎముక", "हड्डी"],
    "bleeding": ["bleeding", "blood", "రక్తం", "రక్తస్రావం", "खून"],
    "diarrhea": ["loose motion", "diarrhea", "విరోచనాలు", "दस्त"],
}

KB = {
    "clean_water": {
        "en": "Boil water 10 min or use chlorine tablets; store covered. Unsafe water causes diarrhea, typhoid, jaundice.",
        "te": "నీటిని 10 నిమిషాలు మరిగించండి లేదా క్లోరిన్ టాబ్లెట్లు వాడండి; మూసిన పాత్రలో నిల్వ చేయండి.",
        "hi": "पानी 10 मिनट उबालें या क्लोरीन टैबलेट डालें; ढककर रखें।",
    },
    "hygiene": {
        "en": "Wash hands with soap before eating and after toilet. Bathe daily, trim nails. Prevents infections.",
        "te": "తినే ముందు, శౌచం తర్వాత సబ్బుతో చేతులు కడగండి. రోజూ స్నానం చేయండి.",
        "hi": "खाने से पहले, शौच के बाद साबुन से हाथ धोएँ। रोज़ नहाएँ।",
    },
    "nutrition": {
        "en": "Eat rice/roti + dal + vegetables + curd. Pregnant women and children need extra iron and protein. Free food at Anganwadi.",
        "te": "బియ్యం + పప్పు + కూరగాయలు + పెరుగు తినండి. గర్భిణీ స్త్రీలు, పిల్లలకు ఎక్కువ పోషకాహారం కావాలి. ఆంగన్‌వాడీలో ఉచిత ఆహారం.",
        "hi": "चावल + दाल + सब्ज़ी + दही खाएँ। गर्भवती महिलाओं और बच्चों को ज़्यादा पोषण चाहिए।",
    },
    "first_aid": {
        "en": "Keep bandage, cotton, antiseptic, ORS, paracetamol at home. Burns: cool water 10 min - never toothpaste/ghee.",
        "te": "ఇంట్లో పట్టీలు, పత్తి, ఆంటిసెప్టిక్, ORS ఉంచండి. కాలిన గాయాలకు చల్ల నీరు 10 నిమిషాలు.",
        "hi": "घर पर पट्टी, रुई, एंटीसेप्टिक, ORS रखें। जलने पर 10 मिनट ठंडा पानी।",
    },
    "fever": {
        "en": "Rest, drink fluids, paracetamol. If over 3 days or with rash/severe pain - free dengue/typhoid test at PHC.",
        "te": "విశ్రాంతి, ద్రవాలు, పారాసిటమాల్. 3 రోజులకు పైగా జ్వరం - PHC లో ఉచిత పరీక్ష.",
        "hi": "आराम, तरल, पैरासिटामोल। 3 दिन से ज़्यादा बुखार - PHC में मुफ़्त जाँच।",
    },
    "cold_cough": {
        "en": "Warm fluids, steam twice a day, salt-water gargling. Over 2 weeks - free TB test at PHC.",
        "te": "వేడి ద్రవాలు, ఆవిరి, ఉప్పునీటి పుక్కిట. 2 వారాలకు పైగా - PHC లో ఉచిత క్షయ పరీక్ష.",
        "hi": "गर्म तरल, भाप, गरारे। 2 हफ़्ते से ज़्यादा - PHC में मुफ़्त टीबी जाँच।",
    },
    "headache": {
        "en": "Rest in a quiet dark room, drink water, wet cloth on forehead. Sudden worst-ever headache - call 108.",
        "te": "నిశ్శబ్ద గదిలో విశ్రాంతి, నీరు త్రాగండి, నుదుటిపై తడి గుడ్డ. హఠాత్ తీవ్ర నొప్పి - 108.",
        "hi": "शांत कमरे में आराम, पानी पिएँ, माथे पर गीला कपड़ा। अचानक तेज़ दर्द - 108।",
    },
    "stomach_pain": {
        "en": "Sip warm water, avoid oily/spicy food. Severe pain or with vomiting/fever - see doctor.",
        "te": "వేడి నీరు త్రాగండి, నూనె/మసాలా ఆహారం మానేయండి. తీవ్రమైతే డాక్టర్.",
        "hi": "गर्म पानी पिएँ, तला/मसालेदार न लें। तेज़ दर्द - डॉक्टर।",
    },
    "chest_pain": {
        "en": "EMERGENCY - call 108 NOW. Sit down, loosen clothes, keep calm. Do not walk or drive.",
        "te": "అత్యవసరం - వెంటనే 108 కు కాల్ చేయండి. కూర్చోండి, ప్రశాంతంగా ఉండండి.",
        "hi": "EMERGENCY - तुरंत 108 पर कॉल करें। बिठाएँ, शांत रखें।",
    },
    "fracture": {
        "en": "Do NOT move the limb or try to set it. Immobilize with stick + cloth. Go to hospital / call 108.",
        "te": "అవయవం కదలించవద్దు. కర్ర + గుడ్డతో కట్టండి. ఆసుపత్రికి వెళ్లండి / 108.",
        "hi": "अंग हिलाएँ नहीं। छड़ी + कपड़े से स्थिर करें। अस्पताल / 108।",
    },
    "bleeding": {
        "en": "Press firmly with clean cloth 10 min, raise the limb. Heavy bleeding - call 108.",
        "te": "శుభ్ర గుడ్డతో 10 నిమిషాలు గట్టిగా నొక్కండి. ఎక్కువ రక్తం - 108.",
        "hi": "साफ़ कपड़े से 10 मिनट दबाएँ, अंग ऊपर उठाएँ। ज़्यादा खून - 108।",
    },
    "diarrhea": {
        "en": "ORS saves lives - 1 packet in 1 litre water, sip continuously. Blood in stool - go to PHC.",
        "te": "ORS ప్రాణరక్షక - 1 లీటరు నీటిలో 1 సంచి, త్రాగుతూ ఉండండి. మలంలో రక్తం - PHC.",
        "hi": "ORS जान बचाता है - 1 लीटर पानी में 1 पैकेट, लगातार पिएँ। मल में खून - PHC।",
    },
}


def detect_lang(text):
    if any("\u0C00" <= ch <= "\u0C7F" for ch in text):
        return "te"
    if any("\u0900" <= ch <= "\u097F" for ch in text):
        return "hi"
    return "en"


def get_answer(query, lang=None):
    q = query.lower()
    lang = lang or detect_lang(query)
    for topic, words in TOPICS.items():
        if any(w in q for w in words):
            return KB[topic].get(lang) or KB[topic]["en"]
    return None
