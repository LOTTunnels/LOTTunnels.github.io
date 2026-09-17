---
Name: Portmap.io
Description: Portmap.io is a hosted tunneling and port-forwarding service that exposes services behind NAT or a firewall to the internet through *.portmap.io hostnames over an OpenVPN connection. It has been repeatedly observed as attacker infrastructure, providing free *.portmap.io subdomains used as command-and-control endpoints by malware such as Pekraut, LodaRAT and SpyNote, and by APT19/Chimera.
Author: cyberbuff
Created: 2026-09-17
Commands:
    - Command: openvpn <config>.ovpn
      Description: Connects the local host to the Portmap.io network using the OpenVPN configuration downloaded from the Portmap.io dashboard, after which configured mappings forward a public *.portmap.io host and port to a local service.
      Usecase: Establishing the Portmap.io tunnel to expose a local service.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS

    - Command: "<mapping via dashboard>: 4433 -> 127.0.0.1:4433"
      Description: A port mapping configured in the Portmap.io web dashboard forwards a public port on a *.portmap.io host to a local service, reachable from anywhere on the internet.
      Usecase: Exposing a local service such as a C2 listener or RAT over the internet.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS
Custom_Domain_Supported: False
Full_Path:
    - Path: Uses the standard OpenVPN client with a Portmap.io-issued configuration; mappings are managed in the Portmap.io web dashboard.
Detection:
    - Domain: "*.portmap.io"
    - Domain: "*.portmap.host"
    - Command: Execution of the OpenVPN client with a Portmap.io configuration file.
Resources:
    - Link: https://portmap.io/
    - Link: https://portmap.io/knowledgebase
---
