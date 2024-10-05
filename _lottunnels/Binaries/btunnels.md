---
Name: Broken Tunnels - Btunnels.exe
Description: Broken Tunnels enables insiders as well as threat actors to expose local ports, local file system, local application over the internet via btunnels dynamic tunnel URLs.
Author: Kamran Saifullah
Created: 2024-10-05
Commands:
  - Command: btunnel.exe file --key <API-KEY>
    Description: This will generate tunnels link while exposing the local filesystem as a Directory Listing.
    Usecase: Exposing file system over the internet.
    Category: Exfiltrate
    Privileges: User
    OperatingSystem: Windows, Mac, Linux
Commands:
  - Command: btunnel.exe http --key <API-KEY>
    Description: This will generate tunnels link binding it to the local service running on the provided port. Can be used to expose local services, web applications and local files etc. 
    Usecase: Exposing local services, ports, web applications etc. over the internet.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux
Full_Path:
  - Path: Downloaded version of Btunnels, which gets executed anywhere on the system.
Detection:
  - Domain: '*.btunnel.co.in'
  - Domain: '*.btunnel.in'
  - Sigma: https://github.com/search?q=repo%3ASigmaHQ%2Fsigma+9e02c8ec-02b9-43e8-81eb-34a475ba7965&type=code
Resources:
  - Link: https://valhalla.nextron-systems.com/info/sigma-rule/9501f8e6-8e3d-48fc-a8a6-1089dd5d7ef4
  - Link: https://defr0ggy.github.io/research/Utilizing-BTunnel-For-Data-Exfiltration/
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
---
