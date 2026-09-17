---
Name: NetBird
Description: NetBird is a WireGuard-based overlay network and zero-trust remote access service that connects peers into a private mesh through NetBird management and signal servers, traversing NAT and firewalls without inbound ports. Threat actors have been observed deploying the NetBird client on compromised hosts to establish persistent, encrypted remote access into internal environments.
Author: cyberbuff
Created: 2026-09-17
Commands:
    - Command: netbird up --setup-key <KEY>
      Description: Enrolls the host into a NetBird network using a setup key and brings the WireGuard-based tunnel up, joining the host to the attacker-controlled mesh.
      Usecase: Establishing persistent remote access to a host behind NAT/firewall.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS

    - Command: netbird up --management-url <URL> --setup-key <KEY>
      Description: Enrolls the host against a specified (including self-hosted) NetBird management server, joining a custom overlay network controlled by the operator.
      Usecase: Joining a self-hosted NetBird network for remote access.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS

    - Command: netbird status
      Description: Shows the status of the NetBird connection and connected peers, confirming the host is reachable within the overlay network.
      Usecase: Verifying remote access into the mesh.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS
Custom_Domain_Supported: True
Full_Path:
    - Path: Downloaded/Installed netbird client binary, which gets executed anywhere on the system.
Detection:
    - Domain: "*.netbird.io"
    - Domain: "api.netbird.io"
    - Command: Execution of the netbird binary, particularly with the up and --setup-key arguments.
Resources:
    - Link: https://netbird.io/
    - Link: https://github.com/netbirdio/netbird
    - Link: https://research.checkpoint.com/2026/handala-hack-unveiling-groups-modus-operandi/
---
