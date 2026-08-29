"""
ArogyaMitra engine - multilingual (Telugu / Hindi / English).
Gemini if GEMINI_API_KEY is set; offline KB otherwise.
"""

import os
import re

GEMINI_KEY = os.environ.get("GEMINI_API_KEY", "") or os.environ.get(
    "GOOGLE_API_KEY", "")
_gemini_model = None
if GEMINI_KEY:
    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_KEY)
        _gemini_model = genai.GenerativeModel("gemini-1.5-flash")
    except Exception as e:
        print("Gemini init failed, offline KB will be used:", e)

SYSTEMPT = (
    "You are ArogyaMitra, a rural health information assistant for "
    "Andhra Pradesh, India. General non-diagnostic health info only. "
    "Never diagnose or prescribe. Advise the PHC for concerns and "
    "108/112 for emergencies. IMPORTANT: reply in the SAME language "
    "the user wrote in (Telugu question = full Telugu answer, Hindi "
    "= Hindi, English = English). Keep answers short and simple."
)

_URGENT_WORDS = [
    "chest pain", "breathless", "unconscious", "seizure", "fits",
    "heavy bleeding", "poison", "snake bite", "snakebite", "scorpion",
    "suicide", "stroke", "paralysis", "not breathing", "heart attack",
    "ఛాతి నొప్పి", "స్పృహ లేదు", "కుప్పకూల", "మూర్ఛ", "పాము",
    "విషము", "ఆవులింట", "రక్తపు వాంతులు",
    "सीने में दर्द", "सांस नहीं", "बेहोश", "दौरा", "खून", "जहर",
    "सांप", "आत्महत्या",
]

URGENT_MSG = {
    "en": "🚨 This sounds URGENT. Call 108 / 112 NOW.",
    "te": "🚨 ఇది తీవ్రమైన పరిస్థితి కావచ్చు. వెంటనే 108 / 112 కు "
          "కాల్ చేయండి.",
    "hi": "🚨 यह गंभीर स्थिति हो सकती है। तुरंत 108 / 112 पर कॉल करें।",
}


def is_urgent(text):
    t = text.lower()
    return any(w in t for w in _URGENT_WORDS)


def emergency_block(text):
    urgent = is_urgent(text)
    return urgent, (URGENT_MSG["en"] if urgent else "")


def detect_lang(text):
    if re.search(r"[\u0C00-\u0C7F]", text):
        return "te"
    if re.search(r"[\u0900-\u097F]", text):
        return "hi"
    return "en"


TOPICS = {
    "headache": ["headache", "head pain", "migraine", "తలనొప్పి",
                 "sar dard", "सिरदर्द", "सिर दर्द"],
    "fever": ["fever", "temperature", "జ్వరం", "bukhar", "बुखार"],
    "cough_cold": ["cough", "cold", "throat", "దగ్గు", "జలుబు",
                   "గొంతు", "khansi", "जुकाम", "खांसी", "गला"],
    "loose_motion": ["loose motion", "diarrhea", "diarrhoea",
                     "విరోచనాలు", "డయేరియా", "dast", "दस्त"],
    "vomiting": ["vomit", "nausea", "వాంతులు", "ulti", "उल्टी"],
    "stomach_pain": ["stomach pain", "stomach ache", "abdominal",
                     "కడుపు", "pet dard", "पेट दर्द"],
    "dengue": ["dengue", "డెంగ్యూ", "डेंगू"],
    "diabetes": ["diabetes", "sugar", "షుగర్", "మధుమేహం", "शुगर",
                 "मधुमेह"],
    "bp": ["blood pressure", "hypertension", "బీపీ", "बीपी"],
    "wound": ["wound", "injury", "గాయం", "ज़ख्म", "जख्म", "चोट"],
    "burn": ["burn", "కాలిన", "మంట", "जलन", "झुलस"],
    "dog_bite": ["dog bite", "rabies", "కుక్క కాటు",
                 "कुत्ते का काटना", "कुत्ते ने"],
    "snake_bite": ["snake bite", "snakebite", "పాము కాటు",
                   "सांप का काटना", "सांप ने"],
    "acidity": ["acidity", "gas", "heartburn", "యాసిడిటీ", "గ్యాస్",
                "एसिडिटी", "गैस"],
    "toothache": ["tooth", "teeth", "పళ్లు", "दांत", "दाँत"],
    "ear_pain": ["ear", "చెవి", "చెవుల", "कान"],
    "eye": ["eye", "vision", "కళ్లు", "కన్ను", "आंख", "आँख"],
    "jaundice": ["jaundice", "yellow", "కామెర్లు", "पीलिया"],
    "periods": ["period", "menstrual", "నెలసరి", "माहवारी",
                "पीरियड्स"],
    "pregnancy": ["pregnan", "antenatal", "గర్భిణీ", "గర్భం",
                  "गर्भ"],
    "child_health": ["child", "baby", "vaccin", "పిల్లల", "టీకా",
                     "बच्चे", "टीका"],
    "stress": ["stress", "anxiety", "depression", "ఒత్తిడి", "तनाव",
               "डिप्रेशन"],
    "nutrition": ["nutrition", "diet", "vitamin", "anemia", "ఆహారం",
                  "పోషక", "आहार", "पोषण"],
    "allergy": ["allergy", "itching", "rash", "skin", "దద్దుర్లు",
                "దురద", "खुजली", "एलर्जी"],
}

ANSWERS = {}

def _add(topic, en, te, hi):
    ANSWERS[topic] = {"en": en, "te": te, "hi": hi}
_add("headache",
    "**Headache - general care**\n- Rest in a quiet, dark room; "
    "drink plenty of water.\n- A wet cloth on the forehead helps.\n"
    "- Paracetamol may help (follow label dose).\n\n**See a doctor "
    "if:** pain is severe or lasts over 2-3 days, or comes with "
    "vomiting, fever or blurred vision.\n⚠️ Sudden worst-ever "
    "headache → call **108**.",
    "**తలనొప్పి - సాధారణ జాగ్రత్తలు**\n- నిశ్శబ్ద గదిలో విశ్రాంతి; "
    "ఎక్కువ నీరు త్రాగండి.\n- నుదుటిపై తడి గుడ్డ పెట్టండి.\n- "
    "పారాసిటమాల్ ఉపశమనం ఇస్తుంది.\n\n**డాక్టర్‌ను చూడండి:** నొప్పి "
    "తీవ్రంగా లేదా 2-3 రోజులకు పైగా ఉంటే.\n⚠️ హఠాత్ తీవ్ర "
    "తలనొప్పి → **108** కు కాల్ చేయండి.",
    "**सिरदर्द - सामान्य देखभाल**\n- शांत कमरे में आराम करें; खूब "
    "पानी पिएँ।\n- माथे पर गीला कपड़ा रखें।\n- पैरासिटामोल ले सकते "
    "हैं।\n\n**डॉक्टर से मिलें अगर:** दर्द तेज़ हो या 2-3 दिन से "
    "ज़्यादा रहे।\n⚠️ अचानक बहुत तेज़ सिरदर्द → **108** पर कॉल करें।")

_add("fever",
    "**Fever - general care**\n- Drink plenty of fluids (water, "
    "ORS); rest.\n- Paracetamol reduces fever - correct dose only.\n\n"
    "**See a doctor if:** fever lasts over 3 days, is very high, or "
    "comes with rash, severe body pain, vomiting or breathlessness "
    "(could be dengue/typhoid).\n⚠️ Fever with confusion or bleeding "
    "→ call **108**.",
    "**జ్వరం - సాధారణ జాగ్రత్తలు**\n- ఎక్కువ ద్రవాలు త్రాగండి "
    "(నీరు, ORS); విశ్రాంతి.\n- పారాసిటమాల్ జ్వరం తగ్గిస్తుంది.\n\n"
    "**డాక్టర్‌ను చూడండి:** జ్వరం 3 రోజులకు పైగా, చాలా ఎక్కువగా, "
    "లేదా దద్దుర్లు, తీవ్ర నొప్పి, వాంతులతో (డెంగ్యూ/టైఫాయిడ్ "
    "కావచ్చు).\n⚠️ జ్వరంతో మతిమరుపు లేదా రక్తస్రావం → **108**.",
    "**बुखार - सामान्य देखभाल**\n- खूब तरल लें (पानी, ORS); आराम "
    "करें।\n- पैरासिटामोल बुखार कम करता है।\n\n**डॉक्टर से मिलें "
    "अगर:** बुखार 3 दिन से ज़्यादा, बहुत तेज़, या दाने, तेज़ दर्द, "
    "उल्टी साथ हो (डेंगू/टाइफाइड हो सकता है)।\n⚠️ बेहोशी या खून → "
    "**108**.")

_add("cough_cold",
    "**Cough and cold - general care**\n- Warm fluids; steam twice "
    "a day.\n- Salt-water gargling for throat pain.\n- Avoid cold "
    "drinks and dust.\n\n**See a doctor if:** cough over 2 weeks, "
    "blood in sputum, weight loss or breathlessness (TB testing at "
    "the PHC is free).\n⚠️ Blue lips → call **108**.",
    "**దగ్గు, జలుబు - సాధారణ జాగ్రత్తలు**\n- వేడి ద్రవాలు; రోజుకు "
    "రెండుసార్లు ఆవిరి.\n- ఉప్పు నీటి పుక్కిట.\n- చల్ల పానీయాలు, "
    "దుమ్ము దూరంగా.\n\n**డాక్టర్‌ను చూడండి:** దగ్గు 2 వారాలకు "
    "పైగా, కఫంలో రక్తం, బరువు తగ్గడం (క్షయ పరీక్ష PHC లో ఉచితం).\n"
    "⚠️ పెదవులు నీలం → **108**.",
    "**खांसी-जुकाम - सामान्य देखभाल**\n- गर्म तरल; दिन में दो बार "
    "भाप।\n- नमक-पानी से गरारे।\n- ठंडी चीज़ें और धूल से बचें।\n\n"
    "**डॉक्टर से मिलें अगर:** खांसी 2 हफ़्ते से ज़्यादा, बलगम में "
    "खून, वज़न घटना (टीबी जाँच PHC में मुफ़्त)।\n⚠️ होंठ नीले → "
    "**108**.")

_add("loose_motion",
    "**Loose motions - general care**\n- Most important: prevent "
    "dehydration. One ORS packet in 1 litre clean water, sip "
    "continuously.\n- Light food (rice-curd, banana).\n- Wash hands "
    "with soap.\n**See a doctor if:** over 6 motions a day, blood "
    "in stool, fever, or dehydration signs.\n⚠️ Severe dehydration "
    "in child/elderly → call **108**.",
    "**విరోచనాలు - సాధారణ జాగ్రత్తలు**\n- ముఖ్యం: నిర్జలీకరణ "
    "నివారణ. ORS సంచి 1 లీటరు నీటిలో కలిపి త్రాగండి.\n- తేలికపాటి "
    "ఆహారం (పెరుగన్నం, అరటి).\n- సబ్బుతో చేతులు కడగండి.\n\n"
    "**డాక్టర్‌ను చూడండి:** రోజుకు 6 కంటే ఎక్కువ, మలంలో రక్తం, "
    "జ్వరం.\n⚠️ తీవ్ర నిర్జలీకరణ → **108**.",
    "**दस्त - सामान्य देखभाल**\n- सबसे ज़रूरी: ORS पैकेट 1 लीटर "
    "पानी में मिलाकर पिएँ।\n- हल्का खाना (दही-चावल, केला)।\n- साबुन "
    "से हाथ धोएँ।\n\n**डॉक्टर से मिलें अगर:** 6 से ज़्यादा दस्त, मल "
    "में खून, बुखार।\n⚠️ तेज़ पानी की कमी → **108**.")

_add("vomiting",
    "**Vomiting - general care**\n- Sip ORS or water slowly in "
    "small sips.\n- Rest the stomach a few hours, then light food.\n"
    "- Avoid oily/spicy food.\n\n**See a doctor if:** vomiting over "
    "24 hours, blood in vomit, severe stomach pain.\n⚠️ Non-stop "
    "vomiting with blood → call **108**.",
    "**వాంతులు - సాధారణ జాగ్రత్తలు**\n- ORS/నీరు చిన్న చుక్కలుగా "
    "త్రాగండి.\n- కొన్ని గంటలు విశ్రాంతి, తర్వాత తేలికపాటి "
    "ఆహారం.\n- నూనె/మసాలా మానేయండి.\n\n**డాక్టర్‌ను చూడండి:** 24 "
    "గంటలకు పైగా వాంతులు, రక్తం, తీవ్ర నొప్పి.\n⚠️ రక్తంతో "
    "వాంతులు → **108**.",
    "**उल्टी - सामान्य देखभाल**\n- ORS/पानी धीरे-धीरे छोटे घूँटों "
    "में पिएँ।\n- कुछ घंटे आराम, फिर हल्का खाना।\n- तला/मसालेदार न "
    "लें।\n\n**डॉक्टर से मिलें अगर:** उल्टी 24 घंटे से ज़्यादा, खून, "
    "तेज़ दर्द।\n⚠️ खून के साथ उल्टी → **108**.")

_add("stomach_pain",
    "**Stomach pain - general care**\n- Sip warm water; avoid "
    "oily, spicy food.\n- No painkillers on an empty stomach.\n\n"
    "**See a doctor if:** pain is severe, lower right side, with "
    "vomiting, fever, or lasts over a day.\n⚠️ Severe sudden pain "
    "with hard belly → call **108**.",
    "**కడుపు నొప్పి - సాధారణ జాగ్రత్తలు**\n- వేడి నీరు త్రాగండి; "
    "నూనె, మసాలా మానేయండి.\n- ఖాళీ కడుపుతో మాత్రలు వేసుకోకండి.\n\n"
    "**డాక్టర్‌ను చూడండి:** తీవ్రంగా, కుడి కింది వైపు, వాంతులు, "
    "జ్వరంతో.\n⚠️ హఠాత్ తీవ్ర నొప్పి → **108**.",
    "**पेट दर्द - सामान्य देखभाल**\n- गर्म पानी पिएँ; तला/मसालेदार "
    "न लें।\n- खाली पेट दर्द निवारक न लें।\n\n**डॉक्टर से मिलें "
    "अगर:** दर्द तेज़, दाईं ओर नीचे, उल्टी/बुखार साथ।\n⚠️ अचानक "
    "तेज़ दर्द → **108**.")

_add("dengue",
    "**Dengue - what to know**\n- High fever with severe body/joint "
    "pain and headache may be dengue.\n- Drink lots of fluids; "
    "paracetamol ONLY - never aspirin/ibuprofen.\n- Blood test "
    "(NS1/platelets) at the PHC is free.\n\n**Go to hospital now "
    "if:** bleeding gums/nose, black stools, severe stomach pain, "
    "drowsiness.\n**Prevention:** no open water storage; nets and "
    "repellents in daytime too.",
    "**డెంగ్యూ - సమాచారం**\n- ఎక్కువ జ్వరంతో తీవ్ర శరీర/కీళ్ల "
    "నొప్పులు డెంగ్యూ కావచ్చు.\n- ఎక్కువ ద్రవాలు; పారాసిటమాల్ మాత్రమే "
    "- ఆస్పిరిన్/ఐబుప్రోఫెన్ వద్దు.\n- NS1 రక్త పరీక్ష PHC లో "
    "ఉచితం.\n\n**వెంటనే ఆసుపత్రికి:** చిగుళ్ల/ముక్కు నుండి రక్తం, "
    "నల్ల మలం, తీవ్ర కడుపు నొప్పి.\n**నివారణ:** నీరు నిల్వ "
    "ఉంచకండి; పగటిపుచ్చులు ఉండండి.",
    "**डेंगू - जानकारी**\n- तेज़ बुखार के साथ तेज़ शरीर/जोड़ों का "
    "दर्द डेंगू हो सकता है।\n- खूब तरल लें; केवल पैरासिटामोल - "
    "आस्प्रिन/आइबुप्रोफेन कभी नहीं।\n- NS1 जाँच PHC में मुफ़्त।\n\n"
    "**तुरंत अस्पताल जाएँ:** मसूड़ों/नाक से खून, काला मल, तेज़ पेट "
    "दर्द, झपकी।\n**बचाव:** खुले पानी को जमा न करें; दिन में भी "
    "मच्छरदानी।")

_add("diabetes",
    "**Diabetes - general information**\n- Less sugar, white rice "
    "and fried food; more vegetables and whole grains.\n- Walk 30 "
    "minutes daily.\n- Take prescribed tablets regularly.\n- Free "
    "sugar testing at the PHC.\n\n**Danger signs:** wounds that "
    "don't heal, vision changes, vomiting with very high sugar → "
    "see a doctor urgently.",
    "**షుగర్ (మధుమేహం) - సమాచారం**\n- తక్కువ షుగర్, బియ్యం, వేపుళ్లు; "
    "ఎక్కువ కూరగాయలు.\n- రోజు 30 నిమిషాలు నడక.\n- మందులు క్రమం "
    "తప్పకుండా.\n- PHC లో ఉచిత పరీక్ష.\n\n**ప్రమాద సూచనలు:** "
    "నయం కాని గాయాలు, కళ్ల సమస్యలు → వెంటనే డాక్టర్.",
    "**शुगर (मधुमेह) - जानकारी**\n- कम शुगर, चावल, तला खाना; ज़्यादा "
    "सब्ज़ियाँ।\n- रोज़ 30 मिनट पैदल चलें।\n- दवाएँ नियमित लें।\n- "
    "PHC में मुफ़्त जाँच।\n\n**ख़तरे के संकेत:** ठीक न होने वाले "
    "घाव, धुंधला दिखना → तु

> ⚠️ The response reached the length limit. Reply **continue** to get the rest.
