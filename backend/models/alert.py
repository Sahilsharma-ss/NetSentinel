class Alert:

    def __init__(
        self,
        alert_type,
        severity,
        source_ip,
        details
    ):
        self.alert_type = alert_type
        self.severity = severity
        self.source_ip = source_ip
        self.details = details