from scapy.all import sniff, IP, TCP

import subprocess

import logging





logging.basicConfig(filename='firewall.log', level=logging.INFO, format='%(asctime)s - %(message)s')



# Whitelist rules

Allowed_IPS = ["192.168.1.4"]  # Example of allowed IPs

Allowed_Ports = ["80", "443"]  # Example of allowed ports



# Function to block traffic using iptables command 

def drop_packet(ip):

    try:

        subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"], check=True)

        logging.warning(f"Dropped traffic from IP: {ip}")

        print(f"Blocked traffic from IP: {ip}")

    except subprocess.CalledProcessError as e:

        logging.error(f"Failed to block IP {ip}: {e}")

        print(f"Failed to block IP {ip}: {e}")



# Packet handler function

def packet_handler(packet):

    if IP in packet and TCP in packet:

        src_ip = packet[IP].src

        dst_ip = packet[IP].dst

        dst_port = str(packet[TCP].dport)



        # Check IP and port against whitelist

        if src_ip not in Allowed_IPS or dst_port not in Allowed_Ports:

            logging.warning(f"Unauthorized traffic detected: {src_ip} -> {dst_ip} on port {dst_port}")

            print(f"Unauthorized traffic detected: {src_ip} -> {dst_ip} on port {dst_port}")

            drop_packet(src_ip)  # Block unauthorized IP

        else:

            logging.info(f"Allowed traffic: {src_ip} -> {dst_ip} on port {dst_port}")

            print(f"Allowed traffic: {src_ip} -> {dst_ip} on port {dst_port}")



# Start sniffing packets

print("Starting the firewall...")

sniff(prn=packet_handler, store=0)

