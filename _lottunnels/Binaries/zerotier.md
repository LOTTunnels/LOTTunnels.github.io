---
Name: ZeroTier
Description: ZeroTier is a peer-to-peer overlay network that joins hosts into a virtual L2/L3 network traversing NAT and firewalls, coordinated through ZeroTier root/controller servers (or a self-hosted controller). Threat actors deploy the ZeroTier client on compromised hosts to establish persistent, encrypted remote access into internal environments, observed with Scattered Spider/UNC3944 and the CrowdStrike telco/BPO intrusion campaign.
Author: cyberbuff
Created: 2026-09-17
Commands:
    - Command: zerotier-cli join <NETWORK_ID>
      Description: Joins the host to an attacker-controlled ZeroTier network, placing it on a virtual overlay reachable by other members regardless of NAT or firewalls.
      Usecase: Establishing persistent remote access to a host behind NAT/firewall.
      Category: Access
      Privileges: Administrator
      OperatingSystem: Windows, Linux, MacOS

    - Command: zerotier-cli listnetworks
      Description: Lists the ZeroTier networks the host is a member of and the assigned overlay IP addresses, confirming reachability within the mesh.
      Usecase: Verifying remote access into the overlay network.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS

    - Command: zerotier-one -d
      Description: Runs the ZeroTier service as a daemon so the host rejoins its networks on boot, maintaining persistent access.
      Usecase: Persisting overlay-network access across reboots.
      Category: Access
      Privileges: Administrator
      OperatingSystem: Windows, Linux, MacOS
Custom_Domain_Supported: True
Full_Path:
    - Path: Downloaded/Installed zerotier-one service and zerotier-cli client, executed anywhere on the system.
Detection:
    - Domain: "*.zerotier.com"
    - Command: Execution of zerotier-one / zerotier-cli, particularly the join subcommand, or traffic to the default ZeroTier UDP port 9993.
Resources:
    - Link: https://www.zerotier.com/
    - Link: https://github.com/zerotier/ZeroTierOne
    - Link: https://www.crowdstrike.com/blog/analysis-of-intrusion-campaign-targeting-telecom-and-bpo-companies/
    - Link: https://blog.sekoia.io/scattered-spider-laying-new-eggs/
---
