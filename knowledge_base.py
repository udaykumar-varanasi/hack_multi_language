"""ArogyaMitra knowledge base - English / Telugu / Hindi."""

DISCLAIMER = (
    "⚕️ ArogyaMitra gives general health information only. It does NOT "
    "diagnose or replace a doctor. For any health concern visit your "
    "nearest PHC. Emergency: 108 / 112."
)

EMERGENCY_CONTACTS = {
    "Ambulance": "108",
    "National Emergency": "112",
    "Health Helpline": "104",
    "Women Helpline": "181",
    "Child Helpline": "1098",
}

TE = "te"
HI = "hi"
EN = "en"

# topic -> {lang: answer}
KNOWLEDGE_BASE = {
    # ---------------- basic needs ----------------
    "clean_water": {
        "en": "**Safe drinking water:** Boil water for 10 minutes OR use "
              "chlorine tablets. Store in a closed, clean container. "
              "Unsafe water causes diarrhea, typhoid and jaundice.",
        "te": "**తాగునీరు:** నీటిని 10 నిమిషాలు మరిగించండి లేదా క్లోరిన్ "
              "టాబ్లెట్లు వాడండి. మూసివేసిన శుభ్రమైన పాత్రలో నిల్వ "
              "ఉంచండి. శుభ్రం కాని నీరు విరోచనాలు, టైఫాయిడ్, కామెర్లకు "
              "కారణమవుతుంది.",
        "hi": "**पीने का पानी:** पानी 10 मिनट उबालें या क्लोरीन टैबलेट "
              "डालें। ढके हुए साफ़ बर्तन में रखें। दूषित पानी से दस्त, "
              "टाइफाइड और पीलिया होता है।",
    },
    "hygiene": {
        "en": "**Hygiene:** Wash hands with soap before eating, after "
              "toilet and after touching animals. Bathe daily; keep "
              "nails short. This prevents most stomach and skin "
              "infections.",
        "te": "**పరిశుభ్రత:** తినే ముందు, శౌచం తర్వాత, జంతువులను తాకిన "
              "తర్వాత సబ్బుతో చేతులు కడగండి. రోజూ స్నానం; గోరు చిన్నగా "
              "ఉంచండి. ఇది చాలా కడుపు, చర్మ వ్యాధులను నివారిస్తుంది.",
        "hi": "**सफ़ाई:** खाने से पहले, शौच के बाद, जानवर छूने के बाद साबुन "
              "से हाथ धोएँ। रोज़ नहाएँ; नाख़ून छोटे रखें। इससे ज़्यादातर "
              "पेट और त्वचा रोग रुकते हैं।",
    },
    "nutrition": {
        "en": "**Good nutrition:** Eat a mix of rice/roti, dal, "
              "vegetables, and curd. Pregnant women and children need "
              "extra iron (greens, jaggery) and protein (eggs, dal). "
              "Anganwadi gives free nutritious food.",
        "te": "**మంచి పోషణ:** బియ్యం/రొట్టె, పప్పు, కూరగాయలు, పెరుగు "
              "కలిపి తినండి. గర్భిణీ స్త్రీలు, పిల్లలకు ఎక్కువ ఇనుము "
              "(ఆకుకూరలు, బెల్లం), ప్రోటీన్ (గుడ్లు, పప్పు) కావాలి. "
              "ఆంగన్‌వాడీలో ఉచిత పోషకాహారం లభిస్తుంది.",
        "hi": "**अच्छा पोषण:** चावल/रोटी, दाल, सब्ज़ियाँ, दही साथ-साथ "
              "खाएँ। गर्भवती महिलाओं और बच्चों को ज़्यादा आयरन (हरी "
              "सब्ज़ियाँ, गुड़) और प्रोटीन (अंडे, दाल) चाहिए। आंगनवाड़ी "
              "में मुफ़्त पौष्टिक भोजन मिलता है।",
    },
    "sleep_rest": {
        "en": "**Sleep & rest:** 7-8 hours of sleep daily. Rest at least "
              "1 hour in the afternoon during hard farm work. Lack of "
              "sleep causes headaches, BP and stress.",
        "te": "**నిద్ర, విశ్రాంతి:** రోజుకు 7-8 గంటలు నిద్ర. కఠినమైన "
              "పనుల సమయంలో మధ్యాహ్నం కనీసం 1 గంట విశ్రాంతి. నిద్ర లేమి "
              "వల్ల తలనొప్పి, బీపీ, ఒత్తిడి వస్తాయి.",
        "hi": "**नींद और आराम:** रोज़ 7-8 घंटे सोएँ। कड़ी मेहनत में दोपहर "
              "कम से कम 1 घंटा आराम करें। नींद की कमी से सिरदर्द, बीपी "
              "और तनाव होता है।",
    },
    "first_aid": {
        "en": "**First-aid basics:** Keep a kit with bandage, cotton, "
              "antiseptic (like Dettol), ORS packets and paracetamol. "
              "For cuts: wash with water, press with clean cloth. For "
              "burns: cool water 10 minutes - never apply toothpaste "
              "or ghee.",
        "te": "**ప్రాథమిక చికిత్స:** పట్టీలు, పత్తి, ఆంటిసెప్టిక్, ORS "
              "సంచులు, పారాసిటమాల్ ఉన్న కిట్ ఉంచండి. కట్లకు: నీటితో "
              "కడగండి, శుభ్ర గుడ్డతో నొక్కండి. కాలిన గాయాలకు: 10 నిమిషాలు "
              "చల్ల నీరు - టూత్‌పేస్ట్/నెయ్యి వేయవద్దు.",
        "hi": "**प्राथमिक चिकित्सा:** पट्टी, रुई, एंटीसेप्टिक, ORS पैकेट, "
              "पैरासिटामोल का किट रखें। कटने पर: पानी से धोएँ, साफ़ "
              "कपड़े से दबाएँ। जलने पर: 10 मिनट ठंडा पानी - टूथपेस्ट/घी "
              "न लगाएँ।",
    },
    # ---------------- diseases ----------------
    "fever": {
        "en": "**Fever:** Rest, drink fluids, paracetamol. Danger signs: "
              "over 3 days, rash, severe body pain, vomiting - test for "
              "dengue/typhoid (free at PHC).",
        "te": "**జ్వరం:** విశ్రాంతి, ద్రవాలు, పారాసిటమాల్. ప్రమాద సూచనలు: "
              "3 రోజులకు పైగా, దద్దుర్లు, తీవ్ర నొప్పి, వాంతులు - "
              "డెంగ్యూ/టైఫాయిడ్ పరీక్ష (PHC లో ఉచితం).",
        "hi": "**बुखार:** आराम, तरल, पैरासिटामोल। ख़तरे के संकेत: 3 दिन "
              "से ज़्यादा, दाने, तेज़ दर्द, उल्टी - डेंगू/टाइफाइड जाँच "
              "(PHC में मुफ़्त)।",
    },
    "cough_cold": {
        "en": "**Cough & cold:** Warm fluids, steam, gargling. Over 2 "
              "weeks cough, blood in sputum or weight loss - free TB "
              "test at PHC.",
        "te": "**దగ్గు, జలుబు:** వేడి ద్రవాలు, ఆవిరి, పుక్కిట. 2 వారాలకు "
              "పైగా దగ్గు, కఫంలో రక్తం, బరువు తగ్గడం - PHC లో ఉచిత క్షయ "
              "పరీక్ష.",
        "hi": "**खांसी-जुकाम:** गर्म तरल, भाप, गरारे। 2 हफ़्ते से ज़्यादा "
              "खांसी, बलगम में खून, वज़न घटना - PHC में मुफ़्त टीबी जाँच।",
    },
    "diarrhea": {
        "en": "**Diarrhea (loose motions):** ORS is the life-saver - one "
              "packet in 1 litre water, sip continuously. Zinc tablets "
              "for children. Blood in stool or 6+ motions a day → PHC.",
        "te": "**విరోచనాలు:** ORS ప్రాణరక్షక - 1 లీటరు నీటిలో ఒక సంచి "
              "కలిపి త్రాగండి. పిల్లలకు జింక్ మాత్రలు. మలంలో రక్తం లేదా "
              "6 కంటే ఎక్కువ → PHC.",
        "hi": "**दस्त:** ORS जान बचाता है - 1 लीटर पानी में एक पैकेट, "
              "लगातार पिएँ। बच्चों को ज़िंक गोली। मल में खून या 6+ दस्त "
              "→ PHC.",
    },
    "dengue": {
        "en": "**Dengue:** High fever + severe body pain. Paracetamol "
              "ONLY (never aspirin/ibuprofen). Danger: bleeding, severe "
              "stomach pain, drowsiness → hospital NOW. Prevention: no "
              "stored open water.",
        "te": "**డెంగ్యూ:** ఎక్కువ జ్వరం + తీవ్ర శరీర నొప్పి. పారాసిటమాల్ "
              "మాత్రమే (ఆస్పిరిన్ వద్దు). ప్రమాదం: రక్తస్రావం, తీవ్ర "
              "కడుపు నొప్పి → వెంటనే ఆసుపత్రి. నివారణ: బహిరంగ నీరు నిల్వ "
              "చేయకండి.",
        "hi": "**डेंगू:** तेज़ बुखार + तेज़ शरीर दर्द। केवल पैरासिटामोल "
              "(आस्प्रिन कभी नहीं)। ख़तरा: खून आना, तेज़ पेट दर्द → तुरंत "
              "अस्पताल। बचाव: खुला पानी जमा न करें।",
    },
    "malaria": {
        "en": "**Malaria:** Fever with chills and shivering, comes in "
              "cycles. Blood test at PHC (free). Sleep under mosquito "
              "net. Treated fully with government medicines.",
        "te": "**మలేరియా:** జ్వరంతో వణుకు, కూల్చిపడే శీతం, చక్రాలలో "
              "వస్తుంది. PHC లో ఉచిత రక్త పరీక్ష. పుచ్చకాయ కింద నిద్ర. "
              "ప్రభుత్వ మందులతో పూర్తిగా నయం అవుతుంది.",
        "hi": "**मलेरिया:** बुखार के साथ कंपकंपी, चक्कर में आता-जाता है। "
              "PHC में मुफ़्त रक्त जाँच। मच्छरदानी में सोएँ। सरकारी दवाओं "
              "से पूरा इलाज होता है।",
    },
    "tb": {
        "en": "**Tuberculosis (TB):** Cough over 2 weeks, night sweats, "
              "weight loss. FREE test and FREE full treatment at the "
              "government PHC. Complete the full course - do not stop "
              "in the middle.",
        "te": "**క్షయ (టీబీ):** 2 వారాలకు పైగా దగ్గు, రాత్రి చెమటలు, "
              "బరువు తగ్గడం. ప్రభుత్వ PHC లో ఉచిత పరీక్ష, ఉచిత పూర్తి "
              "చికిత్స. పూర్తి కోర్సు పూర్తి చేయండి - మధ్యలో ఆపవద్దు.",
        "hi": "**टीबी:** 2 हफ़्ते से ज़्यादा खांसी, रात के पसीने, वज़न "
              "घटना। सरकारी PHC में मुफ़्त जाँच और मुफ़्त पूरा इलाज। पूरा "
              "कोर्स पूरा करें - बीच में मत रोकें।",
    },
    "diabetes": {
        "en": "**Diabetes (sugar):** Less sugar, rice and fried food; "
              "more vegetables. Walk 30 min daily. Tablets regularly. "
              "Free test at PHC. Danger: non-healing wounds, blurred "
              "vision.",
        "te": "**షుగర్:** తక్కువ షుగర్, బియ్యం, వేపుళ్లు; ఎక్కువ కూరగాయలు. "
              "రోజు 30 నిమిషాలు నడక. మాత్రలు క్రమం తప్పకుండా. PHC లో "
              "ఉచిత పరీక్ష. నయం కాని గాయాలు, కళ్లు మసక → డాక్టర్.",
        "hi": "**शुगर:** कम शुगर, चावल, तला खाना; ज़्यादा सब्ज़ियाँ। रोज़ 30 "
              "मिनट चलें। गोलियाँ नियमित लें। PHC में मुफ़्त जाँच। ठीक न "
              "होने वाले घाव, धुंधला दिखना → डॉक्टर।",
    },
    "bp": {
        "en": "**Blood pressure (BP):** Less salt, no pickles/packed "
              "snacks, daily walk, no tobacco. Take tablets EVERY day "
              "even when feeling fine. Danger: severe headache, chest "
              "pain → 108.",
        "te": "**బీపీ:** తక్కువ ఉప్పు, ఊరగాయలు/ప్యాకెట్ స్నాక్స్ లేదు, "
              "రోజు నడక, పొగతాగడం లేదు. బాగున్నా మాత్రలు రోజూ. తీవ్ర "
              "తలనొప్పి, ఛాతి నొప్పి → 108.",
        "hi": "**बीपी:** कम नमक, अचार/पैकेट स्नैक्स नहीं, रोज़ चलें, तंबाकू "
              "नहीं। ठीक लगे तब भी गोली रोज़ लें। तेज़ सिरदर्द, सीने में "
              "दर्द → 108.",
    },
    "heart_attack": {
        "en": "**Heart attack signs:** Chest pain/pressure spreading to "
              "left arm or jaw, sweating, breathlessness. This is an "
              "EMERGENCY - call **108** immediately. Chew one aspirin "
              "if available.",
        "te": "**గుండెపోటు లక్షణాలు:** ఛాతి నొప్పి/ఒత్తిడి ఎడమ చేతికి లేదా "
              "దవడకు పాకడం, చెమటలు, ఊపిరి ఆడకపోవడం. ఇది అత్యవసరం - "
              "వెంటనే **108** కు కాల్ చేయండి.",
        "hi": "**हार्ट अटैक के संकेत:** सीने में दर्द/दबाव बाएँ हाथ या "
              "जबड़े तक, पसीना, सांस फूलना। यह EMERGENCY है - तुरंत "
              "**108** पर कॉल करें।",
    },
    "stroke": {
        "en": "**Stroke signs (FAST):** Face drooping, Arm weakness, "
              "Speech difficulty, Time to call **108**. Treatment "
              "within 3 hours can save the brain - go immediately.",
        "te": "**పక్షవాతం లక్షణాలు (FAST):** ముఖం వాలడం, చేయి బలహీనం, "
              "మాట తేడా, వెంటనే **108** కు కాల్. 3 గంటల్లో చికిత్స "
              "మెదడును కాపాడుతుంది - వెంటనే వెళ్లండి.",
        "hi": "**स्ट्रोक के संकेत (FAST):** चेहरा टेढ़ा, हाथ कमज़ोर, बोलने "
              "में दिक्कत, तुरंत **108** पर कॉल। 3 घंटे के अंदर इलाज दिमाग़ "
              "बचा सकता है - तुरंत जाएँ।",
    },
    "snake_bite": {
        "en": "**Snake bite:** Keep calm and still, bitten limb below "
              "heart level. Do NOT cut, suck or tie tightly. Remove "
              "rings/bangles. Go to hospital IMMEDIATELY - call **108**.",
        "te": "**పాము కాటు:** ప్రశాంతంగా, నిశ్చలంగా ఉండండి, కాటుకు గురైన "
              "చేయి/కాలు గుండె కంటే కింద ఉంచండి. కోయవద్దు, పీల్చవద్దు, "
              "గట్టిగా కట్టవద్దు. వెంటనే ఆసుపత్రి - **108**.",
        "hi": "**सांप का काटना:** शांत और स्थिर रहें, काटा हुआ हाथ/पैर "
              "दिल से नीचे रखें। काटें, चूसें या कसकर बाँधें नहीं। तुरंत "
              "अस्पताल - **108**.",
    },
    "dog_bite": {
        "en": "**Dog bite:** Wash with soap and running water for 15 "
              "minutes NOW. Go to the PHC today itself for anti-rabies "
              "vaccine (free) - rabies is 100% fatal but 100% "
              "preventable.",
        "te": "**కుక్క కాటు:** వెంటనే 15 నిమిషాలు సబ్బు నీటితో కడగండి. "
              "ఈరోజే PHC లో ఉచిత రేబీస్ టీకా తీసుకోండి - రేబీస్ 100% "
              "ప్రాణాంతకం కానీ 100% నివారించవచ్చు.",
        "hi": "**कुत्ते का काटना:** तुरंत 15 मिनट साबुन-पानी से धोएँ। आज ही "
              "PHC में मुफ़्त रेबीज़ टीका लें - रेबीज़ 100% जानलेवा है पर "
              "100% रोका जा सकता ह

> ⚠️ The response reached the length limit. Reply **continue** to get the rest.
