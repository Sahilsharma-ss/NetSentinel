from database.db import save_alert


def raise_alert(
    alert_type,
    severity,
    source_ip,
    details
):

    print("\n====================")
    print("[ALERT]")
    print(f"TYPE: {alert_type}")
    print(f"SEVERITY: {severity}")
    print(f"SOURCE: {source_ip}")
    print(details)
    print("====================\n")

    save_alert(
        alert_type,
        severity,
        source_ip,
        details
    )