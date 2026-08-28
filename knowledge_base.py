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
    "ADULT package dosing plus cautions. 3) Always advise confirming with "
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
    "vomiting, headache, stomach pain, acidity, diabetes, blood pressure, "
    "allergy, wounds, burns, dog bite, snake bite, pregnancy care, child "
    "health, stress, or nutrition. "
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
                     "khansi", "jukam"],
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
        "topic": "dog bite",
        "keywords": ["dog bite", "kukka"],
        "answer": (
            "Dog (or cat/monkey) bite - act immediately:\n"
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
