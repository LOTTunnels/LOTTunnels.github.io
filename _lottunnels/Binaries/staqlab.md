---
Name: StaqLab
Description: Staqlab enables insider threats and threat actors to create fake account on the website as there is no validation for account registration. In the Domains Section, threat actors can define dedicated tunnels subdomain name. Using the token for the authorization on the local system will enable them to connect to dynamically generated domains or else specified domains.  
Author: Kamran Saifullah
Created: 2024-10-06
Commands:

  - Command: staqlab-tunnel.exe token=<AUTH TOKEN>
    Description: This will register the local staqlab-tunnel.exe with the registered account.  
    Usecase: Authenticating, generating and accessing the URL.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux, Raspberry Pi

  - Command: staqlab-tunnel.exe port=<PORT>
    Description: This will create a tunnel to the port defined.
    Usecase: Exposing the local server running on local port over dynamic Staqlab Tunnels.
    Category: exfiltrate
    Privileges: User
    OperatingSystem: Windows, Mac, Linux, Raspberry Pi

  - Command: staqlab-tunnel.exe port=<PORT> domain=<DOMAIN>
    Description: Exposing the local server running on local port over Staqlab Tunnels having static domain names defined in the dashboard. This can be used in Phishing Campaigns. However, the dynamically generated links can also be used for the same purpose.
    Usecase: Exposing the local server running on local port over static Staqlab Tunnels.
    Category: Phishing
    Privileges: User
    OperatingSystem: Windows, Mac, Linux, Raspberry Pi

Full_Path:
  - Path: Downloaded version of Staqlab-tunnels.exe, which gets executed anywhere on the system.
Detection:
  - Domain: '*.tunnel.staqlab.com'
  - Domain: 'https://tunnel.staqlab.com/inspector/<4 Digits>/inspector'
  - Domain: '*.staqlab-tunnel.com'
  - Command: Execution of the binary and/or with arguments. 
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
---