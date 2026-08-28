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
    "Women Helpline": "1091",
    "Child Helpline": "1098",
}

SYSTEM_PROMPT = (
    "You are ArogyaMitra, a friendly rural health guide for villages in "
    "Andhra Pradesh, India. Rules: 1) General health information only, "
    "never diagnose. 2) You MAY mention common over-the-counter options "
    "(paracetamol for fever, ORS for loose motions) with standard ADULT "
    "package dosing plus cautions. 3) Always advise confirming with a "
    "doctor, PHC, ASHA worker, or pharmacist. 4) Always say when to see "
    "a doctor. 5) Reply in the SAME language the user used (Telugu, Hindi "
    "or English), short simple sentences with bullet points. 6) Under 200 "
    "words. 7) For emergencies, first say call 108 or 112, then basic "
    "first aid only. 8) Never suggest prescription medicines (antibiotics, "
    "steroids) and never give doses for babies under 1 year."
)

URGENT_KEYWORDS = [
    "chest pain", "not breathing", "breathless", "unconscious", "seizure",
    "convulsion", "snake", "poison", "suicide", "bleeding heavily",
    "heavy bleeding", "accident", "stroke", "slurred", "overdose",
    "severe burn", "drowning", "dog bite", "fits", "heart attack",
    "chhati", "chaati", "pamu", "saap", "saanp", "nokkindi",
]

FALLBACK_ANSWER = (
    "I am not fully sure about that, so I will not guess. "
    "For any health concern, visit the nearest PHC or call 104. "
    "If this feels urgent, call 108 or 112 now. "
    "You can ask me about: fever, dengue, cough and cold, loose motions, "
    "vomiting, headache, body pain, stomach pain, acidity, constipation, "
    "diabetes, blood pressure, asthma, allergy, skin problems, tooth pain, "
    "joint pain, urinary problems, period problems, anaemia, dog bite, "
    "snake bite, burns, cuts, heat stroke, child health, pregnancy care, "
    "stress, or nutrition. "
    "This is general information only - please consult a doctor."
)

KB_ENTRIES = [
    {
        "topic": "fever",
        "keywords": ["fever", "jwaram", "jvaram", "bukhar", "temperature",
                     "shivering", "jvaram", "bukhar"],
        "answer": (
            "**Fever - what helps**\n"
            "- Rest and drink plenty of fluids (water, buttermilk, soups).\n"
            "- A lukewarm sponge bath can bring temperature down.\n"
            "- **Common tablet for adults:** Paracetamol 500 mg - 1 tablet "
            "every 6 hours after food, maximum 4 tablets in 24 hours.\n"
            "- Do NOT take ibuprofen or aspirin until dengue is ruled out.\n\n"
            "**See a doctor (PHC or call 104) if:** fever lasts more than "
            "3 days, goes above 103 F, or comes with rash, severe body pain, "
            "or very low urine. Babies, elderly and pregnant women should "
            "see a doctor on day 1."
        ),
    },
    {
        "topic": "dengue",
        "keywords": ["dengue", "dengu", "platelet", "mosquito fever"],
        "answer": (
            "**Dengue - warning signs and care**\n"
            "- High fever with severe body pain or pain behind the eyes "
            "needs a **dengue test at the PHC on day 1-2** (free).\n"
            "- Do NOT take ibuprofen, aspirin or combiflam - only paracetamol.\n"
            "- Drink lots of fluids: ORS, coconut water, soups. Rest fully.\n\n"
            "**Go to hospital IMMEDIATELY if:** bleeding gums or nose, black "
            "stools, red spots on skin, severe stomach pain, very low urine, "
            "or drowsiness.\n\n"
            "**Prevention:** empty water containers weekly, sleep under a net."
        ),
    },
    {
        "topic": "cough and cold",
        "keywords": ["cough", "cold", "sneeze", "throat", "daggu", "jalubu",
                     "khansi", "jukam", "zukam"],
        "answer": (
            "**Cough and cold - what helps**\n"
            "- Warm fluids: warm water, soups, pepper-turmeric kashayam.\n"
            "- Steam inhalation 2-3 times a day for blocked nose.\n"
            "- Salt-water gargle for throat pain. Honey soothes cough "
            "(not for babies under 1 year).\n"
            "- **If fever or body pain is troublesome:** Paracetamol 500 mg "
            "- 1 tablet every 6 hours after food (max 4/day).\n\n"
            "**See a doctor if:** cough lasts more than 2 weeks, blood in "
            "sputum, breathing trouble, or weight loss (get TB checked at PHC)."
        ),
    },
    {
        "topic": "tuberculosis",
        "keywords": ["tuberculosis", "tb", "kshayam", "blood in cough",
                     "cough 2 weeks", "cough 3 weeks"],
        "answer": (
            "**Cough lasting more than 2 weeks - get checked for TB**\n"
            "- TB testing and treatment are **completely FREE at government "
            "PHCs** under the NTEP programme.\n"
            "- Warning signs: cough 2+ weeks, blood in sputum, evening fever, "
            "night sweats, weight loss.\n"
            "- TB is curable - treatment takes 6-9 months and must be "
            "completed.\n\n"
            "Go to the PHC this week for a free sputum test. Do not wait."
        ),
    },
    {
        "topic": "asthma",
        "keywords": ["asthma", "wheezing", "wheeze", "breathing problem",
                     "shwasam", "aaspata"],
        "answer": (
            "**Wheezing / breathing difficulty**\n"
            "- Avoid dust, smoke and strong smells; use a cloth over the "
            "nose while working in fields.\n"
            "- Sit upright, lean slightly forward during an attack.\n"
            "- If a doctor has given an **inhaler (like salbutamol)**, use "
            "it as prescribed - inhalers are safe and not addictive.\n\n"
            "**EMERGENCY - call 108 if:** lips or fingers turn blue, cannot "
            "speak full sentences, or the inhaler is not helping."
        ),
    },
    {
        "topic": "loose motions",
        "keywords": ["loose motion", "loose motions", "diarrhea", "diarrhoea",
                     "stool", "motions", "dast", "atlu"],
        "answer": (
            "**Loose motions - what helps**\n"
            "- **ORS is the most important thing.** Mix 1 sachet in 1 litre "
            "clean water and sip continuously. Adults: 2-3 litres a day.\n"
            "- Homemade: 1 litre water + 6 tsp sugar + half tsp salt.\n"
            "- Eat bananas, rice, curd rice, khichdi. Avoid oily food and milk.\n"
            "- Do NOT take loperamide (Imodium) if you have fever or blood "
            "in stool.\n\n"
            "**See a doctor if:** motions more than 6 a day, blood or mucus "
            "in stool, fever, or dehydration signs (very low urine, "
            "dizziness, dry tongue). Children and elderly dehydrate fast - "
            "go to PHC early."
        ),
    },
    {
        "topic": "vomiting",
        "keywords": ["vomit", "vomiting", "nausea", "throw up", "vomilu",
                     "ulti", "kakulu"],
        "answer": (
            "**Vomiting - what helps**\n"
            "- Sip ORS or clean water slowly, small sips every 10 minutes.\n"
            "- Rest the stomach 1-2 hours, then try banana or rice.\n"
            "- Ginger water or lemon water with a pinch of salt can help.\n\n"
            "**See a doctor if:** vomiting more than 6 hours, blood in vomit, "
            "severe stomach pain, dehydration, or after a head injury. "
            "Pregnant women with severe vomiting should visit the PHC."
        ),
    },
    {
        "topic": "acidity",
        "keywords": ["acidity", "acid reflux", "heartburn", "gas", "bloating",
                     "gastric", "edupu"],
        "answer": (
            "**Acidity / gas - what helps**\n"
            "- Eat smaller meals on time; do not skip breakfast.\n"
            "- Avoid very spicy, oily food, and excess tea/coffee.\n"
            "- Do not lie down for 2 hours after eating.\n"
            "- **Tablet/syrup:** an antacid (gelusil/digene type) after "
            "meals, as per the packet.\n\n"
            "**See a doctor if:** pain wakes you at night, vomiting blood, "
            "black stools, weight loss, or pain swallowing."
        ),
    },
    {
        "topic": "constipation",
        "keywords": ["constipation", "constipated", "kabz", "kabj"],
        "answer": (
            "**Constipation - what helps**\n"
            "- Drink 8-10 glasses of water daily.\n"
            "- Eat more fibre: vegetables, papaya, whole grains, soaked raisins.\n"
            "- Walk 20-30 minutes daily; go to the toilet at the same time daily.\n"
            "- **If needed:** isabgol in warm water at night, per packet. "
            "Avoid regular laxative tablets.\n\n"
            "**See a doctor if:** no motion for 4+ days, blood in stool, "
            "severe pain, vomiting, or sudden weight loss."
        ),
    },
    {
        "topic": "stomach pain",
        "keywords": ["stomach pain", "stomach ache", "belly pain", "abdominal",
                     "kadoopu noppi", "pet dard", "potta noppi"],
        "answer": (
            "**Stomach pain - what helps**\n"
            "- Sip warm water. Eat light food (rice curd, khichdi).\n"
            "- Antacid (gelusil-type) helps burning or acidity pain, per packet.\n"
            "- Avoid painkillers like ibuprofen - they can worsen it.\n\n"
            "**See a doctor urgently if:** severe or worsening pain, pain on "
            "the lower right side, vomiting blood, black stools, pain after "
            "an injury, or pain with high fever - call 108 or go to the PHC."
        ),
    },
    {
        "topic": "headache",
        "keywords": ["headache", "head ache", "head pain", "tala noppi",
                     "sir dard", "migraine"],
        "answer": (
            "**Headache - what helps**\n"
            "- Rest in a quiet, dark room. Drink water - dehydration is common.\n"
            "- **Common tablet for adults:** Paracetamol 500 mg - 1 tablet "
            "after food, can repeat after 6 hours (max 4/day).\n"
            "- Wet cloth on the forehead helps some people.\n\n"
            "**See a doctor urgently if:** sudden worst-ever headache, "
            "headache with fever and neck stiffness, vomiting, blurred "
            "vision, weakness on one side, or after a head injury - call 108."
        ),
    },
    {
        "topic": "body pain",
        "keywords": ["body pain", "bodyache", "muscle pain", "body noppi",
                     "badan dard"],
        "answer": (
            "**Body pain - what helps**\n"
            "- Rest and drink more water.\n"
            "- **Common tablet for adults:** Paracetamol 500 mg - 1 tablet "
            "every 6 hours after food (max 4/day).\n"
            "- Warm oil massage and a warm bath can relieve aching.\n\n"
            "**Note:** body pain with fever can be dengue - get tested at "
            "the PHC and avoid ibuprofen/aspirin."
        ),
    },
    {
        "topic": "joint pain",
        "keywords": ["joint pain", "knee pain", "arthritis", "jodha dard",
                     "ghutna"],
        "answer": (
            "**Joint / knee pain - what helps**\n"
            "- Warm compress on the painful joint, 15 minutes twice a day.\n"
            "- Gentle movement is better than complete rest.\n"
            "- **Tablet for adults:** Paracetamol 500 mg - 1 tablet after "
            "food (max 4/day). Avoid long-term ibuprofen without a doctor.\n\n"
            "**See a doctor if:** joint is red, hot and swollen, pain after "
            "a fall with inability to move, or pain lasting more than 2 weeks."
        ),
    },
    {
        "topic": "tooth pain",
        "keywords": ["tooth", "toothache", "teeth", "gum", "dental", "pallu",
                     "dant"],
        "answer": (
            "**Tooth pain - what helps**\n"
            "- Rinse with warm salt water 3-4 times a day.\n"
            "- **Tablet for adults:** Paracetamol 500 mg - 1 tablet after "
            "food (max 4/day) for pain.\n"
            "- Clove oil on a cotton ball at the painful tooth can numb it.\n\n"
            "**See a dentist/PHC within days:** tooth pain means a cavity or "
            "infection that needs treatment. Face swelling with tooth pain "
            "needs the doctor the SAME day."
        ),
    },
    {
        "topic": "eye problem",
        "keywords": ["eye", "eyes", "red eye", "eye pain", "kallu", "aankh"],
        "answer": (
            "**Red / painful eye - what helps**\n"
            "- Wash hands often; do NOT touch or rub the eyes.\n"
            "- Separate towel and pillow for the patient (red eye spreads fast).\n"
            "- Do NOT use anyone else's eye drops.\n\n"
            "**See a doctor within 1-2 days:** red eye usually needs proper "
            "drops. **Go same day (call 108) if:** injury, chemical splash "
            "(wash with water 15 min first), severe pain, vision loss."
        ),
    },
    {
        "topic": "ear pain",
        "keywords": ["ear", "ear pain", "ear discharge", "chevi", "kaan"],
        "answer": (
            "**Ear pain / discharge - what helps**\n"
            "- Never put oil, sticks or leaves inside the ear.\n"
            "- Clean only the OUTER ear with a clean dry cloth.\n"
            "- **Tablet for adults:** Paracetamol 500 mg for pain (max 4/day).\n"
            "- Avoid water entering the ear while bathing.\n\n"
            "**See a doctor at the PHC within 1-2 days:** ear pain or "
            "discharge usually needs antibiotic drops from a doctor - "
            "untreated infections can affect hearing, especially in children."
        ),
    },
    {
        "topic": "diabetes",
        "keywords": ["diabetes", "sugar", "madhumeham", "shugger"],
        "answer": (
            "**Diabetes - daily care basics**\n"
            "- Signs: excess thirst, frequent urination, weight loss, "
            "slow-healing wounds. Free sugar test at the PHC.\n"
            "- Take prescribed tablets daily - never stop on your own.\n"
            "- Cut sugar and sweets; add vegetables and a 30-minute daily walk.\n"
            "- Check feet daily for cuts - keep them clean and dry.\n\n"
            "**Emergency - go to hospital if:** very drowsy or confused, "
            "vomiting with fast breathing, or a wound that is not healing."
        ),
    },
    {
        "topic": "blood pressure",
        "keywords": ["blood pressure", "bp", "hypertension", "pressure",
                     "piddi"],
        "answer": (
            "**Blood pressure - daily care basics**\n"
            "- Take prescribed BP tablets daily at the same time, even when "
            "you feel fine - high BP has no symptoms but damages the heart.\n"
            "- Reduce salt to less than 1 teaspoon a day total.\n"
            "- Walk 30 minutes daily, avoid tobacco, limit alcohol.\n"
            "- Free BP checks at every PHC.\n\n"
            "**Emergency - call 108 if:** chest pain, severe headache with "
            "blurred vision, weakness on one side, or slurred speech (stroke "
            "signs). Every minute counts."
        ),
    },
    {
        "topic": "anaemia",
        "keywords": ["anaemia", "anemia", "weakness", "hemoglobin",
                     "balam leka"],
        "answer": (
            "**Anaemia (weak blood) - what to do**\n"
            "- Signs: tiredness, pale eyes/nails, dizziness, breathlessness.\n"
            "- Get a free haemoglobin test at the PHC.\n"
            "- **Iron-folic acid tablets are FREE** at the PHC - one daily "
            "after food, with lemon water. Do not take with tea or milk.\n"
            "- Eat greens, drumstick leaves, dates, jaggery, eggs and dal.\n\n"
            "**See a doctor if:** very pale, fainting, or breathless at "
            "rest - especially in pregnancy and adolescent girls."
        ),
    },
    {
        "topic": "allergy",
        "keywords": ["allergy", "itching", "rash", "hives", "dadduru",
                     "khujli", "pitika"],
        "answer": (
            "**Itching / skin allergy - what helps**\n"
            "- Apply a cool wet cloth; avoid scratching (infection risk).\n"
            "- Use mild soap; wear loose cotton clothes.\n"
            "- **Tablet for adults:** cetirizine 10 mg - 1 tablet at night "
            "(may cause sleepiness; do not drive after).\n"
            "- Calamine lotion soothes itching.\n\n"
            "**See a doctor urgently if:** rash with face or lip swelling, "
            "breathing difficulty (call 108 - severe allergy), rash with "
            "fever, spreading redness with pain, or pus."
        ),
    },
    {
        "topic": "cuts and wounds",
        "keywords": ["cut", "wound", "injury", "bleeding", "gaya", "gati"],
        "answer": (
            "**Cuts and wounds - first aid**\n"
            "- Wash hands, then wash the wound with clean running water and "
            "soap around it.\n"
            "- Press with a clean cloth for 10 minutes to stop bleeding.\n"
            "- Apply antiseptic (savlon/betadine) and cover with a clean "
            "bandage; change daily.\n\n"
            "**Call 108 if:** bleeding does not stop after 15 minutes of "
            "firm pressure, the cut is deep or gaping, or caused by a rusty "
            "object (needs anti-tetanus)."
        ),
    },
    {
        "topic": "burns",
        "keywords": ["burn", "burns", "scald", "hot water", "jal"],
        "answer": (
            "**Burns - first aid**\n"
            "- **Cool the burn under gently running cool water for 15-20 "
            "minutes.** This is the single most important step.\n"
            "- Do NOT apply toothpaste, ghee, oil or ice - they cause infection.\n"
            "- Remove rings and belts near the burn before swelling starts.\n"
            "- Cover loosely with a clean dry cloth. Do not burst blisters.\n\n"
            "**Call 108 if:** burn larger than the person's palm, on face or "
            "hands, white or charred skin, or any burn in a child."
        ),
    },
    {
        "topic": "heat stroke",
        "keywords": ["heat", "heat stroke", "sun stroke", "loo", "enatha"],
        "answer": (
            "**Heat stroke - EMERGENCY, call 108**\n"
            "- Signs after sun exposure: hot dry skin, confusion, fainting, "
            "very fast heartbeat.\n"
            "- Move to shade immediately; loosen clothes.\n"
            "- Cool aggressively: wet cloths on head, neck, armpits; fan "
            "continuously; sponge with water.\n"
            "- If conscious, give ORS or water in sips. Do NOT give fever "
            "tablets.\n\n"
            "**Prevention:** avoid 12-3 pm field work, carry ORS, cover "
            "your head, drink water hourly."
        ),
    },
    {
        "topic": "dog bite",
        "keywords": ["dog bite", "kukka karachindi", "kukka katuka", "kutta"],
        "answer": (
            "**Dog (or cat/monkey) bite - act immediately**\n"
            "- Wash the wound under running water with soap for **15 full "
            "minutes** - this alone greatly reduces risk.\n"
            "- Apply antiseptic; do not stitch or apply herbs or chilli.\n"
            "- **Go to the PHC the SAME DAY for anti-rabies vaccine - free "
            "and life-saving.** Rabies is 100% fatal once symptoms start, "
            "but 100% preventable with the vaccine series.\n\n"
            "Never skip or delay the vaccine, even for a small scratch."
        ),
    },
    {
        "topic": "snake bite",
        "keywords": ["snake", "snake bite", "snakebite", "pamu karachindi",
                     "pamu kadi", "saap", "saanp"],
        "answer": (
            "**SNAKE BITE - EMERGENCY. Call 108 NOW.**\n"
            "- Keep the person calm and still. Movement spreads venom fast.\n"
            "- Keep the bitten limb BELOW heart level. Remove rings and "
            "tight clothing.\n"
            "- Do NOT cut, suck, or tie the spot tightly. Do NOT apply "
            "turmeric, chilli or herbs.\n"
            "- Note the snake's colour and shape if safe - never try to "
            "catch it.\n"
            "- Go to the nearest PHC or hospital with anti-snake venom "
            "immediately. Every minute matters."
        ),
    },
    {
        "topic": "urinary problem",
        "keywords": ["urine", "urinary", "burning urine", "uti", "mutra",
                     "mootta", "pesab"],
        "answer": (
            "**Burning urination / urinary infection - what helps**\n"
            "- Drink 2.5-3 litres of water daily to flush the system.\n"
            "- Do not hold urine for long; pass urine fully.\n"
            "- Wash with water and keep the area dry; wear cotton.\n\n"
            "**See a doctor at the PHC if:** burning with fever, back or "
            "lower belly pain, blood in urine, or symptoms beyond 2 days - "
            "a urinary infection needs antibiotic tablets from a doctor; "
            "untreated it can reach the kidneys."
        ),
    },
    {
        "topic": "period problems",
        "keywords": ["period", "periods", "menstrual", "menstruation",
                     "painful period", "masik", "mahwari"],
        "answer": (
            "**Menstrual health - what is normal and what helps**\n"
            "- Period pain: hot water bag on the lower belly, warm drinks, rest.\n"
            "- **Tablet for adults:** Paracetamol 500 mg - 1 tablet after "
            "food for pain (max 4/day).\n"
            "- Change cloth or pad every 4-6 hours; dry cloths in sunlight. "
            "Free sanitary pads at PHC or Anganwadi.\n\n"
            "**See a doctor if:** bleeding more than 7 days, changing every "
            "1-2 hours, severe pain that stops daily work, bleeding between "
            "periods, or no period for 3+ months."
        ),
    },
    {
        "topic": "pregnancy care",
        "keywords": ["pregnancy", "pregnant", "garbhini", "garbham"],
        "answer": (
            "**Pregnancy care basics**\n"
            "- Register at the PHC or Anganwadi for free checkups and the "
            "YSR Asara maternity benefit.\n"
            "- Take iron and folic acid tablets daily as given at the PHC.\n"
            "- Eat an extra meal a day; include greens, eggs, milk, dal.\n"
            "- At least 4 checkups; deliver in a hospital, not at home.\n"
            "- Do NOT take any tablet without the doctor's advice.\n\n"
            "**Go to the hospital urgently if:** bleeding, severe headache "
            "with swelling of hands or face, reduced baby movement, fits, "
            "or labour pains before 8 months."
        ),
    },
    {
        "topic": "child health",
        "keywords": ["child", "baby", "kid", "infant", "pillala", "bachche"],
        "answer": (
            "**Child health basics**\n"
            "- **Do NOT give adult tablets to small children - doses differ.**\n"
            "- For fever in a child: ORS, keep cool, only child paracetamol "
            "(syrup or drops) as per weight on the packet.\n"
            "- Keep vaccinations up to date at the PHC or ASHA centre - free.\n"
            "- Breastfeed exclusively for the first 6 months.\n\n"
            "**Go to the doctor same day if:** the child is under 1 year, "
            "refuses feeds, has very low urine, is unusually sleepy, has "
            "fast breathing, or fever above 100 F. Never wait with small babies."
        ),
    },
    {
        "topic": "stress",
        "keywords": ["stress", "anxiety", "tension", "depression", "sad",
                     "sleep", "insomnia", "ottidi", "nidra"],
        "answer": (
            "**Feeling stressed - what can help**\n"
            "- Deep breathing: in 4 counts, hold 4, out 4 - repeat 10 "
            "times, twice a day.\n"
            "- A 20-minute walk, talking to family, and regular sleep help.\n"
            "- Avoid alcohol and tobacco to cope - they make it worse.\n\n"
            "**Free government support:** call Tele-MANAS **14416** (24x7, "
            "Telugu available) or KIRAN **1800-599-0019**.\n\n"
            "**See a doctor if:** stress affects daily work for more than "
            "2 weeks, or there are thoughts of self-harm - call 14416 or "
            "112 right away."
        ),
    },
    {
        "topic": "nutrition",
        "keywords": ["nutrition", "diet", "healthy food", "weight",
                     "vitamin", "protein", "poshana"],
        "answer": (
            "**Healthy eating on a small budget**\n"
            "- Every plate: rice + dal or egg + a vegetable + curd.\n"
            "- Cheap protein: eggs, dal, groundnuts, soya chunks, milk.\n"
            "- Cheap iron: greens, jaggery, dates.\n            "- Limit deep-fried food, excess salt, and sugary drinks.\n"
            "- Children under 5 and pregnant women get free nutrition at "
            "the Anganwadi centre - collect it."
        ),
    },
    {
        "topic": "worms",
        "keywords": ["worms", "worm", "intestinal worm", "kirmulu", "keede"],
        "answer": (
            "**Worm infection - what to do**\n"
            "- Signs: stomach pain, anal itching at night, weakness, poor "
            "appetite, anaemia in children.\n"
            "- **Albendazole 400 mg single chewable tablet** is given FREE "
            "twice a year on National Deworming Day at schools and "
            "Anganwadi centres.\n"
            "- Not for pregnant women in the first trimester - ask the PHC.\n\n"
            "**Prevention:** wash hands with soap before eating, wash "
            "vegetables well, wear slippers, drink boiled or filtered water."
        ),
    },
]


def search_kb(query):
    """Return (score, entry) for best keyword match, or (0, None)."""
    q = query.lower()
    best_score, best_entry = 0, None
    for entry in KB_ENTRIES:
        score = 0
        for kw in entry["keywords"]:
            if kw.lower() in q:
                score += 2 if len(kw) > 4 else 1
        if score > best_score:
            best_score, best_entry = score, entry
    return best_score, best_entry
