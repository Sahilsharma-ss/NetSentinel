import sqlite3

conn = sqlite3.connect(
    "netsentinel.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS packets(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    src_ip TEXT,
    dst_ip TEXT,
    src_port INTEGER,
    dst_port INTEGER,
    protocol TEXT,
    flags TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    alert_type TEXT,
    severity TEXT,
    source_ip TEXT,
    details TEXT
)
""")

conn.commit()


def save_packet(
    src_ip,
    dst_ip,
    src_port,
    dst_port,
    protocol,
    flags
):

    cursor.execute(
        """
        INSERT INTO packets(
            src_ip,
            dst_ip,
            src_port,
            dst_port,
            protocol,
            flags
        )
        VALUES(?,?,?,?,?,?)
        """,
        (
            src_ip,
            dst_ip,
            src_port,
            dst_port,
            protocol,
            flags
        )
    )

    conn.commit()


def save_alert(
    alert_type,
    severity,
    source_ip,
    details
):

    cursor.execute(
        """
        INSERT INTO alerts(
            alert_type,
            severity,
            source_ip,
            details
        )
        VALUES(?,?,?,?)
        """,
        (
            alert_type,
            severity,
            source_ip,
            details
        )
    )

    conn.commit()