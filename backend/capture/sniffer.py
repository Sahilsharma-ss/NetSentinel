from scapy.all import sniff
from scapy.layers.inet import IP
from scapy.layers.inet import TCP

from database.db import save_packet
from detector.port_scan import detect_port_scan


def process_packet(packet):

    if IP not in packet:
        return

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst

    protocol = "IP"

    src_port = None
    dst_port = None
    flags = None

    if TCP in packet:

        protocol = "TCP"

        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

        flags = str(
            packet[TCP].flags
        )

        print(
            f"SRC={src_ip} "
            f"DST={dst_ip} "
            f"SPORT={src_port} "
            f"DPORT={dst_port} "
            f"FLAGS={flags}"
        )

        if flags == "S":

            detect_port_scan(
                src_ip,
                dst_port
            )

    save_packet(
        src_ip,
        dst_ip,
        src_port,
        dst_port,
        protocol,
        flags
    )


def start_sniffer():

    print("[+] NetSentinel Started")

    sniff(
        iface="eth0",
        prn=process_packet,
        store=False
    )