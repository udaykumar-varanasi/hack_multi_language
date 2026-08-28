"""Nearby healthcare locator — real coordinates, haversine distances,
emergency-priority sorting. Swap search_facilities() internals for a
Places/Overpass API later; signature and return shape stay identical."""

from __future__ import annotations

from math import radians, sin, cos, asin, sqrt

SAMPLE_DATASET = True  # surfaced in the UI as "demo data"

DEMO_ORIGIN = (18.6200, 84.0500)  # Tekkali, AP — fallback origin

FACILITIES = [
    {"name": "Government PHC, Tekkali", "type": "PHC",
     "lat": 18.6267, "lon": 84.0464, "phone": "08947-232244",
     "services": "General OPD, Maternal care, Immunization",
     "is_24x7": False, "has_emergency": False},
    {"name": "AITAM Community Health Camp", "type": "Camp/Clinic",
     "lat": 18.6301, "lon": 84.0512, "phone": "08947-232345",
     "services": "General checkups, First aid",
     "is_24x7": False, "has_emergency": True},
    {"name": "Srikakulam Govt General Hospital", "type": "Hospital",
     "lat": 18.2949, "lon": 83.8938, "phone": "08942-240333",
     "services": "Emergency, Surgery, Specialist care, Maternity",
     "is_24x7": True, "has_emergency": True},
    {"name": "Area Hospital, Palasa", "type": "Hospital",
     "lat": 18.7734, "lon": 84.4105, "phone": "08945-244233",
     "services": "General medicine, Pediatrics, Emergency",
     "is_24x7": True, "has_emergency": True},
    {"name": "Rural Sub-Center, Naupada", "type": "Sub-Center",
     "lat": 18.5560, "lon": 84.0230, "phone": "08947-235100",
     "services": "Immunization, Basic maternal care",
     "is_24x7": False, "has_emergency": False},
]


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    lat1, lon1, lat2, lon2 = map(radians, (lat1, lon1, lat2, lon2))
    a = sin((lat2 - lat1) / 2) ** 2 + cos(lat1) * cos(lat2) * sin((lon2 - lon1) / 2) ** 2
    return round(6371.0 * 2 * asin(sqrt(a)), 1)


def search_facilities(query: str = "", max_results: int = 5,
                      user_coords=None, urgent: bool = False):
    """
    Returns a LIST of facility dicts. distance_km is ALWAYS present:
    real haversine from user_coords if given, else from the demo origin.
    """
    origin = DEMO_ORIGIN
    if user_coords and len(user_coords) == 2:
        try:
            origin = (float(user_coords[0]), float(user_coords[1]))
        except (TypeError, ValueError):
            origin = DEMO_ORIGIN

    matched = bool(query.strip())
    results = [dict(f) for f in FACILITIES]

    if matched:
        q = query.strip().lower()
        results = [
            f for f in results
            if q in f["name"].lower()
            or q in f["type"].lower()
            or any(q in s.strip().lower() for s in f["services"].split(","))
        ]
        if not results:
            results = [dict(f) for f in FACILITIES]
            matched = False

    for f in results:
        f["distance_km"] = haversine_km(origin[0], origin[1], f["lat"], f["lon"])

    if urgent:
        results.sort(key=lambda f: (not f["is_24x7"], not f["has_emergency"],
                                    f["distance_km"]))
    else:
        results.sort(key=lambda f: f["distance_km"])

    return results[:max_results]
