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
    "You are ArogyaMitra, a rural health info assistant in Andhra "
    "Pradesh, India. General non-diagnostic info only; never diagnose "
    "or prescribe. Advise the nearest PHC and 108/112 for emergencies. "
    "IMPORTANT: reply in the SAME language the user used - Telugu "
    "question gets a full Telugu answer, Hindi gets Hindi, English "
    "gets English. Keep it short and simple."
)

_URGENT = [
    "chest pain", "breathless", "unconscious", "seizure", "fits",
    "heavy bleeding", "poison", "snake bite", "snakebite", "scorpion",
    "suicide", "stroke", "paralysis", "not breathing", "heart attack",
    "ఛాతి నొప్పి", "స్పృహ లేదు", "కుప్పకూల", "మూర్ఛ", "పాము", "విషము",
    "सीने में दर्द", "सांस नहीं", "बेहोश", "दौरा", "खून", "जहर", "सांप",
]

URGENT_MSG = {
    "en": "🚨 This sounds URGENT. Call 108 / 112 NOW.",
    "te": "🚨 ఇది తీవ్రమైన పరిస్థితి కావచ్చు. వెంటనే 108 / 112 కు కాల్ చేయండి.",
    "hi": "🚨 यह गंभीर स्थिति हो सकती है। तुरंत 108 / 112 पर कॉल करें।",
}


def is_urgent(text):
    t = text.lower()
    return any(w in t for w in _URGENT)


def emergency_block(text):
    urgent = is_urgent(text)
    return urgent, (URGENT_MSG["en"] + "\n\nGo to the nearest hospital immediately."
                    if urgent else "No emergency signs detected. See the Emergency page for helpline numbers.")


def detect_lang(text):
    if re.search(r"[\u0C00-\u0C7F]", text):
        return "te"
    if re.search(r"[\u0900-\u097F]", text):
        return "hi"
    return "en"


TOPICS = {
    "headache": ["headache", "head pain", "migraine", "తలనొప్పి", "sar dard", "सिरदर्द"],
    "fever": ["fever", "temperature", "జ్వరం", "bukhar", "बुखार"],
    "cough_cold": ["cough", "cold", "throat", "దగ్గు", "జలుబు", "గొంతు", "जुकाम", "खांसी"],
    "loose_motion": ["loose motion", "diarrhea", "diarrhoea", "విరోచనాలు", "dast", "दस्त"],
    "vomiting": ["vomit", "nausea", "వాంతులు", "ulti", "उल्टी"],
    "stomach_pain": ["stomach pain", "stomach ache", "abdominal", "కడుపు", "pet dard", "पेट दर्द"],
    "dengue": ["dengue", "డెంగ్యూ", "डेंगू"],
    "diabetes": ["diabetes", "sugar", "షుగర్", "మధుమేహం", "शुगर", "मधुमेह"],
    "bp": ["blood pressure", "hypertension", "బీపీ", "बीपी"],
    "wound": ["wound", "injury", "గాయం", "ज़ख्म", "जख्म", "चोट"],
    "burn": ["burn", "కాలిన", "మంట", "जलन", "झुलस"],
    "dog_bite": ["dog bite", "rabies", "కుక్క కాటు", "कुत्ते"],
    "snake_bite": ["snake bite", "snakebite", "పాము కాటు", "सांप"],
    "acidity": ["acidity", "gas", "heartburn", "యాసిడిటీ", "గ్యాస్", "एसिडिटी", "गैस"],
    "toothache": ["tooth", "teeth", "పళ్లు", "दांत", "दाँत"],
    "ear_pain": ["ear", "చెవి", "చెవుల", "कान"],
    "eye": ["eye", "vision", "కళ్లు", "కన్ను", "आंख", "आँख"],
    "jaundice": ["jaundice", "yellow", "కామెర్లు", "पीलिया"],
    "periods": ["period", "menstrual", "నెలసరి", "माहवारी"],
    "pregnancy": ["pregnan", "antenatal", "గర్భిణీ", "గర్భం", "गर्भ"],
    "child_health": ["child", "baby", "vaccin", "పిల్లల", "టీకా", "बच्चे", "टीका"],
    "stress": ["stress", "anxiety", "depression", "ఒత్తిడి", "तनाव", "डिप्रेशन"],
    "nutrition": ["nutrition", "diet", "vitamin", "anemia", "ఆహారం", "पोषण", "आहार"],
    "allergy": ["allergy", "itching", "rash", "skin", "దద్దుర్లు", "దురద", "खुजली", "एलर्जी"],
}

ANSWERS = {
    "headache": {
        "en": "**Headache - care:** Rest in a quiet dark room, drink water, wet cloth on forehead. Paracetamol may help (label dose). See a doctor if severe or over 2-3 days. ⚠️ Sudden worst-ever headache → call **108**.",
        "te": "**తలనొప్పి - జాగ్రత్తలు:** నిశ్శబ్ద గదిలో విశ్రాంతి, ఎక్కువ నీరు త్రాగండి, నుదుటిపై తడి గుడ్డ. పారాసిటమాల్ తీసుకోవచ్చు. నొప్పి 2-3 రోజులకు పైగా ఉంటే డాక్టర్‌ను చూడండి. ⚠️ హఠాత్ తీవ్ర నొప్పి → **108**.",
        "hi": "**सिरदर्द - देखभाल:** शांत कमरे में आराम, खूब पानी, माथे पर गीला कपड़ा। पैरासिटामोल ले सकते हैं। दर्द 2-3 दिन से ज़्यादा हो तो डॉक्टर से मिलें। ⚠️ अचानक तेज़ दर्द → **108**.",
    },
    "fever": {
        "en": "**Fever - care:** Drink fluids (water, ORS), rest, paracetamol for fever. See a doctor if fever lasts over 3 days or comes with rash, severe body pain or vomiting (could be dengue/typhoid - free test at PHC). ⚠️ Confusion or bleeding → call **108**.",
        "te": "**జ్వరం - జాగ్రత్తలు:** ఎక్కువ ద్రవాలు (నీరు, ORS), విశ్రాంతి, పారాసిటమాల్. జ్వరం 3 రోజులకు పైగా లేదా దద్దుర్లు, తీవ్ర నొప్పి, వాంతులతో ఉంటే డాక్టర్‌ను చూడండి (డెంగ్యూ/టైఫాయిడ్ కావచ్చు - PHC లో ఉచిత పరీక్ష). ⚠️ మతిమరుపు/రక్తస్రావం → **108**.",
        "hi": "**बुखार - देखभाल:** खूब तरल (पानी, ORS), आराम, पैरासिटामोल। बुखार 3 दिन से ज़्यादा या दाने, तेज़ दर्द, उल्टी के साथ हो तो डॉक्टर से मिलें (डेंगू/टाइफाइड - PHC में मुफ़्त जाँच)। ⚠️ बेहोशी/खून → **108**.",
    },
    "cough_cold": {
        "en": "**Cough/cold - care:** Warm fluids, steam twice a day, salt-water gargling. Avoid dust and cold drinks. See a doctor if cough lasts over 2 weeks, blood in sputum, weight loss or breathlessness (free TB test at PHC). ⚠️ Blue lips → call **108**.",
        "te": "**దగ్గు/జలుబు - జాగ్రత్తలు:** వేడి ద్రవాలు, ఆవిరి రోజుకు రెండుసార్లు, ఉప్పునీటి పుక్కిట. దుమ్ము, చల్ల పానీయాలు మానేయండి. దగ్గు 2 వారాలకు పైగా, కఫంలో రక్తం, బరువు తగ్గడం ఉంటే డాక్టర్‌ను చూడండి (PHC లో ఉచిత క్షయ పరీక్ష). ⚠️ పెదవులు నీలం → **108**.",
        "hi": "**खांसी/जुकाम - देखभाल:** गर्म तरल, भाप दिन में दो बार, नमक-पानी के गरारे। धूल और ठंडी चीज़ें बचें। खांसी 2 हफ़्ते से ज़्यादा, बलगम में खून, वज़न घटना हो तो डॉक्टर से मिलें (PHC में मुफ़्त टीबी जाँच)। ⚠️ होंठ नीले → **108**.",
    },
    "loose_motion": {
        "en": "**Loose motions - care:** Most important is ORS - mix one packet in 1 litre clean water and sip continuously. Light food (rice-curd, banana). Wash hands with soap. See a doctor if over 6 motions a day, blood in stool, or fever. ⚠️ Severe dehydration in child/elderly → call **108**.",
        "te": "**విరోచనాలు - జాగ్రత్తలు:** ముఖ్యంగా ORS - ఒక సంచిని 1 లీటరు శుభ్ర నీటిలో కలిపి త్రాగండి. తేలికపాటి ఆహారం (పెరుగన్నం, అరటి). సబ్బుతో చేతులు కడగండి. రోజుకు 6 కంటే ఎక్కువ, మలంలో రక్తం, జ్వరం ఉంటే డాక్టర్‌ను చూడండి. ⚠️ తీవ్ర నిర్జలీకరణ → **108**.",
        "hi": "**दस्त - देखभाल:** सबसे ज़रूरी ORS - एक पैकेट 1 लीटर साफ़ पानी में मिलाकर पिएँ। हल्का खाना (दही-चावल, केला)। साबुन से हाथ धोएँ। 6 से ज़्यादा दस्त, मल में खून, बुखार हो तो डॉक्टर से मिलें। ⚠️ तेज़ पानी की कमी → **108**.",
    },
    "vomiting": {
        "en": "**Vomiting - care:** Sip ORS/water slowly in small sips. Rest the stomach, then light food. Avoid oily/spicy food. See a doctor if vomiting lasts over 24 hours or has blood. ⚠️ Non-stop vomiting with blood → call **108**.",
        "te": "**వాంతులు - జాగ్రత్తలు:** ORS/నీరు చిన్న చుక్కలుగా త్రాగండి. కడుపుకు విశ్రాంతి, తర్వాత తేలికపాటి ఆహారం. నూనె/మసాలా మానేయండి. 24 గంటలకు పైగా లేదా రక్తంతో ఉంటే డాక్టర్‌ను చూడండి. ⚠️ రక్తంతో ఆగని వాంతులు → **108**.",
        "hi": "**उल्टी - देखभाल:** ORS/पानी धीरे-धीरे छोटे घूँटों में पिएँ। पेट को आराम, फिर हल्का खाना। तला/मसालेदार न लें। उल्टी 24 घंटे से ज़्यादा या खून के साथ हो तो डॉक्टर से मिलें। ⚠️ खून के साथ लगातार उल्टी → **108**.",
    },
    "stomach_pain": {
        "en": "**Stomach pain - care:** Sip warm water; avoid oily, spicy food. No painkillers on an empty stomach. See a doctor if pain is severe, on the lower right side, or with vomiting/fever. ⚠️ Severe sudden pain with hard belly → call **108**.",
        "te": "**కడుపు నొప్పి - జాగ్రత్తలు:** వేడి నీరు త్రాగండి; నూనె, మసాలా మానేయండి. ఖాళీ కడుపుతో మాత్రలు వేసుకోకండి. నొప్పి తీవ్రంగా, కుడి కింది వైపు, వాంతులు/జ్వరంతో ఉంటే డాక్టర్‌ను చూడండి. ⚠️ హఠాత్ తీవ్ర నొప్పి → **108**.",
        "hi": "**पेट दर्द - देखभाल:** गर्म पानी पिएँ; तला/मसालेदार न लें। खाली पेट दर्द निवारक न लें। दर्द तेज़, दाईं ओर नीचे, उल्टी/बुखार के साथ हो तो डॉक्टर से मिलें। ⚠️ अचानक तेज़ दर्द → **108**.",
    },
    "dengue": {
        "en": "**Dengue:** High fever with severe body/joint pain may be dengue. Drink lots of fluids; paracetamol ONLY - never aspirin/ibuprofen. Free NS1 blood test at PHC. Go to hospital NOW if: bleeding gums/nose, black stools, severe stomach pain, drowsiness. Prevention: no open water storage, use nets in daytime too.",
        "te": "**డెంగ్యూ:** ఎక్కువ జ్వరంతో తీవ్ర శరీర/కీళ్ల నొప్పులు డెంగ్యూ కావచ్చు. ఎక్కువ ద్రవాలు; పారాసిటమాల్ మాత్రమే - ఆస్పిరిన్/ఐబుప్రోఫెన్ వద్దు. PHC లో ఉచిత NS1 పరీక్ష. చిగుళ్ల/ముక్కు నుండి రక్తం, తీవ్ర కడుపు నొప్పి ఉంటే వెంటనే ఆసుపత్రి. నివారణ: నీరు నిల్వ ఉంచకండి, పగటిపుచ్చులు వాడండి.",
        "hi": "**डेंगू:** तेज़ बुखार के साथ तेज़ शरीर/जोड़ों का दर्द डेंगू हो सकता है। खूब तरल; केवल पैरासिटामोल - आस्प्रिन/आइबुप्रोफेन कभी नहीं। PHC में मुफ़्त NS1 जाँच। मसूड़ों/नाक से खून, तेज़ पेट दर्द हो तो तुरंत अस्पताल। बचाव: खुला पानी जमा न करें, दिन में भी मच्छरदानी।",
    },
    "diabetes": {
        "en": "**Diabetes - info:** Less sugar, white rice and fried food; more vegetables. Walk 30 minutes daily. Take prescribed tablets regularly. Free sugar test at PHC. Danger: wounds that don't heal, vision changes → see a doctor urgently.",
        "te": "**షుగర్ - సమాచారం:** తక్కువ షుగర్, బియ్యం, వేపుళ్లు; ఎక్కువ కూరగాయలు. రోజు 30 నిమిషాలు నడక. మందులు క్రమం తప్పకుండా. PHC లో ఉచిత పరీక్ష. నయం కాని గాయాలు, కళ్ల సమస్యలు → వెంటనే డాక్టర్.",
        "hi": "**शुगर - जानकारी:** कम शुगर, चावल, तला खाना; ज़्यादा सब्ज़ियाँ। रोज़ 30 मिनट पैदल चलें। दवाएँ नियमित लें। PHC में मुफ़त जाँच। ठीक न होने वाले घाव, धुंधला दिखना → तुरंत डॉक्टर।",
    },
    "bp": {
        "en": "**Blood pressure -:** Less salt (under 1 tsp/day), avoid pickles and packaged snacks. Walk daily; no smoking/alcohol. Take BP tablets every day even when feeling fine. ⚠️ BP with severe headache, chest pain or blurred vision → call **108**.",
        "te": "**బీపీ - సమాచారం:** తక్కువ ఉప్పు (రోజుకు 1 టీస్పూన్ కంటే తక్కువ), ఊరగాయలు, ప్యాకెట్ స్నాక్స్ మానేయండి. రోజు నడక; పొగతాగడం/మద్యం లేదు. బీపీ మాత్రలు రోజూ తీసుకోండి. ⚠️ బీపీతో తీవ్ర తలనొప్పి, ఛాతి నొప్పి → **108**.",
        "hi": "**बीपी - जानकारी:** कम नमक (दिन में 1 चम्मच से कम), अचार और पैकेट स्नैक्स बचें। रोज़ पैदल चलें; धूम्रपान/शराब नहीं। बीपी की गोली रोज़ लें। ⚠️ बीपी के साथ तेज़ सिरदर्द, सीने में दर्द → **108**.",
    },
    "wound": {
        "en": "**Wound - care:** Wash hands, clean with water and soap around it. Press with a clean cloth to stop bleeding; cover with clean dressing. Do NOT apply mud, turmeric or toothpaste. See a doctor if the cut is deep, bleeding doesn't stop in 10 minutes, or redness/pus appears (may need tetanus injection). ⚠️ Heavy bleeding → call **108**.",
        "te": "**గాయం - జాగ్రత్తలు:** చేతులు కడగండి, నీటితో శుభ్రం చేయండి. రక్తం ఆగిపోవడానికి శుభ్రమైన గుడ్డతో నొక్కండి. మట్టి, పసుపు, టూత్‌పేస్ట్ వేయవద్దు. గాయం లోతుగా, రక్తం ఆగకపోతే, వాపు/చీము ఉంటే డాక్టర్‌ను చూడండి (టీకా అవసరం కావచ్చు). ⚠️ ఎక్కువ రక్తస్రావం → **108**.",
        "hi": "**घाव - देखभाल:** हाथ धोएँ, पानी से साफ़ करें। खून रोकने के लिए साफ़ कपड़े से दबाएँ। मिट्टी, हल्दी, टूथपेस्

