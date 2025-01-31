---
Name: chisel
Description: Chisel is a fast TCP/UDP tunnel, transported over HTTP, secured via SSH. Single executable including both client and server. Written in Go (golang). Chisel is mainly useful for passing through firewalls, though it can also be used to provide a secure endpoint into a network.
Author: Dan O'Day
Created: 2025-01-31
Commands:
  - Command: chisel client <SERVER_IP>:<SERVER_PORT> <LOCAL_PORT>:<TARGET_IP>:<TARGET_PORT>
    Description: Set up reverse tunneling.
    Usecase: Establishes reverse tunnel. Target IP is typically 127.0.0.1 when executed directly on the target machine.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: chisel client <IP>:<TARGET_PORT> R:socks
    Description: Set up SOCKS proxy.
    Usecase: Establishes SOCKS proxy (often used with proxychains).
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

Full_Path:
  - Path: chisel.exe (standalone executable)
  - Path: chisel (standalone executable)
Detection:
  - Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_chisel.yml
Resources:
  - Link: https://github.com/jpillora/chisel
Acknowledgement:
  - Person: Dan O'Day
    Handle: '@4n68r'
---
