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

LANG_EN = "en"
LANG_TE = "te"
LANG_HI = "hi"

# topic -> keyword list (all languages mixed)
TOPICS = {
    "clean_water": ["water", "drinking water", "నీరు", "తాగునీరు", "पानी"],
    "hygiene": ["hygiene", "wash hands", "soap", "పరిశుభ్రత", "చేతులు",
                "सफ़ाई", "हाथ धो"],
    "nutrition": ["nutrition", "diet", "food", "anemia", "పోషణ",
                  "ఆహారం", "రక్తహీనత", "पोषण", "आहार", "खाना"],
    "sleep_rest": ["sleep", "rest", "నిద్ర", "విశ్రాంతి", "नींद", "आराम"],
    "first_aid": ["first aid", "kit", "bandage", "ప్రాథమిక", "పట్టీ",
                  "प्राथमिक", "पट्टी"],
    "fever": ["fever", "జ్వరం", "జ్వర", "बुखार"],
    "cough_cold": ["cough", "cold", "throat", "దగ్గు", "జలుబు",
                   "గొంతు", "खांसी", "जुकाम"],
    "diarrhea": ["loose motion", "diarrhea", "diarrhoea", "విరోచనాలు",
                 "డయేరియా", "दस्त"],
    "vomiting": ["vomit", "వాంతులు", "వాంత", "उल्टी"],
    "stomach_pain": ["stomach", "belly", "dominal", "కడుపు", "पेट"],
    "headache": ["headache", "head pain", "తలనొప్పి", "सिरदर्द"],
    "dengue": ["dengue", "డెంగ్యూ", "డెంగు", "डेंगू"],
    "malaria": ["malaria", "మలేరియా", "मलेरिया"],
    "tb": ["tb", "terculosis", "క్షయ", "టీబీ", "टीबी"],
    "diabetes": ["diabetes", "sugar", "షుగర్", "మధుమేహం", "शुगर"],
    "bp": ["blood pressure", "hypertension", "బీపీ", "बीपी"],
    "heart_attack": ["heart attack", "గుండెపోటు", "గుండె", "हार्ट"],
    "stroke": ["stroke", "paralysis", "పక్షవాతం", "स्ट्रोक", "लकवा"],
    "snake_bite": ["snake", "పాము", "सांप"],
    "dog_bite": ["dog", "rabies", "కుక్క", "रेबीज़", "कुत्ते"],
    "wound": ["wound", "injury", "cut", "గాయం", "ज़ख्म", "जख्म", "चोट"],
    "burn": ["burn", "కాలిన", "మంట", "जला", "झुलस"],
    "acidity": ["acidity", "gas", "heartburn", "యాసిడిటీ", "గ్యాస్",
                "एसिडिटी"],
    "toothache": ["tooth", "teeth", "పళ్ల", "దంత", "दांत"],
    "ear_pain": ["ear", "చెవి", "చెవుల", "कान"],
    "eye": ["eye", "vision", "కళ్లు", "కన్ను", "కళ్ళ", "आंख"],
    "jaundice": ["jaundice", "yellow", "కామెర్లు", "पीलिया"],
    "periods": ["period", "menstrual", "నెలసరి", "माहवारी"],
    "pregnancy": ["pregnan", "antenatal", "గర్భిణీ", "గర్భ", "गर्भ"],
    "child_health": ["child", "baby", "vaccin", "పిల్లల", "టీకా",
                     "बच्चे", "टीका"],
    "stress": ["stress", "anxiety", "depression", "ఒత్తిడి", "तनाव"],
    "allergy": ["allergy", "itching", "rash", "skin", "దద్దుర్లు",
                "దురద", "खुजली"],
}

# topic -> {lang: answer}
KB = {
    "clean_water": {
        "en": "**Safe drinking water:** Boil water 10 minutes or use "
              "chlorine tablets. Store in a closed clean container. "
              "Unsafe water causes diarrhea, typhoid, jaundice.",
        "te": "**తాగునీరు:** నీటిని 10 నిమిషాలు మరిగించండి లేదా క్లోరిన్ "
              "టాబ్లెట్లు వాడండి. మూసిన శుభ్ర పాత్రలో నిల్వ చేయండి. "
              "శుభ్రం కాని నీరు విరోచనాలు, టైఫాయిడ్, కామెర్లకు కారణం.",
        "hi": "**पीने का पानी:** 10 मिनट उबालें या क्लोरीन टैबलेट डालें। "
              "ढके साफ़ बर्तन में रखें। दूषित पानी से दस्त, टाइफाइड, "
              "पीलिया होता है।",
    },
    "hygiene": {
        "en": "**Hygiene:** Wash hands with soap before eating, after "
              "toilet and after animals. Bathe daily, keep nails short. "
              "Prevents most stomach and skin infections.",
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
              "తినండి. గర్భిణీ స్త్రీలు, పిల్లలకు ఎక్కువ ఇనుము (ఆకుకూరలు, "
              "బెల్లం), ప్రోటీన్ (గుడ్లు, పప్పు) కావాలి. ఆంగన్‌వాడీలో "
              "ఉచిత పోషకాహారం.",
        "hi": "**पोषण:** चावल/रोटी + दाल + सब्ज़ियाँ + दही खाएँ। गर्भवती "
              "महिलाओं और बच्चों को आयरन (हरी सब्ज़ी, गुड़) और प्रोटीन "
              "(अंडे, दाल) चाहिए। आंगनवाड़ी में मुफ़्त पौष्टिक भोजन।",
    },
    "sleep_rest": {
        "en": "**Sleep & rest:** 7-8 hours daily. Lack of sleep causes "
              "headache, BP and stress.",
        "te": "**నిద్ర, విశ్రాంతి:** రోజుకు 7-8 గంటలు. నిద్ర లేమి వల్ల "
              "తలనొప్పి, బీపీ, ఒత్తిడి వస్తాయి.",
        "hi": "**नींद और आराम:** रोज़ 7-8 घंटे। नींद की कमी से सिरदर्द, "
              "बीपी, तनाव होता है।",
    },
    "first_aid": {
        "en": "**First-aid kit:** Keep bandage, cotton, antiseptic, ORS "
              "packets, paracetamol. Cuts: wash, press with clean cloth. "
              "Burns: cool water 10 min - never toothpaste/ghee.",
        "te": "**ప్రాథమిక చికిత్స కిట్:** పట్టీలు, పత్తి, ఆంటిసెప్టిక్, "
              "ORS సంచులు, పారాసిటమాల్ ఉంచండి. కట్లకు: కడగండి, శుభ్ర గుడ్డతో "
              "నొక్కండి. కాలిన గాయాలకు: 10 నిమిషాలు చల్ల నీరు - "
              "టూత్‌పేస్ట్/నెయ్యి వద్దు.",
        "hi": "**प्राथमिक चिकित्सा किट:** पट्टी, रुई, एंटीसेप्टिक, ORS, "
              "पैरासिटामोल रखें। कटने पर: धोएँ, साफ़ कपड़े से दबाएँ। जलने "
              "पर: 10 मिनट ठंडा पानी - टूथपेस्ट/घी नहीं।",
    },
    "fever": {
        "en": "**Fever:** Rest, fluids, paracetamol. Danger: over 3 "
              "days, rash, severe body pain, vomiting - dengue/typhoid "
              "test (free at PHC).",
        "te": "**జ్వరం:** విశ్రాంతి, ద్రవాలు, పారాసిటమాల్. ప్రమాదం: 3 "
              "రోజులకు పైగా, దద్దుర్లు, తీవ్ర నొప్పి - డెంగ్యూ/టైఫాయిడ్ "
              "పరీక్ష (PHC లో ఉచితం).",
        "hi": "**बुखार:** आराम, तरल, पैरासिटामोल। ख़तरा: 3 दिन से ज़्यादा, "
              "दाने, तेज़ दर्द - डेंगू/टाइफाइड जाँच (PHC में मुफ़्त)।",
    },
    "cough_cold": {
        "en": "**Cough/cold:** Warm fluids, steam twice a day, salt-water "
              "gargling. Over 2 weeks cough or blood in sputum - free TB "
              "test at PHC.",
        "te": "**దగ్గు/జలుబు:** వేడి ద్రవాలు, ఆవిరి, ఉప్పునీటి పుక్కిట. 2 "
              "వారాలకు పైగా దగ్గు, కఫంలో రక్తం - PHC లో ఉచిత క్షయ పరీక్ష.",
        "hi": "**खांसी/जुकाम:** गर्म तरल, भाप, नमक-पानी के गरारे। 2 हफ़्ते "
              "से ज़्यादा खांसी, बलगम में खून - PHC में मुफ़्त टीबी जाँच।",
    },
    "diarrhea": {
        "en": "**Loose motions:** ORS is the life-saver - 1 packet in 1 "
              "litre water, sip continuously. Zinc for children. Blood "
              "in stool or 6+ motions a day -> PHC.",
        "te": "**విరోచనాలు:** ORS ప్రాణరక్షక - 1 లీటరు నీటిలో ఒక సంచి, "
              "త్రాగుతూ ఉండండి. పిల్లలకు జింక్. మలంలో రక్తం లేదా 6 కంటే "
              "ఎక్కువ -> PHC.",
        "hi": "**दस्त:** ORS जान बचाता है - 1 लीटर पानी में एक पैकेट, "
              "लगातार पिएँ। बच्चों को ज़िंक। मल में खून या 6+ दस्त -> PHC.",
    },
    "vomiting": {
        "en": "**Vomiting:** Sip ORS/water slowly. Avoid oily/spicy "
              "food. Over 24 hours or with blood -> doctor.",
        "te": "**వాంతులు:** ORS/నీరు నెమ్మదిగా త్రాగండి. నూనె/మసాలా "
              "మానేయండి. 24 గంటలకు పైగా లేదా రక్తంతో -> డాక్టర్.",
        "hi": "**उल्टी:** ORS/पानी धीरे-धीरे पिएँ। तला/मसालेदार न लें। 24 "
              "घंटे से ज़्यादा या खून के साथ -> डॉक्टर।",
    },
    "stomach_pain": {
        "en": "**Stomach pain:** Sip warm water, avoid oily/spicy food, "
              "no painkillers on empty stomach. Severe pain, lower right "
              "side, or with vomiting/fever -> doctor.",
        "te": "**కడుపు నొప్పి:** వేడి నీరు త్రాగండి, నూనె/మసాలా మానేయండి, "
              "ఖాళీ కడుపుతో మాత్రలు వద్దు. తీవ్రమైన నొప్పి, కుడి కింది "
              "వైపు, వాంతులు/జ్వరంతో -> డాక్టర్.",
        "hi": "**पेट दर्द:** गर्म पानी पिएँ, तला/मसालेदार न लें, खाली पेट "
              "दर्द निवारक नहीं। तेज़ दर्द, दाईं ओर नीचे, उल्टी/बुखार के "
              "साथ -> डॉक्टर।",
    },
    "headache": {
        "en": "**Headache:** Rest in a quiet dark room, drink water, wet "
              "cloth on forehead. Over 2-3 days -> doctor. ⚠️ Sudden "
              "worst-ever headache -> call 108.",
        "te": "**తలనొప్పి:** నిశ్శబ్ద గదిలో విశ్రాంతి, నీరు త్రాగండి, నుదుటిపై "
              "తడి గుడ్డ. 2-3 రోజులకు పైగా -> డాక్టర్. ⚠️ హఠాత్ తీవ్ర "
              "నొప్పి -> 108.",
        "hi": "**सिरदर्द:** शांत कमरे में आराम, पानी पिएँ, माथे पर गीला "
              "कपड़ा। 2-3 दिन से ज़्यादा -> डॉक्टर। ⚠️ अचानक तेज़ दर्द -> "
              "108.",
    },
    "dengue": {
        "en": "**Dengue:** High fever + severe body pain. Paracetamol "
              "ONLY (never aspirin/ibuprofen). Danger: bleeding, severe "
              "stomach pain, drowsiness -> hospital NOW. Prevention: no "
              "stored open water.",
        "te": "**డెంగ్యూ:** ఎక్కువ జ్వరం + తీవ్ర శరీర నొప్పి. పారాసిటమాల్ "
              "మాత్రమే (ఆస్పిరిన్ వద్దు). ప్రమాదం: రక్తస్రావం, తీవ్ర కడుపు "
              "నొప్పి -> వెంటనే ఆసుపత్రి. నివారణ: బహిరంగ నీరు నిల్వ "
              "చేయకండి.",
        "hi": "**डेंगू:** तेज़ बुखार + तेज़ शरीर दर्द। केवल पैरासिटामोल "
              "(आस्प्रिन कभी नहीं)। ख़तरा: खून आना, तेज़ पेट दर्द -> तुरंत "
              "अस्पताल। बचाव: खुला पानी जमा न करें।",
    },
    "malaria": {
        "en": "**Malaria:** Fever with chills/shivering in cycles. Free "
              "blood test at PHC. Sleep under mosquito net. Fully "
              "curable with government medicines.",
        "te": "**మలేరియా:** జ్వరంతో వణుకు, చక్రాలలో వస్తుంది. PHC లో ఉచిత "
              "రక్త పరీక్ష. పుచ్చకాయ కింద నిద్ర. ప్రభుత్వ మందులతో పూర్తిగా "
              "నయం.",
        "hi": "**मलेरिया:** बुखार के साथ कंपकंपी, चक्कर में आता-जाता है। "
              "PHC में मुफ़्त रक्त जाँच। मच्छरदानी में सोएँ। सरकारी दवाओं "
              "से पूरा इलाज।",
    },
    "tb": {
        "en": "**TB:** Cough over 2 weeks, night sweats, weight loss. "
              "FREE test and FREE full treatment at government PHC. "
              "Complete the full course.",
        "te": "**క్షయ (టీబీ):** 2 వారాలకు పైగా దగ్గు, రాత్రి చెమటలు, బరువు "
              "తగ్గడం. ప్రభుత్వ PHC లో ఉచిత పరీక్ష, ఉచిత పూర్తి చికిత్స. "
              "పూర్తి కోర్సు చేయండి.",
        "hi": "**टीबी:** 2 हफ़्ते से ज़्यादा खांसी, रात के पसीने, वज़न "
              "घटना। सरकारी PHC में मुफ़्त जाँच और मुफ़्त पूरा इलाज। पूरा "
              "कोर्स करें।",
    },
    "diabetes": {
        "en": "**Diabetes:** Less sugar/rice/fried food, more vegetables. "
              "Walk 30 min daily. Tablets regularly. Free test at PHC. "
              "Danger: non-healing wounds, blurred vision.",
        "te": "**షుగర్:** తక్కువ షుగర్/బియ్యం/వేపుళ్లు, ఎక్కువ కూరగాయలు. "
              "రోజు 30 నిమిషాలు నడక. మాత్రలు క్రమం తప్పకుండా. PHC లో ఉచిత "
              "పరీక్ష. నయం కాని గాయాలు, కళ్లు మసక -> డాక్టర్.",
        "hi": "**शुगर:** कम शुगर/चावल/तला खाना, ज़्यादा सब्ज़ियाँ। रोज़ 30 "
              "मिनट चलें। गोलियाँ नियमित। PHC में मुफ़्त जाँच। ठीक न होने "
              "वाले घाव, धुंधला दिखना -> डॉक्टर।",
    },
    "bp": {
        "en": "**BP:** Less salt (under 1 tsp/day), daily walk, no "
              "tobacco. Take tablets EVERY day even when fine. Danger: "
              "severe headache, chest pain -> 108.",
        "te": "**బీపీ:** తక్కువ ఉప్పు (రోజుకు 1 ట

> ⚠️ The response reached the length limit. Reply **continue** to get the rest.
