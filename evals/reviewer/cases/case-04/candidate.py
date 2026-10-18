def check(text):
    warnings = []
    for field in ("Observable", "Environment", "Verify"):
        if field.lower() + ":" not in text.lower():
            warnings.append(field)
    return 0, warnings
