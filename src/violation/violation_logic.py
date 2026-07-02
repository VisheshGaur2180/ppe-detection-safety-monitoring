def check_violation(detections):
    persons = []
    helmets = []

    for det in detections:
        if det["label"] == "person":
            persons.append(det)
        if det["label"] == "helmet":
            helmets.append(det)

    violations = []

    if len(persons) > len(helmets):
        violations.append("Helmet Missing")

    return violations