---
Name: NPS
Description: NPS is a Chinese-developed intranet-penetration proxy server with a web management console. A server component (nps) is installed on an operator-controlled host, and a client component (npc) run on the target network registers with the server and exposes configured TCP/UDP/HTTP(S)/SOCKS5 tunnels, all managed through the web UI rather than command-line flags.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: ./nps install && nps start
    Description: Installs and starts the NPS server as a system service on the operator's host, exposing the web management console (default port 8080) and the client bridge port (default 8024).
    Usecase: Operator side of the proxy.
    Category: access
    Privileges: Administrator/root
    OperatingSystem: Windows, Linux, MacOS

  - Command: ./npc -server=<SERVER_IP>:8024 -vkey=<CLIENT_KEY>
    Description: Connects a client on the target network to the NPS server using a key generated in the web console, after which tunnels configured in the console become active.
    Usecase: Exposing internal services, or pivoting into the internal network, through the operator's NPS server.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: nps
  - Filename: npc
  - Filename: npc.exe
  - Path: /etc/nps (Linux/macOS server configuration directory)
Detection:
  - Command: Execution of npc with -server and -vkey arguments, or nps with install/start arguments.
  - Command: Outbound connections to an uncategorized host on TCP 8024 (default NPS bridge port), or installation of an nps/npc system service.
Resources:
  - Link: https://github.com/ehang-io/nps
  - Link: https://ehang-io.github.io/nps/
---
