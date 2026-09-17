---
Name: Packetriot
Description: Packetriot (pktriot) is a tunneling service that exposes local HTTP, TCP and UDP services behind NAT or a firewall to the internet through Packetriot edge servers, reachable via assigned *.pktriot.net hostnames (edge servers use *.packetriot.net) or a custom domain. It has been observed being abused by threat actors, including in XWorm campaigns, to expose command-and-control and internal services without configuring port forwarding.
Author: cyberbuff
Created: 2026-09-17
Commands:
    - Command: pktriot start
      Description: Starts the Packetriot client using the configured tunnel, exposing the local service to the internet through a Packetriot edge server. The client is authenticated with an account token and the edge host is assigned as a *.packetriot.net address.
      Usecase: Quick execution of Packetriot to expose a local service.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS

    - Command: pktriot http 8080
      Description: Exposes a local HTTP service listening on port 8080 through the Packetriot edge, returning a public *.pktriot.net URL.
      Usecase: Exposing a local web service over the internet for access or data exfiltration.
      Category: Exfiltrate
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS

    - Command: pktriot tunnel tcp --destination 127.0.0.1 --dport 22
      Description: Forwards a public TCP port on the Packetriot edge to a local service such as SSH, giving remote access to a host behind NAT or a firewall.
      Usecase: Maintaining remote access to an internal host.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS
Custom_Domain_Supported: True
Full_Path:
    - Path: Downloaded/Installed version of the pktriot binary, which gets executed anywhere on the system.
Detection:
    - Domain: "*.packetriot.net"
    - Domain: "*.pktriot.net"
    - Command: Execution of the pktriot binary and/or with arguments.
Resources:
    - Link: https://packetriot.com/
    - Link: https://packetriot.com/docs
    - Link: https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/how-cybercriminals-abuse-cloud-tunneling-services
    - Link: https://cert.pl/en/posts/2023/10/deworming-the-xworm/
---
