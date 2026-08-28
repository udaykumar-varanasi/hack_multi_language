"""Knowledge base — Rural Health Assistant. Safe, non-diagnostic content."""

DISCLAIMER = (
    "⚕️ This assistant provides general health information only. It does NOT "
    "diagnose, prescribe, or replace a doctor. For urgent problems call "
    "108 / 112 immediately."
)

EMERGENCY_CONTACTS = {
    "Ambulance": "108",
    "National Emergency": "112",
    "Health Helpline": "104",
    "Tele-MANAS Mental Health": "14416",
    "KIRAN Crisis Line": "1800-599-0019",
}

GLOBAL_EMERGENCY_KEYWORDS = [
    "unconscious", "unresponsive", "not breathing", "severe bleeding",
    "seizure", "convulsion", "chest pain", "heart attack", "stroke",
    "snake bite", "snakebite", "poisoning", "suicide", "kill myself",
    "end my life", "self harm", "overdose", "electric shock", "drowning",
    "severe burn", "heat stroke", "heatstroke", "pesticide poisoning",
    "heavy bleeding", "can't breathe", "cannot breathe", "severe injury",
    "paralysis", "fits",
]

KNOWLEDGE_BASE = [
    {
        "topic": "fever",
        "title": "Fever",
        "content": (
            "Fever is usually the body's natural response to infection.\n\n"
            "WHAT TO DO:\n"
            "1. Rest and drink plenty of fluids (water, ORS, soups).\n"
            "2. Wear light clothing; keep the room airy.\n"
            "3. Paracetamol may be taken for comfort as per the label dosage.\n"
            "4. Sponge with lukewarm (NOT cold) water if fever is high.\n\n"
            "SEE A DOCTOR IF:\n"
            "- Fever lasts more than 3 days\n"
            "- Fever with rash, stiff neck, severe headache or confusion\n"
            "- In malaria/dengue areas: fever with chills needs a blood test the same day"
        ),
        "keywords": ["fever", "temperature", "jwaram", "bukhar", "hot body"],
        "urgent_flags": [],
        "regex_flags": [r"\bfever\b.*\b(fits|convulsion|seizure|unconscious|rash|stiff neck)\b"],
    },
    {
        "topic": "cough_cold",
        "title": "Cough and Cold",
        "content": (
            "Most coughs and colds are viral and settle in 5-7 days.\n\n"
            "WHAT TO DO:\n"
            "1. Drink warm fluids; steam inhalation helps a blocked nose.\n"
            "2. Rest well; avoid smoke and dust.\n"
            "3. Honey with warm water soothes the throat (not for babies under 1 year).\n\n"
            "SEE A DOCTOR IF:\n"
            "- Cough lasts more than 2 weeks (TB screening advised)\n"
            "- Blood in sputum, high fever, weight loss\n"
            "- Breathing difficulty or chest pain"
        ),
        "keywords": ["cough", "cold", "khansi", "sore throat", "runny nose", "jalu"],
        "urgent_flags": ["coughing blood"],
        "regex_flags": [r"\bcough\b.*\b(blood|breathless)\b"],
    },
    {
        "topic": "diarrhoea",
        "title": "Diarrhoea and Dehydration",
        "content": (
            "Dehydration — not the germs — is the danger of diarrhoea.\n\n"
            "WHAT TO DO:\n"
            "1. ORS is the most important treatment: drink after every loose stool.\n"
            "2. Continue normal food and breastfeeding — do not starve.\n"
            "3. Zinc for 14 days helps children recover faster.\n"
            "4. Wash hands with soap before eating and after the toilet.\n\n"
            "GO TO HOSPITAL NOW IF:\n"
            "- Blood in stool, no urine for 8+ hours, sunken eyes\n"
            "- Skin pinch settles slowly, extreme thirst, drowsiness\n"
            "- More than 5 villagers affected (possible outbreak — call 104)"
        ),
        "keywords": ["diarrhoea", "diarrhea", "loose motion", "dast", "vomiting", "ors"],
        "urgent_flags": ["blood in stool"],
        "regex_flags": [],
    },
    {
        "topic": "dengue_malaria",
        "title": "Dengue and Malaria",
        "content": (
            "PREVENTION:\n"
            "- Empty and scrub water containers weekly; cover all tanks.\n"
            "- Use mosquito nets; full-sleeve clothes at dawn and dusk.\n\n"
            "SUSPICION:\n"
            "- Dengue: high fever with severe body pain, pain behind the eyes.\n"
            "- Malaria: shaking chills followed by high fever in cycles.\n"
            "- Get a blood test at the PHC the SAME day.\n\n"
            "DANGER SIGNS (hospital now): bleeding gums, black stools, severe\n"
            "stomach pain, persistent vomiting, no urine, drowsiness.\n\n"
            "IMPORTANT: No aspirin or ibuprofen for dengue — only paracetamol."
        ),
        "keywords": ["dengue", "malaria", "mosquito", "platelet", "dommu"],
        "urgent_flags": ["bleeding gums", "black stool"],
        "regex_flags": [],
    },
    {
        "topic": "headache",
        "title": "Headache",
        "content": (
            "COMMON CAUSES: tension, dehydration, eye strain, missed meals, heat.\n\n"
            "WHAT TO DO:\n"
            "1. Rest in a quiet, dim room; drink water.\n"
            "2. A cold cloth on the forehead may help.\n"
            "3. Paracetamol may be taken as per label dosage.\n\n"
            "SEE A DOCTOR IF:\n"
            "- Sudden worst-ever headache; headache with vomiting and stiff neck\n"
            "- Headache with fever, weakness, vision problems or confusion"
        ),
        "keywords": ["headache", "head pain", "tala noppi", "sir dard", "migraine"],
        "urgent_flags": ["worst headache"],
        "regex_flags": [r"\bheadache\b.*\b(fits|unconscious|paralysis|stiff neck)\b"],
    },
    {
        "topic": "pregnancy",
        "title": "Pregnancy Care",
        "content": (
            "DO:\n"
            "- Register at the nearest PHC in the first trimester.\n"
            "- Attend all ANC checkups; take iron-folic acid tablets daily.\n"
            "- Eat an extra meal a day; iron-rich foods (greens, ragi, eggs).\n"
            "- Plan delivery at a health facility (JSY cash benefit applies).\n\n"
            "DANGER SIGNS (call 102/108 IMMEDIATELY):\n"
            "- Bleeding, severe headache with blurred vision, fits\n"
            "- Swelling of face and hands, reduced baby movements\n"
            "- Labour before 8 months, water breaking without labour"
        ),
        "keywords": ["pregnancy", "pregnant", "garbhini", "anc", "delivery", "maternity"],
        "urgent_flags": ["bleeding during pregnancy", "fits during pregnancy"],
        "regex_flags": [],
    },
    {
        "topic": "childcare",
        "title": "Child Health",
        "content": (
            "BASICS:\n"
            "- Exclusive breastfeeding for the first 6 months.\n"
            "- Complete the immunization schedule on time.\n"
            "- Weigh the child monthly at the Anganwadi.\n\n"
            "DANGER SIGNS (hospital now):\n"
            "- Refusing feeds, unusually sleepy, difficult breathing\n"
            "- Fever with fits, less than 3 wet diapers a day\n"
            "- Any fever in a baby under 3 months\n\n"
            "NEVER give aspirin to children."
        ),
        "keywords": ["child", "baby", "infant", "bidda", "baccha", "breastfeeding"],
        "urgent_flags": ["refusing feeds"],
        "regex_flags": [],
    },
    {
        "topic": "bites_stings",
        "title": "Bites and Stings",
        "content": (
            "SNAKE BITE (call 108 immediately):\n"
            "1. Keep the victim CALM and STILL — movement spreads venom.\n"
            "2. Remove rings/watches; immobilise the limb at heart level.\n"
            "3. Do NOT cut, suck, apply tourniquets, ice, herbs or cow dung.\n"
            "4. Note the snake's appearance from a distance; never chase it.\n"
            "5. Anti-snake-venom works best within 4 hours — reach hospital fast.\n\n"
            "DOG/MONKEY BITE:\n"
            "- Wash with soap under running water for 15 minutes.\n"
            "- Anti-rabies vaccine must start the SAME DAY (rabies is fatal once symptoms begin).\n\n"
            "SCORPION STING:\n"
            "- Wash area, apply a cold pack; stings in children need hospital care."
        ),
        "keywords": ["snake", "pamu", "dog bite", "kukka", "scorpion", "bite", "sting", "venom"],
        "urgent_flags": ["snake bite", "snakebite", "dog bite", "scorpion sting"],
        "regex_flags": [],
    },
    {
        "topic": "heat_stroke",
        "title": "Heat Stroke (Sunstroke)",
        "content": (
            "Heat stroke is LIFE THREATENING. Signs: temperature above 40 C,\n"
            "hot dry skin or profuse sweating, confusion, seizures, fainting.\n\n"
            "IMMEDIATE ACTION (call 108):\n"
            "1. Move the person to shade; remove excess clothing.\n"
            "2. Cool aggressively — wet cloths on neck, armpits, groin; fan continuously.\n"
            "3. If fully conscious, give ORS/water in sips — NEVER to an unconscious person.\n"
            "4. Do NOT give paracetamol for heat stroke.\n\n"
            "PREVENTION: work before 11am and after 4pm in summer, drink water\n"
            "every 20 minutes, cover the head, take salt with food."
        ),
        "keywords": ["heat stroke", "heatstroke", "sunstroke", "endala", "garmi", "loo", "summer"],
        "urgent_flags": ["heat stroke", "heatstroke"],
        "regex_flags": [],
    },
    {
        "topic": "pesticide",
        "title": "Pesticide Poisoning",
        "content": (
            "SIGNS: excessive sweating, drooling, pinpoint pupils, vomiting,\n"
            "cramps, trembling, breathing difficulty, confusion, seizures.\n\n"
            "IMMEDIATE ACTION (call 108):\n"
            "1. Move the victim away from the chemical to fresh air.\n"
            "2. Remove contaminated clothes; wash skin with soap and water for 15 minutes.\n"
            "3. Flush eyes with clean water for 15 minutes if affected.\n"
            "4. Do NOT induce vomiting if the victim is drowsy or convulsing.\n"
            "5. Carry the pesticide container/label to the hospital.\n\n"
            "PREVENTION: never spray against the wind, never store pesticides\n"
            "in drink bottles, never eat or smoke while spraying."
        ),
        "keywords": ["pesticide", "spray", "poison", "chemical", "visham", "insecticide"],
        "urgent_flags": ["pesticide poisoning", "swallowed pesticide"],
        "regex_flags": [],
    },
    {
        "topic": "drowning",
        "title": "Drowning",
        "content": (
            "RESCUE:\n"
            "1. Reach the victim with a stick, rope or tube — do NOT jump in unless trained.\n"
            "2. Once out, lay the person flat and check breathing for 10 seconds.\n"
            "3. Not breathing: start CPR — 30 chest compressions in the centre of the chest\n"
            "(5-6 cm deep, 100-120 per minute); continue until help arrives.\n"
            "4. Do NOT hang the person upside down to remove water — it wastes minutes.\n"
            "5. Even after recovery, a hospital check-up is mandatory (delayed lung\n"
            "complications can occur within 24-72 hours).\n\n"
            "PREVENTION: fence open wells; supervise children near ponds constantly."
        ),
        "keywords": ["drowning", "well", "pond", "neellu", "water accident"],
        "urgent_flags": ["drowning", "fell in well"],
        "regex_flags": [],
    },
    {
        "topic": "farmer_distress",
        "title": "Farmer Distress & Mental Health",
        "content": (
            "Debt, crop failure and isolation can feel unbearable — but help is FREE.\n\n"
            "HELP LINES (24x7, free):\n"
            "- KIRAN: 1800-599-0019\n"
            "- Tele-MANAS: 14416\n\n"
            "WHAT HELPS:\n"
            "1. Talking to one trusted person reduces risk immediately.\n"
            "2. Crop insurance (PMFBY), loan rescheduling and relief exist —\n"
            "   ask the agriculture officer.\n"
            "3. Warning signs in a loved one: giving away possessions, talking\n"
            "   about ending life, sudden calm after depression — do NOT leave\n"
            "   them alone, remove pesticides/weapons, call KIRAN together.\n\n"
            "You are not alone — lakhs of farmers have received help and recovered."
        ),
        "keywords": ["stress", "depression", "mental health", "debt", "crop loss", "suicide"],
        "urgent_flags": ["suicide", "kill myself", "end my life", "self harm"],
        "regex_flags": [],
    },
    {
        "topic": "nutrition",
        "title": "Nutrition & Anaemia",
        "content": (
            "ANAEMIA (weakness, pale eyes/nails, tiredness) is very common in\n"
            "rural women and children.\n\n"
            "DO:\n"
            "- Iron-rich foods: greens, ragi, jaggery, dates, eggs, lentils.\n"
            "- Take iron-folic acid tablets from the Anganwadi/PHC (free).\n"
            "- Vitamin C (lemon, amla, guava) with meals improves absorption.\n"
            "- Avoid tea/coffee WITH meals — it blocks iron absorption.\n\n"
            "SEE A DOCTOR IF: severe tiredness, breathlessness on light work,\n"
            "or pale palms — a simple haemoglobin blood test confirms it."
        ),
        "keywords": ["nutrition", "anaemia", "anemia", "weakness", "diet", "iron", "kamzori"],
        "urgent_flags": [],
        "regex_flags": [],
    },
]
