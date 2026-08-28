"""
ArogyaMitra knowledge base - symptoms, OTC guidance, emergency contacts.
25 topics with English, Telugu, Hindi and transliterated keywords.
"""

DISCLAIMER = (
    "ArogyaMitra shares general health information for awareness only. "
    "It is NOT a doctor and does not diagnose or prescribe. Always confirm "
    "with a doctor, PHC, ASHA worker, or pharmacist before taking any medicine."
)

EMERGENCY_CONTACTS = {
    "Ambulance": "108",
    "National Emergency": "112",
    "Health Helpline": "104",
    "Tele-MANAS Mental Health": "14416",
    "KIRAN Helpline": "1800-599-0019",
    "Poison Information": "1800-116-117",
    "Women Helpline": "1091",
    "Child Helpline": "1098",
}

SYSTEM_PROMPT = (
    "You are ArogyaMitra, a friendly rural health guide for villages in Andhra "
    "Pradesh, India. Follow these rules strictly: "
    "1) Give simple general health information only - never diagnose. "
    "2) You MAY mention commonly used over-the-counter options (like paracetamol "
    "for fever, ORS for loose motions) with standard package dosing for ADULTS, "
    "plus clear cautions. "
    "3) Always advise confirming with a doctor, PHC, ASHA worker, or pharmacist. "
    "4) Always list when to see a doctor (red flags, duration). "
    "5) Reply in the SAME language the user used (Telugu, Hindi, or English), "
    "in short simple sentences with bullet points. "
    "6) Keep answers under 200 words. "
    "7) For emergencies, first say to call 108 or 112 immediately, then give "
    "basic first-aid steps only. "
    "8) Never suggest prescription-only medicines (antibiotics, steroids) and "
    "never give doses for babies under 1 year - send them to a doctor."
)

URGENT_KEYWORDS = [
    "chest pain", "not breathing", "breathless", "unconscious", "seizure",
    "convulsion", "snake", "poison", "suicide", "bleeding heavily",
    "heavy bleeding", "accident", "stroke", "slurred", "overdose",
    "severe burn", "drowning", "dog bite", "fits", "heart attack",
    # Telugu
    "ఛాతీ", "పాము", "విషం", "మయకం", "కుట్టింది",
    # transliterations
    "chhati", "chaati", "pamu", "saap", "saanp", "nokkindi", "hrudayam",
]

FALLBACK_ANSWER = (
    "I am not fully sure about that, so I will not guess. "
    "For any health concern, visit the nearest PHC or call 104. "
    "If this feels urgent, call 108 or 112 now. "
    "You can ask me about: fever, dengue, cough and cold, loose motions, "
    "vomiting, headache, body pain, stomach pain, acidity, constipation, "
    "diabetes, blood pressure, TB, asthma, allergy, skin problems, eye or "
    "ear pain, tooth pain, joint pain, urinary problems, period problems, "
    "anaemia, worm infection, dog bite, snake bite, burns, cuts, heat "
    "stroke, child health, pregnancy care, elderly care, stress, or nutrition. "
    "This is general information only - please consult a doctor for diagnosis "
    "and treatment."
)

KB_ENTRIES = [
    # ---------------- FEVER & INFECTIONS ----------------
    {
        "topic": "fever",
        "keywords": ["fever", "jwaram", "jvaram", "bukhar", "temperature",
                     "shivering", "100 f", "102", "జ్వరం", "బుఖార్", "बुखार"],
        "answer": (
            "**Fever - what helps**\n"
            "- Rest and drink plenty of fluids (water, buttermilk, soups).\n"
            "- A lukewarm sponge bath can bring temperature down.\n"
            "- **Common tablet for adults:** Paracetamol 500 mg - 1 tablet every "
            "6 hours after food, maximum 4 tablets in 24 hours.\n"
            "- Do NOT take ibuprofen or aspirin until dengue is ruled out "
            "(common in our district).\n\n"
            "**See a doctor (PHC or call 104) if:** fever lasts more than 3 days, "
            "goes above 103 F, or comes with rash, severe body pain, or very low "
            "urine. Babies, elderly, and pregnant women should see a doctor on "
            "day 1.\n\n"
            "This is general information, not a prescription."
        ),
    },
    {
        "topic": "dengue",
        "keywords": ["dengue", "dengu", "platelet", "mosquito fever", "డెంగ్యూ",
                     "దోమ", "डेंगू", "मच्छर"],
        "answer": (
            "**Dengue - warning signs and care**\n"
            "- High fever with severe body/joint pain, pain behind the eyes, "
            "or rash needs a **dengue test at the PHC on day 1-2** (free).\n"
            "- Do NOT take ibuprofen, aspirin, or combiflam - only paracetamol.\n"
            "- Drink lots of fluids: ORS, coconut water, soups.\n"
            "- Rest fully. No mosquitoes near the patient (use a net).\n\n"
            "**Go to hospital IMMEDIATELY if:** bleeding gums or nose, black "
            "stools, red spots on skin, severe stomach pain, very low urine, "
            "or drowsiness. Platelet counts can fall fast from day 4.\n\n"
            "**Prevention:** empty water containers weekly, sleep under a net."
        ),
    },
    {
        "topic": "malaria",
        "keywords": ["malaria", "chills", "periodic fever", "మలేరియా", "मलेरिया"],
        "answer": (
            "**Malaria - what to do**\n"
            "- Fever with severe shivering/chills that comes and goes, with "
            "sweating - get a **free blood test at the PHC**.\n"
            "- Until tested: paracetamol for fever, plenty of fluids, rest.\n"
            "- Malaria needs prescription medicines from the PHC - do not "
            "self-medicate.\n\n"
            "**Prevention:** sleep under mosquito nets, use repellents, "
            "report any fever lasting 2+ days for free testing.\n\n"
            "Treated early, malaria is completely curable - do not delay testing."
        ),
    },
    {
        "topic": "tuberculosis",
        "keywords": ["tb", "tuberculosis", "kshayam", "blood in cough",
                     "cough 2 weeks", "cough 3 weeks", "క్షయ", "టీబీ", "टीबी"],
        "answer": (
            "**Cough lasting more than 2 weeks - get checked for TB**\n"
            "- TB testing and treatment are **completely FREE at government "
            "PHCs** under the NTEP programme.\n"
            "- Warning signs: cough 2+ weeks, blood in sputum, evening fever, "
            "night sweats, weight loss.\n"
            "- TB is curable - treatment takes 6-9 months and must be "
            "completed even after feeling better.\n"
            "- Cover your mouth; TB spreads through cough droplets.\n\n"
            "Go to the PHC this week for a free sputum test. Do not wait."
        ),
    },
    # ---------------- COUGH, COLD, THROAT ----------------
    {
        "topic": "cough and cold",
        "keywords": ["cough", "cold", "sneeze", "throat", "daggu", "jalubu",
                     "khansi", "zukam", "jukam", "దగ్గు", "జలుబు", "గొంతు",
                     "खांसी", "जुकाम"],
        "answer": (
            "**Cough and cold - what helps**\n"
            "- Warm fluids: warm water, soups, pepper-turmeric kashayam.\n"
            "- Steam inhalation 2-3 times a day for blocked nose.\n"
            "- Salt-water gargle for throat pain. Honey soothes cough "
            "(not for babies under 1 year).\n"
            "- **If fever or body pain is troublesome:** Paracetamol 500 mg - "
            "1 tablet every 6 hours after food (max 4/day).\n\n"
            "**See a doctor if:** cough lasts more than 2 weeks, blood in "
            "sputum, breathing trouble, wheezing, or weight loss (get TB "
            "checked at PHC).\n\n"
            "This is general information, not a prescription."
        ),
    },
    {
        "topic": "asthma",
        "keywords": ["asthma", "wheezing", "wheeze", "breathing problem",
                     "shwasam", "aaspata", "ఆయాసం", "ఉబ్బసం", "दमा", "सांस"],
        "answer": (
            "**Wheezing / breathing difficulty**\n"
            "- Avoid dust, smoke, and strong smells; use a cloth over the "
            "nose while working in fields.\n"
            "- Sit upright, lean slightly forward during an attack.\n"
            "- If a doctor has given an **inhaler (like salbutamol)**, use it "
            "as prescribed - inhalers are safe and not addictive.\n"
            "- Warm steam can ease mild tightness.\n\n"
            "**EMERGENCY - call 108 if:** lips or fingers turn blue, cannot "
            "speak full sentences, or the inhaler is not helping. Do not wait."
        ),
    },
    # ---------------- DIGESTIVE ----------------
    {
        "topic": "loose motions",
        "keywords": ["loose motion", "loose motions", "diarrhea", "diarrhoea",
                     "stool", "motions", "atlu", "pichi atlu", "dast", "patla",
                     "అతిడు", "అతిసారం", "డయేరియా", "దస్తా", "दस्त"],
        "answer": (
            "**Loose motions - what helps**\n"
            "- **ORS is the most important thing.** Mix 1 sachet in 1 litre "
            "clean water and sip continuously. Adults: 2-3 litres a day.\n"
            "- Homemade: 1 litre water + 6 tsp sugar + half tsp salt.\n"
            "- Eat bananas, rice, curd rice, khichdi. Avoid oily food and milk.\n"
            "- **Tablet:** Zinc is helpful if advised. Do NOT take loperamide "
            "(Imodium) if you have fever or blood in stool.\n\n"
            "**See a doctor if:** motions more than 6 a day, blood or mucus in "
            "stool, fever, or signs of dehydration (very low urine, dizziness, "
            "dry tongue). Children and elderly dehydrate fast - go to PHC early."
        ),
    },
    {
        "topic": "vomiting",
        "keywords": ["vomit", "vomiting", "nausea", "throw up", "kakulu",
                     "vomilu", "anti", "ulti", "వాంతులు", "వాక్కు", "उल्टी"],
        "answer": (
            "**Vomiting - what helps**\n"
            "- Sip ORS or clean water slowly, small sips every 10 minutes.\n"
            "- Rest the stomach for 1-2 hours, then try banana or rice.\n"
            "- Ginger water or lemon water with a pinch of salt can help.\n"
            "- Avoid solid oily food until it settles.\n\n"
            "**See a doctor if:** vomiting more than 6 hours, blood in vomit, "
            "severe stomach pain, signs of dehydration, or if it follows a head "
            "injury. Pregnant women with severe vomiting should visit the PHC."
        ),
    },
    {
        "topic": "acidity",
        "keywords": ["acidity", "acid reflux", "heartburn", "gas", "bloating",
                     "gastric", "amlapitta", "edupu", "ఎదుపు", "గ్యాస్",
                     "एसिडिटी", "गैस"],
        "answer": (
            "**Acidity / gas - what helps**\n"
            "- Eat smaller meals on time; do not skip breakfast.\n"
            "- Avoid very spicy, oily food, and excess tea/coffee.\n"
            "- Do not lie down for 2 hours after eating.\n"
            "- **Tablet/syrup:** an antacid (gelusil/digene type) after meals, "
            "as per the packet. Add 30 minutes before breakfast as per packet.\n\n"
            "**See a doctor if:** pain wakes you at night, vomiting blood, "
            "black stools, weight loss, or pain swallowing - these need a "
            "proper check-up at the PHC."
        ),
    },
    {
        "topic": "constipation",
        "keywords": ["constipation", "constipated", "mala baddha", "motion not",
                     "kabz", "kabj", "మలబద్ధకం", "कब्ज"],
        "answer": (
            "**Constipation - what helps**\n"
            "- Drink 8-10 glasses of water daily.\n"
            "- Eat more fibre: vegetables, fruits (papaya is excellent), "
            "whole grains, and soaked raisins at night.\n"
            "- Walk 20-30 minutes daily; go to the toilet at the same time "
            "each morning.\n"
            "- **If needed:** an isabgol (psyllium) spoon in warm water at "
            "night, as per the packet. Avoid regular laxative tablets.\n\n"
            "**See a doctor if:** no motion for 4+ days, blood in stool, "
            "severe pain, vomiting, or sudden weight loss."
        ),
    },
    {
        "topic": "stomach pain",
        "keywords": ["stomach pain", "stomach ache", "belly pain", "abdominal",
                     "kadoopu noppi", "pet dard", "potta noppi", "కడుపు నొప్పి",
                     "पेट दर्द"],
        "answer": (
            "**Stomach pain - what helps**\n"
            "- Sip warm water. Eat light food (rice curd, khichdi).\n"
            "- Antacid syrup/tablet (gelusil-type) helps burning or acidity "
            "pain - take after food as per the packet.\n"
            "- Avoid painkillers like ibuprofen - they can worsen it.\n\n"
            "**See a doctor urgently if:** severe or worsening pain, pain on "
            "the lower right side, vomiting blood, black stools, pain after "
            "an injury, or pain with high fever - call 108 or go to the PHC."
        ),
    },
    {
        "topic": "worms",
        "keywords": ["worms", "worm", "intestinal worm", "kirmulu", "krimi",
                     "keede", "క్రిములు", "పురుగులు", "कीड़े"],
        "answer": (
            "**Worm infection - what to do**\n"
            "- Signs: stomach pain, itching around the anus (especially at "
            "night), weakness, poor appetite, anaemia in children.\n"
            "- **Albendazole 400 mg single chewable tablet** is given FREE "
            "twice a year to everyone above 1 year on National Deworming Day "
            "at schools/Anganwadi centres - take it from the PHC.\n"
            "- Not for pregnant women in the first trimester - ask the PHC.\n\n"
            "**Prevention:** wash hands with soap before eating, wash "
            "vegetables well, wear slippers, drink boiled/filtered water."
        ),
    },
    # ---------------- PAIN & GENERAL ----------------
    {
        "topic": "headache",
        "keywords": ["headache", "head ache", "head pain", "tala noppi",
                     "sir dard", "migraine", "తలనొప్పి", "తల నొప్పి", "सिरदर्द"],
        "answer": (
            "**Headache - what helps**\n"
            "- Rest in a quiet, dark room. Drink water - dehydration is a "
            "common cause.\n"
            "- **Common tablet for adults:** Paracetamol500 mg - 1 tablet "
            "after food, can repeat after 6 hours (max 4/day).\n"
            "- Wet cloth on the forehead helps some people.\n\n"
            "**See a doctor urgently if:** sudden worst-ever headache, headache "
            "with fever and neck stiffness, vomiting, blurred vision, weakness "
            "on one side, or after a head injury - call 108."
        ),
    },
    {
        "topic": "body pain",
        "keywords": ["body pain", "bodyache", "muscle pain", "kallu noppi",
                     "body noppi", "badan dard", "శరీరం నొప్పి", "బాధ"],
        "answer": (
            "**Body pain - what helps**\n"
            "- Rest and drink more water.\n"
            "- **Common tablet for adults:** Paracetamol 500 mg - 1 tablet "
            "every 6 hours after food (max 4/day).\n"
            "- Warm oil massage and a warm bath can relieve aching.\n\n"
            "**Note:** body pain with fever in our district can be dengue - "
            "if fever is also present, get tested at the PHC and avoid "
            "ibuprofen/aspirin.\n\n"
            "This is general information, not a prescription."
        ),
    },
    {
        "topic": "joint pain",
        "keywords": ["joint pain", "knee pain", "arthritis", "arthritis",
                     "kallu noppi", "jodha dard", "ghutna", "కీళ్ల నొప్పులు",
                     "మోకాలి నొప్పి", "घुटने दर्द"],
        "answer": (
            "**Joint / knee pain - what helps**\n"
            "- Warm compress on the painful joint, 15 minutes twice a day.\n"
            "- Keep weight healthy; avoid climbing stairs excessively during "
            "pain.\n"
            "- Gentle movement is better than complete rest.\n"
            "- **Tablet for adults:** Paracetamol 500 mg - 1 tablet after food "
            "(max 4/day). Avoid long-term ibuprofen without a doctor.\n\n"
            "**See a doctor if:** joint is red, hot and swollen, pain after a "
            "fall with inability to move, or pain lasting more than 2 weeks. "
            "The PHC can also check for calcium/vitamin D deficiency."
        ),
    },
    {
        "topic": "tooth pain",
        "keywords": ["tooth", "toothache", "teeth", "gum", "dental", "pallu",
                     "dant", "daant", "పళ్లు", "దంత", "दांत"],
        "answer": (
            "**Tooth pain - what helps**\n"
            "- Rinse with warm salt water 3-4 times a day.\n"
            "- **Tablet for adults:** Paracetamol 500 mg - 1 tablet after food "
            "(max 4/day) for pain.\n"
            "- Clove oil on a cotton ball at the painful tooth can numb it.\n"
            "- Avoid very hot, cold, or sweet food.\n\n"
            "**See a dentist/PHC within days:** tooth pain always means a "
            "cavity or infection that needs treatment - tablets only delay it. "
            "Face swelling with tooth pain needs the doctor the SAME day.\n\n"
            "**Prevention:** brush twice daily with fluoride toothpaste."
        ),
    },
    # ---------------- EYES & EARS ----------------
    {
        "topic": "eye problem",
        "keywords": ["eye", "eyes", "red eye", "eye pain", "kallu",
                     "kalla jalubu", "aankh", "కళ్లు", "కంటి", "आंख"],
        "answer": (
            "**Red / painful eye - what helps**\n"
            "- Wash hands often; do NOT touch or rub the eyes.\n"
            "- Separate towel and pillow for the patient (red eye spreads "
            "fast in families).\n"
            "- Clean lids with clean water; avoid dust and smoke.\n"
            "- Do NOT use anyone else's eye drops.\n\n"
            "**See a doctor within 1-2 days:** red eye is usually mild but "
            "needs proper drops. **Go same day (call 108) if:** injury, "
            "chemical splash (wash with water 15 min first), severe pain, "
            "vision loss, or a white spot on the cornea."
        ),
    },
    {
        "topic": "ear pain",
        "keywords": ["ear", "ear pain", "ear discharge", "chevi", "chevi noppi",
                     "kaan", "kaandard", "చెవి", "చెవి నొప్పి", "कान"],
        "answer": (
            "**Ear pain / discharge - what helps**\n"
            "- Never put oil, sticks, or leaves inside the ear.\n"
            "- If discharge is present, gently clean the OUTER ear with a "
            "clean dry cloth only.\n"
            "- **Tablet for adults:** Paracetamol 500 mg for pain (max 4/day).\n"
            "- Avoid water entering the ear while bathing.\n\n"
            "**See a doctor at the PHC within 1-2 days:** ear pain or "
            "discharge usually needs antibiotic drops from a doctor - "
            "untreated infections can affect hearing, especially in children."
        ),
    },
    # ---------------- CHRONIC DISEASES ----------------
    {
        "topic": "diabetes",
        "keywords": ["diabetes", "sugar", "sugar problem", "madhumeham",
                     "shugger", "షుగర్", "మధుమేహం", "मधुमेह", "शुगर"],
        "answer": (
            "**Diabetes - daily care basics**\n"
            "- Signs: excess thirst, frequent urination, weight loss, slow-"
            "healing wounds. A free sugar test is available at the PHC.\n"
            "- Take your prescribed tablets daily even on good days - never "
            "stop on your own.\n"
            "- Cut sugar, sweets, white rice portions; add vegetables, "
            "whole grains, and a 30-minute daily walk.\n"
            "- Check feet daily for cuts - keep them clean and dry.\n\n"
            "**Emergency - go to hospital if:** very drowsy/confused, "
            "vomiting with fast breathing, or a wound that is not healing. "
            "Free checkups are at every PHC under the NCD programme."
        ),
    },
    {
        "topic": "blood pressure",
        "keywords": ["blood pressure", "bp", "hypertension", "pressure",
                     "raktapu podu", "piddi", "బీపీ", "పీడనం", "बीपी", "उच्च"],
        "answer": (
            "**Blood pressure - daily care basics**\n"
            "- Take prescribed BP tablets daily at the same time, even when "
            "you feel fine - high BP has no symptoms but damages the heart "
            "and brain.\n"
            "- Reduce salt to less than 1 teaspoon a day total (including "
            "pickles and papads).\n"
            "- Walk 30 minutes daily, avoid tobacco, limit alcohol.\n"
            "- Free BP checks at every PHC; keep a home record if possible.\n\n"
            "**Emergency - call 108 if:** chest pain, severe headache with "
            "blurred vision, weakness on one side, or slurred speech (stroke "
            "signs). Every minute counts."
        ),
    },
    {
        "topic": "anaemia",
        "keywords": ["anaemia", "anemia", "weakness", "hemoglobin", "raktaheenata",
                     "balam leka", "రక్తహీనత", "खून की कमी", "कमजोरी"],
        "answer": (
            "**Anaemia (weak blood) - what to do**\n"
            "- Signs: tiredness, pale eyes/nails, dizziness on standing, "
            "breathlessness on small effort.\n"
            "- Get a free haemoglobin test at the PHC.\n"
            "- **Iron-folic acid (IFA) tablets are FREE** at the PHC - one "
            "daily after food, with lemon/orange water (vitamin C helps "
            "absorption). Do not take with tea or milk.\n"
            "- Eat greens (thotakura, palakura), drumstick leaves, dates, "
            "jaggery, eggs, and dal.\n\n"
            "**See a doctor if:** very pale, fainting, or breathless at rest - "
            "especially in pregnancy and adolescent girls."
        ),
    },
    # ---------------- SKIN, ALLERGY, INJURIES ----------------
    {
        "topic": "allergy",
        "keywords": ["allergy", "itching", "rash", "hives", "skin allergy",
                     "dadduru", "pitika", "khujli", "దద్దుర్లు", "పిటిక",
                     "खुजली", "रैश"],
        "answer": (
            "**Itching / skin allergy - what helps**\n"
            "- Apply a cool wet cloth; avoid scratching (infection risk).\n"
            "- Use mild soap; wear loose cotton clothes.\n"
            "- **Tablet for adults:** an antihistamine like cetirizine 10 mg - "
            "1 tablet at night (may cause sleepiness; do not drive after).\n"
            "- Calamine lotion soothes itching.\n\n"
            "**See a doctor urgently if:** rash with face/lip swelling, "
            "breathing difficulty (call 108 - severe allergy), rash with "
            "fever, spreading redness with pain, or pus."
        ),
    },
    {
        "topic": "fungal infection",
        "keywords": ["fungal", "ringworm", "jock itch", "athlete", "dadru",
                     "budda dadduru", "daad", "పొట్టు", "दाद"],
        "answer": (
            "**Ringworm / fungal infection - what helps**\n"
            "- Keep the area clean and DRY - fungus grows in sweat.\n"
            "- Bathe twice daily; dry folds (groin, between toes) well.\n"
            "- Wear cotton and change sweaty clothes daily.\n"
            "- **Cream:** an antifungal cream (clotrimazole type) twice a "
            "day, and continue 2 weeks after it clears.\n"
            "- Do NOT share towels or clothes; do not use steroid creams.\n\n"
            "**See a doctor if:** it spreads despite 2 weeks of cream, or "
            "there is pus, hair loss patches on the scalp, or nail involvement."
        ),
    },
    {
        "topic": "cuts and wounds",
        "keywords": ["cut", "wound", "injury", "bleeding", "gaya", "kaat",
                     "gati", "గాయం", "కట్", "घाव", "कट"],
        "answer": (
            "**Cuts and wounds - first aid**\n"
            "- Wash your hands, then wash the wound with clean running water "
            "and soap around it.\n"
            "- Press with a clean cloth for 10 minutes to stop bleeding - "
            "do not keep lifting to check.\n"
            "- Apply antiseptic (like savlon/betadine) and cover with a clean "
            "bandage; change daily.\n"
            "- For tetanus safety, show it at the PHC if deep or dirty.\n\n"
            "**Call 108 if:** bleeding does not stop after 15 minutes of firm "
            "pressure, the cut is deep/gaping, or caused by a rusty object."
        ),
    },
    {
        "topic": "burns",
        "keywords": ["burn", "burns", "scald", "hot water", "kagguthundi",
                     "jal", "కాగుతుంది", "మంట", "जलन", "जला"],
        "answer": (
            "**Burns - first aid**\n"
            "- **Cool the burn under gently running cool water for 15-20 "
            "minutes.** This is the single most important step.\n"
            "- Do NOT apply toothpaste, ghee, oil, ice, or egg - they cause "
            "infection.\n"
            "- Remove rings/belts near the burn before swelling starts.\n"
            "- Cover loosely with a clean dry cloth. Give water to drink.\n\n"
            "**Call 108 if:** burn larger than the person's palm, on face/"
            "hands/genitals, white or charred skin, or any burn in a child. "
            "Do not burst blisters."
        ),
    },
    {
        "topic": "heat stroke",
        "keywords": ["heat", "heat stroke", "sun stroke", "loogie", "enatha",
                     "loo", "ఎండ", "ఎండ కొట్టింది", "लू"],
        "answer": (
            "**Heat stroke - EMERGENCY, call 108**\n"
            "- Signs after sun exposure: hot dry skin (or heavy sweating), "
            "confusion, fainting, very fast heartbeat.\n"
            "- Move to shade immediately; loosen clothes.\n"
            "- Cool aggressively: wet cloths on head, neck, armpits, groin; "
            "fan continuously; sponge with water.\n"
            "- If conscious, give ORS/water in sips. Do NOT give fever tablets.\n\n"
            "**Prevention in summer:** avoid 12-3 pm field work, carry ORS, "
            "cover your head, drink water hourly."
        ),
    },
    {
        "topic": "dog bite",
        "keywords": ["dog bite", "dog", "kukka karachindi", "kukka", "kutta",
                     "కుక్క కాటు", "कुत्ते"],
        "answer": (
            "**Dog (or cat/monkey) bite - act immediately**\n"
            "- Wash the wound under running water with soap for **15 full "
            "minutes** - this alone greatly reduces risk.\n"
            "- Apply antiseptic; do not stitch or apply herbs/chilli.\n"
            "- **Go to the PHC the SAME DAY for anti-rabies vaccine - it is "
            "free and life-saving.** Rabies is 100% fatal once symptoms "
            "start, but 100% preventable with the vaccine series.\n"
            "- Note the animal; if it is a stray, inform the PHC.\n\n"
            "Never skip or delay the vaccine, even for a small scratch "
            "without bleeding."
        ),
    },
    {
        "topic": "snake bite",
        "keywords": ["snake", "snake bite", "snakebite", "pamu karachindi",
                     "pamu kadi", "saap", "saanp", "పాము కాటు", "పాము",
                     "सांप"],
        "answer": (
            "**SNAKE BITE - EMERGENCY. Call 108 NOW.**\n"
            "- Keep the person and still. Movement spreads venom fast.\n"
            "- Keep the bitten limb BELOW heart level. Remove rings, "
            "bangles, tight clothing.\n"
            "- Do NOT cut, suck, or tie the spot tightly. Do NOT apply "
            "turmeric/chilli or herbs on the bite.\n"
            "- Note the snake's colour/shape if safe - never try to catch it.\n"
            "- Go to the nearest PHC/hospital with anti-snake venom "
            "immediately - do not wait for the pain to decide.\n\n"
            "Every minute matters. 108 ambulance has free treatment pathways."
        ),
    },
    {
        "topic": "urinary problem",
        "keywords": ["urine", "urinary", "burning urine", "uti", "mutra",
                     "mootta", "pesab", "మూత్రం", "पेशाब"],
        "answer": (
            "**Burning urination / urinary infection - what helps**\n"
            "- Drink 2.5-3 litres of water daily to flush the system.\n"
            "- Do not hold urine for long; pass urine fully.\n"
            "- Wash with water and keep the area dry; wear cotton.\n"
            "- Coconut water can soothe symptoms.\n\n"
            "**See a doctor at the PHC if:** burning with fever, back or "
            "lower belly pain, blood in urine, or symptoms beyond 2 days - "
            "a true

> ⚠️ The response reached the length limit. Reply **continue** to get the rest.
