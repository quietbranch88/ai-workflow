import re


def check(text):
    warnings = []
    for field in ("Observable", "Environment", "Verify"):
        pattern = r"\s*(?:-\s+)?" + field + r":[ \t]*(.*)"
        values = [match.group(1) for line in text.splitlines()
                  if (match := re.fullmatch(pattern, line, re.IGNORECASE))]
        if not any(value.strip() for value in values):
            warnings.append(field)
    return 0, warnings
