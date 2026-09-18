---
Name: frp
Description: frp (Fast Reverse Proxy) is a self-hosted reverse proxy that exposes local HTTP, TCP and UDP services behind NAT or a firewall to the internet through an attacker-controlled frps server. Because both the frps server and frpc client are operator-run, there is no vendor domain to block. It is one of the most widely abused tunneling tools in real intrusions, observed with Volt Typhoon/VOLTZITE, Cobalt Mirage, LightBasin and BIOPASS RAT, and is called out in the NSA/CISA "Living off the Land" guidance.
Author: cyberbuff
Created: 2026-09-17
Commands:
    - Command: frpc -c frpc.ini
      Description: Starts the frp client using an frpc.ini/frpc.toml configuration that points at an operator-controlled frps server, exposing configured local services through it.
      Usecase: Quick execution of frp to expose local services through a remote frps server.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS

    - Command: frpc tcp --server-addr <FRPS_IP> --server-port 7000 --local-port 22 --remote-port 6000
      Description: Forwards a public port (6000) on the frps server to a local service such as SSH (22), giving remote access to a host behind NAT or a firewall.
      Usecase: Maintaining remote access to an internal host.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS

    - Command: frpc stcp --role visitor --server-addr <FRPS_IP> --sk <SECRET>
      Description: Connects to a secret TCP (stcp) tunnel published by another frpc client via the shared frps server, reaching an internal service without opening a public port.
      Usecase: Reaching an internal service through a private frp tunnel.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS
Custom_Domain_Supported: True
Full_Path:
    - Path: Downloaded/Installed frpc (client) and frps (server) binaries, executed anywhere on the system, typically with an frpc.ini/frpc.toml configuration file.
Detection:
    - Command: Execution of the frpc or frps binaries, presence of frpc.ini/frpc.toml/frps.ini configuration files, or the default frps control port 7000.
Resources:
    - Link: https://github.com/fatedier/frp
    - Link: https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF
    - Link: https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf
    - Link: https://hub.dragos.com/hubfs/116-Datasheets/Dragos_IntelBrief_VOLTZITE_FINAL.pdf
---
