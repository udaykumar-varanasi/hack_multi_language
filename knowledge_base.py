"""ArogyaMitra knowledge base - basic needs + diseases (EN/TE/HI)."""

DISCLAIMER = (
    "⚕️ ArogyaMitra gives general health information only. It does NOT "
    "diagnose or replace a doctor. For any health concern visit your "
    " PHC. Emergency: 108 / 112."
)

EMERGENCY_CONTACTS = {
    "Ambulance": "108",
    "National Emergency": "112",
    "Health Helpline": "104",
}

TOPICS = {
    "clean_water": ["water", "నీరు", "తాగు", "पानी"],
    "hygiene": ["hygiene", "wash hands", "soap", "పరిశుభ్రత", "सफ़ाई", "हाथ धो"],
    "nutrition": ["nutrition", "diet", "food", "పోషణ", "ఆహారం", "पोषण", "खाना"],
    "sleep_rest": ["sleep", "rest", "నిద్ర", "విశ్రాంతి", "नींद", "आराम"],
    "first_aid": ["first aid", "kit", "bandage", "ప్రాథమిక", "పట్టీ", "प्रमिक"],
    "sanitation": ["toilet", "garbage", "శౌచం", "చెత్త", "शौच", "कचरा"],
    "fever": ["fever", "జ్వరం", "జ్వర", "बुखार"],
    "cold_cough": ["cough", "cold", "throat", "దగ్గు", "జలుబు", "గొంతు", "खांसी", "जुकाम"],
    "headache": ["headache", "head pain", "తలనొప్పి", "सिरदर्द"],
    "stomach_pain": ["stomach", "belly", "abdominal", "కడుపు", "पेट"],
    "chest_pain": ["chest pain", "heart pain", "heart attack", "ఛాతి", "గుండె", "सीने में दर्द", "हार्ट"],
    "fracture": ["fracture", "broken bone", "bone", "ఎముక", "విరుపు", "हड्डी", "टूट"],
    "bleeding": ["bleeding", "blood", "రక్తస్రావం", "రక్తం", "खून", "रक्त"],
    "diarrhea": ["loose motion", "diarrhea", "విరోచనాలు", "दस्त"],
    "vomiting": ["vomit", "వాంతులు", "వాంత", "उल्टी"],
    "dengue": ["dengue", "డెంగ్యూ", "డెంగు", "डेंगू"],
    "malaria": ["malaria", "మలేరియా", "मलेरिया"],
    "tb": ["tb", "క్షయ", "టీబీ", "टीबी"],
    "diabetes": ["diabetes", "sugar", "షుగర్", "మధుమేహం", "शुगर"],
    "bp": ["blood pressure", "బీపీ", "बीपी"],
    "snake_bite": ["snake", "పాము", "सांप"],
    "dog_bite": ["dog bite", "dog", "rabies", "కుక్క", "कुत्ते"],
    "burn": ["burn", "కాలిన", "మంట", "जला", "झुलस"],
    "wound": ["wound", "injury", "గాయం", "ज़ख्म", "जख्म", "चोट"],
    "pregnancy": ["pregnan", "గర్భిణీ", "గర్భ", "गर्भ"],
    "jaundice": ["jaundice", "yellow", "కామెర్లు", "पीलिया"],
}

KB = {
    "clean_water": {
        "en": "**Safe water:** Boil 10 min or use chlorine tablets; store covered. Unsafe water causes diarrhea, typhoid, jaundice.",
        "te": "**తాగునీరు:** 10 నిమిషాలు మరిగించండి లేదా క్లోరిన్ టాబ్లెట్లు వాడండి; మూసిన పాత్రలో నిల్వ.",
        "hi": "**पीने का पानी:** 10 मिनट उबालें या क्लोरीन टैबलेट डालें; ढककर रखें।",
    },
    "hygiene": {
        "en": "**Hygiene:** Wash hands with soap before eating and after toilet. Bathe daily, trim nails. Prevents stomach and skin infections.",
        "te": "**పరిశుభ్రత:** తినే ముందు, శౌచం తర్వాత సబ్బుతో చేతులు కడగండి. రోజూ స్నానం.",
        "hi": "**सफ़ाई:** खाने से पहले, शौच के बाद साबुन से हाथ धोएँ। रोज़ नहाएँ।",
    },
    "nutrition": {
        "en": "**Nutrition:** Rice/roti + dal + vegetables + curd. Pregnant women and children need iron (greens) and protein (eggs, dal). Free food at Anganwadi.",
        "te": "**పోషణ:** బియ్యం + పప్పు + కూరగాయలు + పెరుగు. గర్భిణీ స్త్రీలు, పిల్లలకు ఆకుకూరలు, గుడ్లు కావాలి. ఆంగన్‌వాడీలో ఉచిత ఆహారం.",
        "hi": "**पोषण:** चावल + दाल + सब्ज़ी + दही। गर्भवती महिलाओं और बच्चों को हरी सब्ज़ी, अंडे चाहिए।",
    },
    "sleep_rest": {
        "en": "**Sleep & rest:** 7-8 hours daily. Lack of sleep causes headache, BP and stress.",
        "te": "**నిద్ర:** రోజుకు 7-8 గంటలు. నిద్ర లేమి వల్ల తలనొప్పి, బీపీ, ఒత్తిడి.",
        "hi": "**नींद:** रोज़ 7-8 घंटे। कम नींद से सिरदर्द, बीपी, तनाव।",
    },
    "first_aid": {
        "en": "**First aid:** Keep bandage, cotton, antiseptic, ORS, paracetamol. Cuts: wash and press with clean cloth. Burns: cool water 10 min - never toothpaste/ghee.",
        "te": "**ప్రాథమిక చికిత్స:** పట్టీలు, పత్తి, ఆంటిసెప్టిక్, ORS ఉంచండి. కట్లకు: కడిగి నొక్కండి. కాలినవి: చల్ల నీరు 10 నిమిషాలు.",
        "hi": "**प्राथमिक चिकित्सा:** पट्टी, रुई, एंटीसेप्टिक, ORS रखें। कटने पर धोकर दबाएँ। जलने पर 10 मिनट ठंडा पानी।",
    },
    "sanitation": {
        "en": "**Sanitation:** Use the toilet, never open fields near water. Prevents diarrhea, cholera, worms.",
        "te": "**పారిశుధ్యం:** శౌచాలయం వాడండి, నీటి దగ్గర బహిరంగంగా చేయవద్దు.",
        "hi": "**स्वच्छता:** शौचालय का उपयोग करें, पानी के पास खुले में न जाएँ।",
    },
    "fever": {
        "en": "**Fever:** Rest, drink fluids, paracetamol. Danger: over 3 days, rash, severe body pain - dengue/typhoid test (free at PHC).",
        "te": "**జ్వరం:** విశ్రాంతి, ద్రవాలు, పారాసిటమాల్. ప్రమాదం: 3 రోజులకు పైగా, దద్దుర్లు - PHC లో ఉచిత పరీక్ష.",
        "hi": "**बुखार:** आराम, तरल, पैरासिटामोल। ख़तरा: 3 दिन से ज़्यादा, दाने - PHC में मुफ़्त जाँच।",
    },
    "cold_cough": {
        "en": "**Cold & cough:** Warm fluids, steam twice a day, salt-water gargling. Over 2 weeks or blood in sputum - free TB test at PHC.",
        "te": "**దగ్గు, జలుబు:** వేడి ద్రవాలు, ఆవిరి, ఉప్పునీటి పుక్కిట. 2 వారాలకు పైగా - PHC లో ఉచిత క్షయ పరీక్ష.",
        "hi": "**खांसी-जुकाम:** गर्म तरल, भाप, गरारे। 2 हफ़्ते से ज़्यादा - PHC में मुफ़्त टीबी जाँच।",
    },
    "headache": {
        "en": "**Headache:** Rest in a quiet dark room, drink water, wet cloth on forehead. Over 2-3 days - doctor. Sudden worst-ever headache - call 108.",
        "te": "**తలనొప్పి:** నిశ్శబ్ద గదిలో విశ్రాంతి, నీరు, నుదుటిపై తడి గుడ్డ. హఠాత్ తీవ్ర నొప్పి - 108.",
        "hi": "**सिरदर्द:** शांत कमरे में आराम, पानी, माथे पर गीला कपड़ा। अचानक तेज़ दर्द - 108।",
    },
    "stomach_pain": {
        "en": "**Stomach pain:** Sip warm water, avoid oily/spicy food, no painkillers on empty stomach. Severe pain or with vomiting/fever - doctor.",
        "te": "**కడుపు నొప్పి:** వేడి నీరు, నూనె/మసాలా మానేయండి. తీవ్రమైతే డాక్టర్.",
        "hi": "**पेट दर्द:** गर्म पानी पिएँ, तला/मसालेदार न लें। तेज़ दर्द - डॉक्टर।",
    },
    "chest_pain": {
        "en": "**Chest/heart pain - EMERGENCY:** Call **108** NOW. Sit the person down, loosen clothes, keep calm. Do not walk or drive yourself.",
        "te": "**ఛాతి నొప్పి - అత్యవసరం:** వెంటనే **108** కు కాల్ చేయండి. కూర్చోబెట్టండి, ప్రశాంతంగా ఉంచండి. నడవవద్దు.",
        "hi": "**सीने/दिल का दर्द - EMERGENCY:** तुरंत **108** पर कॉल करें। बिठाएँ, शांत रखें। चलें नहीं।",
    },
    "fracture": {
        "en": "**Fracture (broken bone):** Do NOT move the limb or try to set it. Immobilize with a splint (stick + cloth). Go to hospital / call 108.",
        "te": "**ఎముక విరుపు:** అవయవం కదలించవద్దు, బలవంతంగా సరిచేయవద్దు. కర్ర + గుడ్డతో కట్టండి. ఆసుపత్రి / 108.",
        "hi": "**हड्डी टूटना:** अंग हिलाएँ नहीं, सीधा करने की कोशिश न करें। छड़ी + कपड़े से स्थिर करें। अस्पताल / 108।",
    },
    "bleeding": {
        "en": "**Bleeding:** Press firmly with a clean cloth for 10 minutes, raise the limb. Heavy bleeding - call **108**.",
        "te": "**రక్తస్రావం:** శుభ్ర గుడ్డతో 10 నిమిషాలు గట్టిగా నొక్కండి, ఎత్తుగా ఉంచండి. ఎక్కువ రక్తం - **108**.",
        "hi": "**खून बहना:** साफ़ कपड़े से 10 मिनट दबाएँ, अंग ऊपर उठाएँ। ज़्यादा खून - **108**।",
    },
    "diarrhea": {
        "en": "**Loose motions:** ORS saves lives - 1 packet in 1 litre water, sip continuously. Blood in stool or 6+ motions a day - go to PHC.",
        "te": "**విరోచనాలు:** ORS ప్రాణరక్షక - 1 లీటరు నీటిలో 1 సంచి, త్రాగుతూ ఉండండి. మలంలో రక్తం - PHC.",
        "hi": "**दस्त:** ORS जान बचाता है - 1 लीटर पानी में 1 पैकेट, लगातार पिएँ। मल में खून - PHC।",
    },
    "vomiting": {
        "en": "**Vomiting:** Sip ORS/water slowly. Avoid oily food. Over 24 hours or with blood - doctor.",
        "te": "**వాంతులు:** ORS/నీరు నెమ్మదిగా త్రాగండి. నూనె ఆహారం మానేయండి. 24 గంటలకు పైగా - డాక్టర్.",
        "hi": "**उल्टी:** ORS/पानी धीरे-धीरे पिएँ। तला खाना न लें। 24 घंटे से ज़्यादा - डॉक्टर।",
    },
    "dengue": {
        "en": "**Dengue:** High fever + severe body pain. Paracetamol ONLY (never aspirin). Bleeding or severe stomach pain - hospital NOW. Don't store open water.",
        "te": "**డెంగ్యూ:** ఎక్కువ జ్వరం + తీవ్ర నొప్పి. పారాసిటమాల్ మాత్రమే (ఆస్పిరిన్ వద్దు). రక్తస్రావం - వెంటనే ఆసుపత్రి.",
        "hi": "**डेंगू:** तेज़ बुखार + तेज़ दर्द। केवल पैरासिटामोल (आस्प्रिन कभी नहीं)। खून आना - तुरंत अस्पताल।",
    },
    "malaria": {
        "en": "**Malaria:** Fever with chills/shivering in cycles. Free blood test at PHC. Sleep under mosquito net. Fully curable.",
        "te": "**మలేరియా:** జ్వరంతో వణుకు. PHC లో ఉచిత రక్త పరీక్ష. పుచ్చకాయ కింద నిద్ర.",
        "hi": "**मलेरिया:** बुखार के साथ कंपकंपी। PHC में मुफ़्त रक्त जाँच। मच्छरदानी में सोएँ।",
    },
    "tb": {
        "en": "**TB:** Cough over 2 weeks, night sweats, weight loss. FREE test and treatment at government PHC. Complete the full course.",
        "te": "**క్షయ:** 2 వారాలకు పైగా దగ్గు, రాత్రి చెమటలు. PHC లో ఉచిత పరీక్ష, చికిత్స. పూర్తి కోర్సు చేయండి.",
        "hi": "**टीबी:** 2 हफ़्ते से ज़्यादा खांसी, रात के पसीने। PHC में मुफ़्त जाँच, इलाज। पूरा कोर्स करें।",
    },
    "diabetes": {
        "en": "**Sugar (diabetes):** Less sugar/rice/fried food, more vegetables. Walk 30 min daily. Tablets regularly. Free test at PHC.",
        "te": "**షుగర్:** తక్కువ తీయని/బియ్యం/వేపుళ్లు, ఎక్కువ కూరగాయలు. రోజు 30 నిమిషాలు నడక. మాత్రలు క్రమం తప్పకుండా.",
        "hi": "**शुगर:** कम मीठा/चावल/तला खाना, ज़्यादा सब्ज़ी। रोज़ 30 मिनट चलें। गोलियाँ नियमित लें।",
    },
    "bp": {
        "en": "**BP:** Less salt, daily walk, no tobacco. Take tablets EVERY day even when feeling fine. Severe headache or chest pain - call 108.",
        "te": "**బీపీ:** తక్కువ ఉప్పు, రోజు నడక, పొగతాగడం వద్దు. బాగున్నా మాత్రలు రోజూ. తీవ్ర తలనొప్పి - 108.",
        "hi": "**बीपी:** कम नमक, रोज़ चलें, तंबाकू नहीं। ठीक लगे तब भी गोली रोज़। तेज़ सिरदर्द - 108।",
    },
    "snake_bite": {
        "en": "**Snake bite - EMERGENCY:** Keep calm and still, limb below heart. Do NOT cut, suck or tie tightly. Call **108** immediately.",
        "te": "**పాము కాటు - అత్యవసరం:** ప్రశాంతంగా ఉండండి, అవయవం కిందకు. కోయవద్దు, గట్టిగా కట్టవద్దు. వెంటనే **108**.",
        "hi": "**सांप काटना - EMERGENCY:** शांत रहें, अंग नीचे रखें। काटें/बाँधें नहीं। तुरंत **108**।",
    },
    "dog_bite": {
        "en": "**Dog bite:** Wash with soap and running water 15 minutes NOW. Go to PHC today for free anti-rabies vaccine - do not delay.",
        "te": "**కుక్క కాటు:** వెంటనే 15 నిమిషాలు సబ్బు నీటితో కడగండి. ఈరోజే PHC లో ఉచిత రేబీస్ టీకా.",
        "hi": "**कुत्ते काटना:** तुरंत 15 मिनट साबुन-पानी से धोएँ। आज ही PHC में मुफ़्त रेबीज़ टीका।",
    },
    "burn": {
        "en": "**Burns:** Cool water 10 minutes. Never apply toothpaste, ghee or ice. Cover with clean dry cloth. Big blisters - PHC.",
        "te": "**కాలిన గాయాలు:** 10 నిమిషాలు చల్ల నీరు. టూత్‌పేస్ట్/నెయ్యి/మంచు వేయవద్దు. శుభ్ర గుడ్డతో కప్పండి.",
        "hi": "**जलना:** 10 मिनट ठंडा पानी। टूथपेस्ट/घी/बर्फ नहीं। साफ़ सूखा कपड़ा बाँधें।",
    },
    "wound": {
        "en": "**Wound/injury:** Wash with clean water, press with clean cloth to stop bleeding, cover with bandage. Deep or dirty wound - PHC.",
        "te": "**గాయం:** శుభ్ర నీటితో కడగండి, గుడ్డతో నొక్కండి, పట్టీ కట్టండి. లోతైన గాయం - PHC.",
        "hi": "**घाव:** साफ़ पानी से धोएँ, कपड़े से दबाएँ, पट्टी बाँधें। गहरा घाव - PHC।",
    },
    "pregnancy": {
        "en": "**Pregnancy:** Monthly ANC checkup at PHC (free), iron tablets daily, 2 tetanus injections, extra food and rest. Bleeding or severe pain - 108.",
        "te": "**గర్భిణీ:** ప్రతి నెల PHC తనిఖీ (ఉచితం), ఇనుము మాత్రలు రోజూ, 2 టీకాలు, ఎక్కువ ఆహారం. రక్తస్రావం - 108.",
        "hi": "**गर्भावस्था:** हर महीने PHC जाँच (मुफ़्त), आयरन गोली रोज़, 2 टीके, ज़्यादा खाना। खून आना - 108।",
    },
    "jaundice": {
        "en": "**Jaundice (yellow eyes/skin):** Rest, plenty of fluids, boiled water only. No alcohol, no oily food. Free test at PHC.",
        "te": "**కామెర్లు:** విశ్రాంతి, ఎక్కువ ద్

> ⚠️ The response reached the length limit. Reply **continue** to get the rest.
