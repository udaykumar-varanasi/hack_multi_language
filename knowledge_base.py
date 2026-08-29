DISCLAIMER = (
    "ArogyaMitra shares general health information for awareness only. "
    "It is NOT a doctor and does not diagnose or prescribe. Always confirm "
    "with a doctor, PHC, ASHA worker, or pharmacist before taking any medicine."
)

EMERGENCY_CONTACTS = {
    "Ambulance": "108",
    "National Emergency": "112",
    "Health Helpline": "104",
}

SYSTEM_PROMPT = (
    "You are ArogyaMitra, a friendly rural health guide for villages in "
    "Andhra Pradesh, India. Rules: 1) General health information only, "
    "never diagnose. 2) You MAY mention common over-the-counter options "
    "like paracetamol for fever or ORS for loose motions, with standard "
    "ADULT dosing plus cautions. 3) Always advise confirming with "
    "a doctor, PHC, ASHA worker, or pharmacist. 4) Always say when to see "
    "a doctor. 5) Reply in the SAME language the user used (Telugu, Hindi "
    "or English), short simple sentences with bullet points. 6) Under 200 "
    "words. 7) For emergencies, first say call 108 or 112, then basic "
    "first aid only. 8) Never suggest prescription medicines like "
    "antibiotics or steroids, and never give doses for babies under 1 year."
)

URGENT_KEYWORDS = [
    "chest pain", "not breathing", "breathless", "unconscious", "seizure",
    "convulsion", "snake", "poison", "suicide", "bleeding heavily",
    "heavy bleeding", "accident", "stroke", "slurred", "overdose",
    "severe burn", "drowning", "dog bite", "fits", "heart attack",
    "chhati", "chaati", "pamu", "saanp", "nokkindi",
]

FALLBACK_ANSWER = (
    "I am not fully sure about that, so I will not guess. "
    "For any health concern, visit the nearest PHC or call 104. "
    "If this feels urgent, call 108 or 112 now. "
    "You can ask me about: fever, dengue, cough and cold, loose motions, "
    "vomiting, headache, stomach pain, acidity, constipation, wounds, "
    "burns, diabetes, blood pressure, allergy, dog bite, snake bite, "
    "toothache, ear pain, eye problems, jaundice, periods, pregnancy "
    "care, child health, stress, or nutrition. "
    "This is general information only - please consult a doctor."
)

KB_ENTRIES = [
    {
        "topic": "fever",
        "keywords": ["fever", "jwaram", "bukhar", "temperature",
                     "shivering"],
        "answer": (
            "Fever - what helps:\n"
            "- Rest and drink plenty of fluids.\n"
            "- A lukewarm sponge bath can bring temperature down.\n"
            "- Common tablet for adults: Paracetamol 500 mg, 1 tablet "
            "every 6 hours after food, maximum 4 in 24 hours.\n"
            "- Do NOT take ibuprofen or aspirin until dengue is ruled out.\n"
            "See a doctor if fever lasts more than 3 days, goes above "
            "103 F, or comes with rash or severe body pain. Babies, "
            "elderly and pregnant women should see a doctor on day 1."
        ),
    },
    {
        "topic": "stomach pain",
        "keywords": ["stomach pain", "stomach ache", "tummy", "pet dard",
                     "kadoopu noppi", "abdominal pain", "belly pain",
                     "pet noppi"],
        "answer": (
            "Stomach pain - what helps:\n"
            "- Sip warm water. Rest. Avoid oily, spicy food for a day.\n"
            "- A hot water bag on the belly relaxes cramps.\n"
            "- If there is gas or bloating, walking for 10 minutes and "
            "an antacid (1 spoon after food) may help.\n"
            "Do NOT take painkillers like ibuprofen on an empty stomach.\n"
            "Go to a doctor or call 108 URGENTLY if: pain is very severe "
            "or on the lower right side, vomiting blood, blood in stool, "
            "belly is hard like a board, pain after an injury, or if it "
            "is a pregnant woman with pain."
        ),
    },
    {
        "topic": "acidity",
        "keywords": ["acidity", "gas", "heartburn", "acid reflux",
                     "adagi", "bloating", "indigestion", "ajiranam"],
        "answer": (
            "Acidity / gas - what helps:\n"
            "- Eat small meals on time; do not skip meals.\n"
            "- Avoid tea/coffee on an empty stomach, spicy and fried "
            "food, and lying down right after eating.\n"
            "- Cold milk or cold water gives quick relief.\n"
            "- Antacid gel (1-2 spoons after meals or bedtime) helps.\n"
            "See a doctor if burning lasts more than 2 weeks, you are "
            "losing weight, vomiting blood, or black stools appear."
        ),
    },
    {
        "topic": "constipation",
        "keywords": ["constipation", "motion problem", "kabz",
                     "malabaddhata", "not passing stool", "hard stool"],
        "answer": (
            "Constipation - what helps:\n"
            "- Drink 8-10 glasses of water a day.\n"
            "- Eat more fiber: vegetables, fruits (papaya is excellent), "
            "whole grains. Soaked raisins at night help.\n"
            "- Walk 20-30 minutes daily. Go to the toilet at the same "
            "time every morning - do not suppress the urge.\n"
            "See a doctor if no motion for more than 4-5 days, severe "
            "pain, vomiting, blood in stool, or if you are elderly with "
            "sudden constipation."
        ),
    },
    {
        "topic": "wound",
        "keywords": ["wound", "cut", "injury", "bleeding", "gaya",
                     "scratched"],
        "answer": (
            "Cuts and wounds - first aid:\n"
            "- Wash your hands, then wash the wound with clean running "
            "water and soap around it.\n"
            "- Press with a clean cloth for 10 minutes to stop bleeding.\n"
            "- Apply antiseptic and cover with a clean bandage. Change "
            "it daily.\n"
            "Go to the PHC if: bleeding does not stop after 15 minutes "
            "of pressure, the cut is deep or gaping, caused by rust or "
            "a dirty object (need tetanus shot), or shows pus, redness "
            "spreading, or fever later."
        ),
    },
    {
        "topic": "dengue",
        "keywords": ["dengue", "platelet", "mosquito fever"],
        "answer": (
            "Dengue - warning signs and care:\n"
            "- High fever with severe body pain or pain behind the eyes: "
            "get a dengue test at the PHC on day 1 or 2 (free).\n"
            "- Do NOT take ibuprofen, aspirin or combiflam - only "
            "paracetamol.\n"
            "- Drink lots of fluids: ORS, coconut water, soups.\n"
            "Go to hospital IMMEDIATELY if: bleeding gums or nose, red "
            "spots on skin, severe stomach pain, very low urine, or "
            "drowsiness. Prevention: empty water containers weekly."
        ),
    },
    {
        "topic": "cough and cold",
        "keywords": ["cough", "cold", "sneeze", "throat", "daggu",
                     "khansi", "jukam", "sore throat"],
        "answer": (
            "Cough and cold - what helps:\n"
            "- Warm fluids like soups and pepper-turmeric kashayam.\n"
            "- Steam inhalation 2 to 3 times a day for blocked nose.\n"
            "- Salt-water gargle for throat pain. Honey soothes cough "
            "(not for babies under 1 year).\n"
            "See a doctor if cough lasts more than 2 weeks, blood in "
            "sputum, breathing trouble, or weight loss (get TB checked "
            "at the PHC, testing is free)."
        ),
    },
    {
        "topic": "loose motions",
        "keywords": ["loose motion", "diarrhea", "diarrhoea", "dast",
                     "motions"],
        "answer": (
            "Loose motions - what helps:\n"
            "- ORS is the most important thing. Mix 1 sachet in 1 litre "
            "clean water and sip continuously. Adults: 2 to 3 litres a "
            "day. Homemade: 1 litre water + 6 tsp sugar + half tsp salt.\n"
            "- Eat bananas, rice, curd rice. Avoid oily food and milk.\n"
            "- Do NOT take loperamide if you have fever or blood in stool.\n"
            "See a doctor if more than 6 motions a day, blood in stool, "
            "fever, or signs of dehydration. Children dehydrate fast - "
            "go to the PHC early."
        ),
    },
    {
        "topic": "vomiting",
        "keywords": ["vomit", "nausea", "ulti", "kakulu"],
        "answer": (
            "Vomiting - what helps:\n"
            "- Sip ORS or clean water slowly, small sips every 10 "
            "minutes.\n"
            "- Rest the stomach 1 to 2 hours, then try banana or rice.\n"
            "- Ginger water or lemon water with a pinch of salt helps.\n"
            "See a doctor if vomiting lasts more than 6 hours, blood in "
            "vomit, severe stomach pain, or after a head injury."
        ),
    },
    {
        "topic": "headache",
        "keywords": ["headache", "head ache", "tala noppi", "sir dard",
                     "migraine"],
        "answer": (
            "Headache - what helps:\n"
            "- Rest in a quiet, dark room. Drink water - dehydration is "
            "a common cause.\n"
            "- Common tablet for adults: Paracetamol 500 mg, 1 tablet "
            "after food, can repeat after 6 hours (max 4 per day).\n"
            "- A wet cloth on the forehead helps some people.\n"
            "Call 108 urgently if: sudden worst-ever headache, headache "
            "with fever and neck stiffness, blurred vision, weakness on "
            "one side, or after a head injury."
        ),
    },
    {
        "topic": "diabetes",
        "keywords": ["diabetes", "sugar", "madhumeham"],
        "answer": (
            "Diabetes - daily care basics:\n"
            "- Signs: excess thirst, frequent urination, weight loss, "
            "slow-healing wounds. Free sugar test at the PHC.\n"
            "- Take prescribed tablets daily - never stop on your own.\n"
            "- Cut sugar and sweets; add vegetables and a 30 minute "
            "daily walk.\n"
            "- Check feet daily for cuts.\n"
            "Go to hospital if very drowsy or confused, vomiting with "
            "fast breathing, or a wound is not healing."
        ),
    },
    {
        "topic": "blood pressure",
        "keywords": ["blood pressure", "bp", "hypertension", "pressure"],
        "answer": (
            "Blood pressure - daily care basics:\n"
            "- Take prescribed BP tablets daily at the same time, even "
            "when you feel fine.\n"
            "- Reduce salt to less than 1 teaspoon a day total.\n"
            "- Walk 30 minutes daily, avoid tobacco. Free BP checks at "
            "every PHC.\n"
            "Call 108 if chest pain, severe headache with blurred "
            "vision, weakness on one side, or slurred speech - stroke "
            "signs. Every minute counts."
        ),
    },
    {
        "topic": "allergy",
        "keywords": ["allergy", "itching", "rash", "hives", "khujli"],
        "answer": (
            "Itching / skin allergy - what helps:\n"
            "- Apply a cool wet cloth; avoid scratching.\n"
            "- Tablet for adults: cetirizine 10 mg, 1 tablet at night "
            "(causes sleepiness - do not drive after).\n"
            "- Calamine lotion soothes itching.\n"
            "Call 108 if rash with face or lip swelling or breathing "
            "difficulty. See a doctor if rash has fever, spreading "
            "redness with pain, or pus."
        ),
    },
    {
        "topic": "burns",
        "keywords": ["burn", "scald", "hot water"],
        "answer": (
            "Burns - first aid:\n"
            "- Cool the burn under gently running cool water for 15 to "
            "20 minutes. This is the most important step.\n"
            "- Do NOT apply toothpaste, ghee, oil or ice.\n"
            "- Cover loosely with a clean dry cloth. Do not burst "
            "blisters.\n"
            "Call 108 if the burn is larger than the person's palm, on "
            "the face or hands, skin is white or charred, or any burn "
            "in a child."
        ),
    },
    {
        "topic": "toothache",
        "keywords": ["toothache", "tooth pain", "dant dard",
                     "palla noppi", "teeth pain", "gum"],
        "answer": (
            "Toothache - what helps:\n"
            "- Rinse with warm salt water (half tsp salt in a glass) "
            "3-4 times a day.\n"
            "- Floss gently to remove stuck food. Do not put aspirin "
            "directly on the gum - it burns.\n"
            "- Paracetamol 500 mg (adults, 1 tablet after food) helps "
            "the pain temporarily.\n"
            "See a dentist or PHC within a few days - decay does not "
            "heal on its own. Go sooner if the face is swelling or you "
            "have fever with the pain."
        ),
    },
    {
        "topic": "ear pain",
        "keywords": ["ear pain", "earache", "kaan dard", "chevi noppi",
                     "ear"],
        "answer": (
            "Ear pain - what helps:\n"
            "- A warm (not hot) cloth held over the ear soothes pain.\n"
            "- Do NOT put oil, leaves or sticks into the ear.\n"
            "- Paracetamol 500 mg (adults, 1 tablet after food) helps.\n"
            "- If water got in while bathing, tilt the head and let it "
            "drain; dry the outer ear only.\n"
            "See a doctor or PHC if pain lasts more than 2 days, there "
            "is discharge or pus from the ear, hearing reduces, or a "
            "child with ear pain also has fever."
        ),
    },
    {
        "topic": "eye problem",
        "keywords": ["eye", "eyes", "red eye", "kanu", "aankh",
                     "eye pain", "vision"],
        "answer": (
            "Eye problems - what helps:\n"
            "- Red itchy eye (likely conjunctivitis): wash hands often, "
            "use a separate towel, do not rub. Clean eyelids with clean "
            "water. It usually settles in 5-7 days.\n"
            "- Dust in the eye: blink in clean water; do not rub.\n"
            "Do NOT use anyone else's eye drops.\n"
            "Go to the PHC or eye doctor SAME DAY if: eye injury, "
            "chemical splashed in the eye, sudden vision loss, severe "
            "pain, or a white spot on the black part of the eye."
        ),
    },
    {
        "topic": "jaundice",
        "keywords": ["jaundice", "yellow eyes", "kamla", "paandu",
                     "yellow skin", "hepatitis"],
        "answer": (
            "Jaundice (yellow eyes or skin) - what to do:\n"
            "- Get a blood test at the PHC - liver tests are often "
            "free. Jaundice has many causes; do not self-treat.\n"
            "- Rest well, drink plenty of fluids, eat boiled food, "
            "avoid oily food and completely avoid alcohol.\n"
            "- Do NOT take random liver tablets or unknown herbs - some "
            "damage the liver more.\n"
            "Go to hospital URGENTLY if: drowsiness or confusion, "
            "repeated vomiting, bleeding, swelling of the belly, or "
            "jaundice in a newborn baby (always urgent)."
        ),
    },
    {
        "topic": "periods",
        "keywords": ["period", "periods", "menstrual", "monthly",
                     "menstruation", "painful periods", "cramps"],
        "answer": (
            "Period pain - what helps:\n"
            "- Hot water bag on the lower belly works well.\n"
            "- Warm drinks, light walking, and rest help.\n"
            "- Paracetamol 500 mg (1 tablet after food) is safe for "
            "period pain in adults.\n"
            "- Track your cycle; some pain is normal.\n"
            "See a doctor or PHC if: bleeding so heavy you soak a pad "
            "every 1-2 hours, periods lasting more than 7-8 days, "
            "fainting, severe sudden one-sided pain, bleeding during "
            "pregnancy, or periods that stopped for months suddenly."
        ),
    },
    {
        "topic": "pregnancy",
        "keywords": ["pregnan", "delivery", "garbini", "expecting",
                     "morning sickness"],
        "answer": (
            "Pregnancy care basics:\n"
            "- Register at the PHC early - get FREE checkups, iron and "
            "folic acid tablets, and TT vaccines.\n"
            "- Take iron tablets daily, eat extra food, milk, green "
            "leafy vegetables and fruits.\n"
            "- Attend 4 or more checkups; deliver in a hospital - "
            "call 108 for free transport.\n"
            "Go to hospital IMMEDIATELY if: bleeding, severe headache "
            "with blurred vision, swelling of face and hands, water "
            "breaks, baby movements reduce, or labour pains start."
        ),
    },
    {
        "topic": "child health",
        "keywords": ["child fever", "baby fever", "kid fever",
                     "child health", "child sick", "not feeding",
                     "baby sick"],
        "answer": (
            "Sick child - when to act fast:\n"
            "- For fever, syrup dose depends on WEIGHT - ask the PHC "
            "or pharmacist; never give adult tablets to a child.\n"
            "- Keep giving fluids and breastmilk; light clothing; "
            "sponging with lukewarm water.\n"
            "Go to the PHC or call 108 IMMEDIATELY if the child: is "
            "under 2 months with any fever, refuses feeds, is very "
            "drowsy or will not wake, has fits, breathes fast or with "
            "difficulty, has sunken eyes or no tears (dehydration), or "
            "fever with rash."
        ),
    },
    {
        "topic": "dog bite",
        "keywords": ["dog bite", "kukka", "cat bite", "monkey bite"],
        "answer": (
            "Dog (or cat or monkey) bite - act immediately:\n"
            "- Wash the wound under running water with soap for 15 full "
            "minutes.\n"
            "- Apply antiseptic. Do not apply herbs or chilli.\n"
            "- Go to the PHC the SAME DAY for anti-rabies vaccine - it "
            "is free and life-saving. Rabies is fatal once symptoms "
            "start, but preventable with the vaccine series.\n"
            "Never skip or delay the vaccine, even for a small scratch."
        ),
    },
    {
        "topic": "snake bite",
        "keywords": ["snake", "snake bite", "snakebite", "pamu"],
        "answer": (
            "SNAKE BITE - EMERGENCY. Call 108.\n"
            "- Keep the person calm and still. Movement spreads venom "
            "fast.\n"
            "- Keep the bitten limb BELOW heart level. Remove rings and "
            "tight clothing.\n"
            "- Do NOT cut, suck, or tie the spot tightly. Do NOT apply "
            "turmeric or herbs.\n"
            "- Note the snake's colour if safe - never try to catch it.\n"
            "- Go to the nearest PHC or hospital with anti-snake venom "
            "immediately."
        ),
    },
    {
        "topic": "stress",
        "keywords": ["stress", "tension", "anxiety", "depression",
                     "sad", "sleep problem", "insomnia", "worry"],
        "answer": (
            "Stress, sleep and mental health - what helps:\n"
            "- Fix sleep time: no screens 1 hour before bed, no tea or "
            "coffee after evening.\n"
            "- 20-30 minutes of walking daily and talking to family or "
            "friends genuinely helps.\n"
            "- Deep slow breathing: in for 4 counts, out for 6, for a "
            "few minutes when tense.\n"
            "- Tele-MANAS free mental health helpline: 14416 (24x7, "
            "available in Telugu and other languages).\n"
            "See a doctor or PHC if low mood or poor sleep lasts over "
            "2 weeks, or if there are thoughts of self-harm - call "
            "104 or 14416 right away."
        ),
    },
    {
        "topic": "nutrition",
        "keywords": ["nutrition", "diet", "weakness", "weak",
                     "anemia", "weight", "food"],
        "answer": (
            "Good nutrition on a budget:\n"
            "- Every meal: rice or roti + dal or curd + a vegetable.\n"
            "- Cheap proteins: eggs, groundnut, dal, milk, soya.\n"
            "- Weekly: green leafy vegetables and seasonal fruit.\n"
            "- Weakness and tiredness are often anemia (low blood) - "
            "free hemoglobin test at the PHC; iron tablets given free.\n"
            "See a doctor or PHC if losing weight without trying, "
            "swelling of feet, or a child is not gaining weight (ask "
            "about nutrition support at the Anganwadi centre)."
        ),
    },
]


def search_kb(query):
    """Return (score, entry) for the best keyword match, or (0, None)."""
    q = (query or "").lower()
    best_score, best_entry = 0, None
    for entry in KB_ENTRIES:
        score = 0
        for kw in entry["keywords"]:
            if kw.lower() in q:
                score += 2 if len(kw) > 4 else 1
        if score > best_score:
            best_score, best_entry = score, entry
    return best_score, best_entry
