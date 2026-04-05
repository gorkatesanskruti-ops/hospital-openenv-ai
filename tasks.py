def get_task(level):

    if level == "easy":
        return {
            "patients_waiting": 10,
            "critical_patients": 1,
            "available_beds": 10,
            "icu_beds": 2,
            "doctors_available": 3
        }

    elif level == "medium":
        return {
            "patients_waiting": 25,
            "critical_patients": 5,
            "available_beds": 8,
            "icu_beds": 2,
            "doctors_available": 2
        }

    elif level == "hard":
        return {
            "patients_waiting": 50,
            "critical_patients": 10,
            "available_beds": 5,
            "icu_beds": 1,
            "doctors_available": 1
        }

    else:
        return {
            "patients_waiting": 15,
            "critical_patients": 3,
            "available_beds": 8,
            "icu_beds": 2,
            "doctors_available": 2
        }