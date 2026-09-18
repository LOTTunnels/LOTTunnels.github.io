---
Name: Twingate
Description: Twingate is a hosted zero-trust remote access service that connects clients to private resources through Twingate Connectors deployed inside a network, without exposing inbound ports. Threat actors, notably Scattered Spider/UNC3944 and Octo Tempest, have been observed deploying Twingate Connectors on compromised networks to establish persistent remote access into internal environments.
Author: cyberbuff
Created: 2026-09-17
Commands:
    - Command: twingate setup
      Description: Configures the Twingate client on a host, authenticating it to a Twingate network so the host can reach private resources published through Connectors.
      Usecase: Establishing client access into a Twingate-connected network.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS

    - Command: twingate start
      Description: Starts the Twingate client and establishes the tunnel to the Twingate network, giving the host access to internal resources over the internet.
      Usecase: Maintaining remote access to an internal network.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS

    - Command: docker run twingate/connector
      Description: Deploys a Twingate Connector inside a network. A threat actor with a foothold can deploy a Connector to publish internal resources to their own Twingate tenant and reach them remotely.
      Usecase: Establishing persistent remote access into a compromised network.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS
Custom_Domain_Supported: False
Full_Path:
    - Path: Downloaded/Installed Twingate client, or a Connector deployed via Docker/binary inside the target network.
Detection:
    - Domain: "*.twingate.com"
    - Command: Execution of the twingate client binary, or deployment of the twingate/connector image.
Resources:
    - Link: https://www.twingate.com/
    - Link: https://www.microsoft.com/en-us/security/blog/2023/10/25/octo-tempest-crosses-boundaries-to-facilitate-extortion-encryption-and-destruction/
    - Link: https://blog.sekoia.io/scattered-spider-laying-new-eggs/
    - Link: https://www.mandiant.com/resources/blog/unc3944-sms-phishing-sim-swapping-ransomware
---
