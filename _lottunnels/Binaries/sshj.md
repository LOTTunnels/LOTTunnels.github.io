---
Name: SSH-J
Description: SSH-J.com is a public SSH jump and port forwarding server powered by dropbear-sshj, a modified Dropbear SSH server. A host behind NAT can publish SSH ports to the public internet by connecting to ssh-j.com with an arbitrary username and a remote-forward specification, then be reached from anywhere via an SSH jump host. Also reachable over a Tor onion service. Published hosts are scoped to the username that created them.
Author: ValdikSS
Created: 2026-08-17
Commands:
  - Command: ssh any-username@ssh-j.com -N -R laptop-behind-nat:22:localhost:22
    Description: Publishes the local SSH server (localhost:22) of a host behind NAT as "laptop-behind-nat:22" on the ssh-j.com server, bound to the chosen username.
    Usecase: Exposes an SSH port of a NAT'd host to the public internet.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, MacOS, Linux

  - Command: ssh -J any-username@ssh-j.com laptop-behind-nat
    Description: Connects to a previously published host ("laptop-behind-nat") by jumping through ssh-j.com as the proxy.
    Usecase: Reaches a published SSH server from anywhere.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, MacOS, Linux
Full_Path:
  - Path: Client side uses the standard OpenSSH ssh client; server side uses the dropbear-sshj fork of Dropbear.
Detection:
  - Domain: 'ssh-j.com'
  - Domain: 'sshjmpnoutfqotbj6r3acexiwoalgkth55y5kys7js3px2qqqrwuhqqd.onion'
  - Command: Execution of the ssh client with "-R" remote forward and/or "-J" jump host arguments targeting ssh-j.com.
Resources:
  - Link: https://ssh-j.com/
  - Link: https://bitbucket.org/ValdikSS/dropbear-sshj/
Acknowledgement:
  - Person: ValdikSS
    Handle: ''
---