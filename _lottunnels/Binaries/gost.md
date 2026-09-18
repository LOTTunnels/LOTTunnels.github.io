---
Name: GOST
Description: GOST (GO Simple Tunnel) is a self-hosted, multi-protocol tunneling and proxy tool bundled in a single Go executable that acts as both client and server. It supports SOCKS5/HTTP proxying, TCP/UDP port forwarding and chained (multi-hop) tunnels over transports such as TLS, WebSocket, KCP and QUIC. Because the relay server is operator-run, there is no vendor domain to block. It is heavily abused for pivoting and C2 relaying, observed with Cadet Blizzard/APT44, MirrorFace, Hydrochasma and BlackCat/BlackMatter ransomware, and is named in CISA advisories on Russian military cyber actors.
Author: cyberbuff
Created: 2026-09-17
Commands:
  - Command: gost -L=:8080
    Description: Starts a local proxy listener (SOCKS5/HTTP auto-detected) on port 8080, providing a proxy entry point into the network from the host.
    Usecase: Standing up a proxy pivot on a compromised host.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: gost -L=rtcp://:6000/127.0.0.1:22
    Description: Publishes a remote TCP forward so that connections to port 6000 on the GOST server are forwarded to a local service such as SSH (22), reaching a host behind NAT or a firewall.
    Usecase: Reaching an internal service through a reverse tunnel.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: gost -L=socks5://:1080 -F=relay+tls://<SERVER>:443
    Description: Runs a local SOCKS5 proxy that chains outbound through an operator-controlled GOST relay over TLS, tunneling traffic to blend with ordinary HTTPS and bypass egress controls.
    Usecase: Establishing a chained SOCKS pivot to an operator-controlled relay.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Custom_Domain_Supported: True
Full_Path:
  - Path: Downloaded/Installed gost binary (single executable acting as client and server), executed anywhere on the system.
Detection:
  - Command: 'Execution of the gost binary, particularly with -L listen and -F forward-chain arguments (e.g. rtcp://, relay+tls://, socks5://).'
Resources:
  - Link: https://github.com/ginuerzh/gost
  - Link: https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/
  - Link: https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html
  - Link: https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/hydrochasma-asia-medical-shipping-intelligence-gathering
Acknowledgement:
  - Person: cyberbuff
---
