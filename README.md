
# Python-Based Host Firewall

## credits : 
 - Authore : Oussama Abd el ilah Belaiche

## Overview

This project implements a simple host-based firewall using Python and Linux iptables to manage network traffic. It uses a whitelist approach, where only specified IPs and ports are allowed, and others are blocked.

## Features

- Monitors incoming TCP/IP traffic using scapy.
- Logs unauthorized access attempts.
- Dynamically adds iptables rules to block packets from unauthorized sources.
- Customizable whitelist of IPs and ports.

## Installation

### Requirements

- Python 3.6+
- Required Python libraries:
  - scapy
  - logging
  - subprocess
- Linux system with iptables installed.

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Oussama-A-Belaiche/firewall-from-scratch
   cd firewall-from-scratch
   cd Firewall-python-code
   ```

2. Install required Python libraries:

   ```bash
   pip install scapy
   ```

3. Ensure Python script has execution permissions:

   ```bash
   chmod +x Firewall-code.py
   ```

4. Run the script with root privileges:

   ```bash
   sudo python Firewall-code.py
   ```

## Configuration

### Whitelist

The whitelist is defined in the script:

- Allowed IP header:

  ```python
  Allowed_IPS_header = "192"  # Local communication prefix
  ```

- Specific Allowed IPs:

  ```python
  Allowed_IPS = ["192.168.1.4"]
  ```

- Allowed Ports:

  ```python
  Allowed_Ports = ["80", "443"]
  ```

Modify these lists based on your requirements before running the script.

## How It Works

### Packet Monitoring:

- The script uses scapy to sniff incoming packets.

### Packet Inspection:

- Extracts source IP, destination IP, and ports from each packet.
- Checks if the packet matches the whitelist rules.

### Packet Blocking:

- Unauthorized packets are dropped using iptables commands executed via the subprocess library.

### Logging:

- Logs all blocked packets in a file named `firewall.log`.

## Usage

- Run the script:

  ```bash
  sudo python Firewall-code.py
  ```

- Monitor logs:

  ```bash
  tail -f firewall.log
  ```

- Modify the whitelist as needed and restart the script to apply new rules.

## Limitations

- Designed as a host-based firewall and not suitable for managing traffic across multiple systems.
- Requires administrative privileges to modify iptables rules.
- Does not support advanced traffic analysis or stateful inspection.

## Future Enhancements

- Add support for dynamic rule updates without restarting the script.
- Implement a graphical user interface (GUI) for easier rule management.
- Extend support for protocols beyond TCP/IP.


## Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.
```
