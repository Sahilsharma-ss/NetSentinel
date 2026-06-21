def calculate_severity(port_count):

    if port_count >= 100:
        return "CRITICAL"

    if port_count >= 50:
        return "HIGH"

    if port_count >= 20:
        return "MEDIUM"

    return "LOW"