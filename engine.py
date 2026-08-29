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

SYSTEM_PROMPT = (
    "You are ArogyaMitra, a rural health information assistant for "
    "Andhra Pradesh, India. Give general, non-diagnostic health "
    "information only. Never diagnose or prescribe. Advise the PHC "
    "for concerns and 108/112 for emergencies. IMPORTANT: reply in "
    "the SAME language the user wrote in (Telugu question = full "
    "Telugu answer, Hindi = Hindi, English = English). Keep answers "
    "short and simple."
)

# ---------------- emergency detection ----------------
_URGENT_WORDS = [
    "chest pain", "breathless", "unconscious", "seizure", "fits",
    "heavy bleeding", "poison", "snake bite", "snakebite", "scorpion",
    "suicide", "stroke", "paralysis", "not breathing",
    "heart attack",
    "ఛాతి నొప్పి", "తీవ్రమైన", "ప్రాణాంతక", "స్పృహ లేదు", "కుప్పకూల",
    "నాడీ", "మూర్ఛ", "రక్తపు", "పాము", "విష", "ఆవులింట",
    "सीने में दर्द", "सांस नहीं", "बेहोश", "दौरा", "खून", "जहर",
    "सांप", "आत्महत्या",
]


def is_urgent(text):
    t = text.lower()
    return any(w in t for w in _URGENT_WORDS)


URGENT_MSG = {
    "en": "🚨 This sounds URGENT. Call 108 / 112 NOW.\n\n",
    "te": "🚨 ఇది తీవ్రమైన పరిస్థితి కావచ్చు. వెంటనే 108 / 112 కు "
          "కాల్ చేయండి.\n\n",
    "hi": "🚨 यह गंभीर स्थिति हो सकती है। तुरंत 108 / 112 पर कॉल "
          "करें।\n\n",
}


def emergency_block(text):
    """Return (urgent, advice)."""
    urgent = is_urgent(text)
    return urgent, URGENT_MSG["en"] if urgent else ""


# ---------------- language detection ----------------
def detect_lang(text):
    if re.search(r"[\u0C00-\u0C7F]", text):
        return "te"
    if re.search(r"[\u0900-\u097F]", text):
        return "hi"
    return "en"


# ---------------- topic matching ----------------
# topic -> keywords per language (native script + romanised)
TOPICS = {
    "headache": ["headache", "head ache", "head pain", "migraine",
                 "తలనొప్పి", "తల", "sar dard", "सिरदर्द", "सिर दर्द"],
    "fever": ["fever", "temperature", "జ్వరం", "జ్వర", "bukhar",
              "बुखार"],
    "cough_cold": ["cough", "cold", "throat", "sneeze", "దగ్గు",
                   "జలుబు", "గొంతు", "khansi", "जुकाम", "खांसी",
                   "गला"],
    "loose_motion": ["loose motion", "diarrhea", "diarrhoea", "stools",
                     "విరోచన", "డయేరియా", "dast", "दस्त"],
    "vomiting": ["vomit", "nausea", "వాంతులు", "వాంత", "ulti",
                   "उल्टी", "मतली"],
    "stomach_pain": ["stomach pain", "stomach ache", "abdominal",
                     "belly", "కడుపు నొప్పి", "కడుపు", "pet dard",
                     "पेट दर्द"],
    "dengue": ["dengue", "డెంగ్యూ", "डेंगू"],
    "diabetes": ["diabetes", "sugar", "షుగర్", "మధుమేహం",
                 "shugar", "मधुमेह", "शुगर"],
    "bp": ["blood pressure", "hypertension", "బీపీ", "bp",
           "बीपी", "रक्तचाप"],
    "wound": ["wound", "cut", "injury", "గాయం", "కట", "ज़ख्म",
              "जख्म", "चोट"],
    "burn": ["burn", "కాలిన", "మంట", "jalna", "जलन", "झुलस"],
    "dog_bite": ["dog bite", "rabies", "కుక్క కాటు", "कुत्ते ने",
                 "कुत्ते का काटना"],
    "snake_bite": ["snake bite", "snakebite", "పాము కాటు", "सांप ने",
                   "सांप का काटना"],
    "acidity": ["acidity", "gas", "heartburn", "యాసిడిటీ", "గ్యాస్",
                "tezabiyata", "एसिडिटी", "गैस"],
    "toothache": ["tooth", "teeth", "పళ్లు", "దంత", "daant",
                  "दांत", "दाँत"],
    "ear_pain": ["ear", "చెవి", "చెవుల", "kaan", "कान"],
    "eye": ["eye", "vision", "కళ్లు", "కన్ను", "aankh", "आंख",
            "आँख"],
    "jaundice": ["jaundice", "yellow", "కామెర్లు", "पीलिया"],
    "periods": ["period", "menstrual", "నెలసరి", "माहवारी",
                "पीरियड्स"],
    "pregnancy": ["pregnan", "antenatal", "గర్భిణీ", "గర్భం",
                  "garbh", "गर्भ"],
    "child_health": ["child", "baby", "infant", "vaccin", "పిల్లల",
                     "బిడ్డ", "bacche", "बच्चे", "टीका", "tikakaran"],
    "stress": ["stress", "anxiety", "depression", "mental", "ఒత్తిడి",
               "तनाव", "डिप्रेशन"],
    "nutrition": ["nutrition", "diet", "food", "vitamin", "anemia",
                  "ఆహార", "పోషణ", "आहार", "पोषण", "खाना"],
    "allergy": ["allergy", "itching", "rash", "skin", "దద్దుర్లు",
                "దురద", "खुजली", "एलर्जी"],
}

# ---------------- offline answers ----------------
ANSWERS = {
    "headache": {
        "en": "**Headache - general care**\n- Rest in a quiet, dark "
              "room; drink plenty of water.\n- A wet cloth on the "
              "forehead helps.\n- Paracetamol may help (follow label "
              "dose).\n\n**See a doctor if:** pain is severe or "
              "lasts over 2-3 days, or comes with vomiting, fever, "
              "blurred vision or weakness.\n⚠️ Sudden worst-ever "
              "headache → call **108**.",
        "te": "**తలనొప్పి - సాధారణ జాగ్రత్తలు**\n- నిశ్శబ్ద, చీకటి "
              "గదిలో విశ్రాంతి తీసుకోండి; ఎక్కువ నీరు త్రాగండి.\n- "
              "నుదుటిపై తడి గుడ్డ పెట్టండి.\n- పారాసిటమాల్ తగ్గించి "
              "ఉంటుంది (లేబుల్ మోతాదులో).\n\n**డాక్టర్‌ను చూడండి:** "
              "నొప్పి తీవ్రంగా లేదా 2-3 రోజులకు పైగా ఉంటే, వాంతులు, "
              "జ్వరం, కళ్లు మసక లేదా బలహీనతతో ఉంటే.\n⚠️ హఠాత్తుగా "
              "తీవ్ర తలనొప్పి → **108** కు కాల్ చేయండి.",
        "hi": "**सिरदर्द - सामान्य देखभाल**\n- शांत, अंधेरे कमरे में "
              "आराम करें; खूब पानी पिएँ।\n- माथे पर गीला कपड़ा रखें।\n- "
              "पैरासिटामोल ले सकते हैं (लेबल खुराक देखें)।\n\n**डॉक्टर "
              "से मिलें अगर:** दर्द बहुत तेज़ हो या 2-3 दिन से ज़्यादा "
              "रहे, या उल्टी, बुखार, धुंधला दिखना या कमज़ोरी साथ हो।\n"
              "⚠️ अचानक बहुत तेज़ सिरदर्द → **108** पर कॉल करें।",
    },
    "fever": {
        "en": "**Fever - general care**\n- Drink plenty of fluids "
              "(water, ORS, soups); rest.\n- Paracetamol reduces "
              "fever - take the correct dose.\n- Wipe the body with "
              "a wet cloth if very hot.\n\n**See a doctor if:** fever "
              "lasts over 3 days, is very high, or comes with rash, "
              "severe body pain, vomiting or breathlessness (could "
              "be dengue/typhoid).\n⚠️ Fever with confusion or "
              "bleeding → call **108**.",
        "te": "**జ్వరం - సాధారణ జాగ్రత్తలు**\n- ఎక్కువ ద్రవాలు త్రాగండి "
              "(నీరు, ORS); విశ్రాంతి తీసుకోండి.\n- పారాసిటమాల్ జ్వరం "
              "తగ్గిస్తుంది - సరైన మోతాదులో.\n- శరీరం ఎక్కువ వేడిగా "
              "ఉంటే తడి గుడ్డతో తుడవండి.\n\n**డాక్టర్‌ను చూడండి:** "
              "జ్వరం 3 రోజులకు పైగా ఉంటే, చాలా ఎక్కువగా ఉంటే, లేదా "
              "దద్దుర్లు, తీవ్ర నొప్పి, వాంతులు లేదా ఊపిరి తీసుకోవడంలో "
              "ఇబ్బంది ఉంటే (డెంగ్యూ/టైఫాయిడ్ కావచ్చు).\n⚠️ జ్వరంతో "
              "మతిమరుపు లేదా రక్తస్రావం → **108**.",
        "hi": "**बुखार - सामान्य देखभाल**\n- खूब तरल लें (पानी, ORS); "
              "आराम करें।\n- पैरासिटामोल बुखार कम करता है - सही खुराक "
              "लें।\n- बहुत गर्म शरीर को गीले कपड़े से पोंछें।\n\n**डॉक्टर "
              "से मिलें अगर:** बुखार 3 दिन से ज़्यादा हो, बहुत तेज़ हो, "
              "या दाने, तेज़ दर्द, उल्टी या सांस लेने में दिक्कत साथ "
              "हो (डेंगू/टाइफाइड हो सकता है)।\n⚠️ बुखार के साथ बेहोशी "
              "या खून → **108**.",
    },
    "cough_cold": {
        "en": "**Cough and cold - general care**\n- Drink warm "
              "fluids; take steam twice a day.\n- Salt-water gargling "
              "soothes throat pain.\n- Avoid cold drinks and dust.\n\n"
              "**See a doctor if:** cough lasts over 2 weeks, blood "
              "in sputum, weight loss or breathlessness (TB testing "
              "at the PHC is free).\n⚠️ Breathlessness or blue lips → "
              "call **108**.",
        "te": "**దగ్గు, జలుబు - సాధారణ జాగ్రత్తలు**\n- వేడి ద్రవాలు "
              "త్రాగండి; రోజుకు రెండుసార్లు ఆవిరి పట్టండి.\n- ఉప్పు "
              "నీటితో పుక్కిట పట్టండి.\n- చల్ల పానీయాలు, దుమ్ము "
              "దూరంగా ఉండండి.\n\n**డాక్టర్‌ను చూడండి:** దగ్గు 2 "
              "వారాలకు పైగా ఉంటే, కఫంలో రక్తం, బరువు తగ్గడం లేదా "
              "ఊపిరి ఇబ్బంది ఉంటే (క్షయ పరీక్ష PHC లో ఉచితం).\n⚠️ "
              "ఊపిరి ఇబ్బంది లేదా పెదవులు నీలం → **108**.",
        "hi": "**खांसी-जुकाम - सामान्य देखभाल**\n- गर्म तरल पिएँ; दिन "
              "में दो बार भाप लें।\n- नमक-पानी से गरारे करें।\n- ठंडी "
              "चीज़ें और धूल से बचें।\n\n**डॉक्टर से मिलें अगर:** खांसी "
              "2 हफ़्ते से ज़्यादा हो, बलगम में खून, वज़न घटना या सांस "
              "फूलना (टीबी जाँच PHC में मुफ़्त है)।\n⚠️ सांस तंग या "
              "होंठ नीले → **108**.",
    },
    "loose_motion": {
        "en": "**Loose motions - general care**\n- Most important: "
              "prevent dehydration. Mix one ORS packet in 1 litre "
              "clean water and sip continuously.\n- Eat light food "
              "(rice-curd, banana).\n- Wash hands with soap before "
              "eating.\n\n**See a doctor if:** more than 6 motions a "
              "day, blood in stool, fever, or dehydration signs "
              "(very dry mouth, little urine).\n⚠️ Severe dehydration "
              "in child/elderly → call **108**.",
        "te": "**విరోచనాలు - సాధారణ జాగ్రత్తలు**\n- ముఖ్యం: నిర్జలీకరణ "
              "నివారించండి. ఒక ORS సంచిని 1 లీటరు శుభ్ర నీటిలో కలిపి "
              "కొద్దకొద్దిగా త్రాగండి.\n- తేలికపాటి ఆహారం "
              "(పెరుగన్నం, అరటి).\n- తినే ముందు సబ్బుతో చేతులు "
              "కడగండి.\n\n**డాక్టర్‌ను చూడండి:** రోజుకు 6 కంటే ఎక్కువ, "
              "మలంలో రక్తం, జ్వరం, లేదా నిర్జలీకరణ లక్షణాలు (నోరు "
              "పొడి, తక్కువ మూత్రం).\n⚠️ పిల్లలు/పెద్దలలో తీవ్ర "
              "నిర్జలీకరణ → **108**.",
        "hi": "**दस्त - सामान्य देखभाल**\n- सबसे ज़रूरी: पानी की कमी "
              "रोकें। ORS का पैकेट 1 लीटर साफ़ पानी में मिलाकर "
              "धीरे-धीरे पिएँ।\n- हल्का खाना खाएँ (दही-चावल, केला)।\n- "
              "खाने से पहले साबुन से हाथ धोएँ।\n\n**डॉक्टर से मिलें "
              "अगर दिन में 6 से ज़्यादा दस्त, मल में खून, बुखार, या "
              "पानी की कमी के लक्षण (मुँह सूखना, कम पेशाब)।\n⚠️ बच्चे/"
              "बुज़ुर्ग में तेज़ पानी की कमी → **108**.",
    },
    "vomiting": {
        "en": "**Vomiting - general care**\n- Sip ORS or water slowly "
              "in small sips; do not gulp.\n- Rest the stomach a few "
              "hours, then light food.\n- Avoid oily/spicy food.\n\n"
              "**See a doctor if:** vomiting lasts over 24 hours, "
              "blood in vomit, severe stomach pain, or dehydration "
              "signs.\n⚠️ Non-stop vomiting with blood → call "
              "**108**.",
        "te": "**వాంతులు - సాధారణ జాగ్రత్తలు**\n- ORS లేదా నీరు చిన్న "
              "చిన్న చుక్కలుగా నెమ్మదిగా త్రాగండి.\n- కొన్ని గంటలు "
              "కడుపుకు విశ్రాంతి, తర్వాత తేలికపాటి ఆహారం.\n- ఎక్కువ "
              "నూనె/మసాలా తినకండి.\n\n**డాక్టర్‌ను చూడండి:** వాంతులు "
              "24 గంటలకు పైగా, వాంతుల్లో రక్తం, తీవ్ర కడుపు నొప్పి, "
              "లేదా నిర్జలీకరణ.\n⚠️ ఆగని వాంతులు, రక్తంతో → **108**.",
        "hi": "**उल्टी - सामान्य देखभाल**\n- ORS या पानी छोटे-छोटे "
              "घूँटों मेंधीरे-धीरे पिएँ।\n- पेट को कुछ घंटे आराम दें, "
              "फिर हल्का खाना।\n- तला/मसालेदार खाना न लें।\n\n**डॉक्टर "
              "से मिलें अगर:** उल्टी 24 घंटे से ज़्यादा, उल्टी में "
              "खून, तेज़ पेट दर्द, या पानी की कमी।\n⚠️ लगातार उल्टी, "
              "खून के साथ → **108**.",
    },
    "stomach_pain": {
        "en": "**Stomach pain - general care**\n- Sip warm water; "
              "avoid oily, spicy food.\n- Do NOT take painkillers on "
              "an empty stomach.\n\n**See a doctor if pain is "
              "severe, on the lower right side, with vomiting, "
              "fever, or lasts over a day.\n⚠️ Severe sudden pain "
              "with a hard belly → call **108**.",
        "te": "**కడుపు నొప్పి - సాధారణ జాగ్రత్తలు**\n- వేడి నీరు "
              "త్రాగండి; నూనె, మసాలా ఆహారం మానేయండి.\n- ఖాళీ కడుపుతో "
              "నొప్పి మాత్రలు వేసుకోకండి.\n\n**డాక్టర్‌ను చూడండి:** "
              "నొప్పి తీవ్రంగా, కుడి కింది వైపు, వాంతులు, జ్వరంతో, "
              "లేదా రోజుకు పైగా ఉ

> ⚠️ The response reached the length limit. Reply **continue** to get the rest.
