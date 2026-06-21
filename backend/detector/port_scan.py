from collections import defaultdict
from datetime import datetime
from datetime import timedelta

from services.alert_manager import raise_alert
from services.threat_score import calculate_severity

PORT_THRESHOLD = 3
TIME_WINDOW = 30

scan_tracker = defaultdict(list)


def detect_port_scan(
    src_ip,
    dst_port
):

    now = datetime.now()

    scan_tracker[src_ip].append(
        (
            now,
            dst_port
        )
    )

    cutoff = now - timedelta(
        seconds=TIME_WINDOW
    )

    scan_tracker[src_ip] = [

        (t, p)

        for t, p
        in scan_tracker[src_ip]

        if t >= cutoff
    ]

    unique_ports = {

        p

        for t, p
        in scan_tracker[src_ip]
    }

    count = len(unique_ports)

    if count >= PORT_THRESHOLD:

        severity = calculate_severity(
            count
        )

        raise_alert(
            "PORT_SCAN",
            severity,
            src_ip,
            f"{count} unique ports scanned within {TIME_WINDOW} seconds"
        )

        scan_tracker[src_ip].clear()