import math

FACILITIES = [
    {
        "name": "PHC Tekkali",
        "type": "Primary Health Centre",
        "services": "General OP, Emergency, Maternity, Lab, Pharmacy",
        "phone": "104",
        "lat": 18.6063, "lon": 84.2460,
        "tags": ["emergency", "maternity", "general", "phc", "lab",
                 "vaccination"],
    },
    {
        "name": "Area Hospital, Srikakulam",
        "type": "Area Hospital",
        "services": "24x7 Emergency, Surgery, Pediatrics, Blood bank",
        "phone": "08942-224455",
        "lat": 18.2949, "lon": 83.8938,
        "tags": ["emergency", "pediatric", "surgery", "maternity",
                 "hospital"],
    },
    {
        "name": "Govt General Hospital, Srikakulam",
        "type": "District Hospital",
        "services": "All specialties, 24x7 Emergency, ICU, Ambulance",
        "phone": "08942-224455",
        "lat": 18.3010, "lon": 83.8930,
        "tags": ["emergency", "icu", "specialist", "surgery", "maternity",
                 "pediatric"],
    },
    {
        "name": "PHC Santabommali",
        "type": "Primary Health Centre",
        "services": "General OP, Emergency, Lab, Vaccination",
        "phone": "104",
        "lat": 18.5487, "lon": 84.1583,
        "tags": ["general", "phc", "lab", "vaccination", "emergency"],
    },
    {
        "name": "PHC Voppangi",
        "type": "Primary Health Centre",
        "services": "General OP, Maternity, Pharmacy",
        "phone": "104",
        "lat": 18.6550, "lon": 84.3100,
        "tags": ["general", "phc", "maternity"],
    },
    {
        "name": "Community Health Centre, Palasa",
        "type": "Community Health Centre",
        "services": "24x7 Emergency, Surgery, Maternity, Lab",
        "phone": "104",
        "lat": 18.7747, "lon": 84.4110,
        "tags": ["emergency", "surgery", "maternity", "general", "lab"],
    },
]


def _haversine_km(lat1, lon1, lat2, lon2):
    r = 6371.0
    p1 = math.radians(lat1)
    p2 = math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = (math.sin(dp / 2) ** 2
         + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2)
    return 2 * r * math.asin(math.sqrt(a))


def search_facilities(lat, lon, need="Any", max_km=50):
    results = []
    for f in FACILITIES:
        d = _haversine_km(lat, lon, f["lat"], f["lon"])
        if d > max_km:
            continue
        if need != "Any" and need not in f["tags"]:
            continue
        g = dict(f)
        g["distance_km"] = d
        results.append(g)
    results.sort(key=lambda x: x["distance_km"])
    return results
