---
Name: Dev Tunnels
Description: Dev Tunnels enables insiders as well as threat actors to expose local ports over the internet via Microsoft dev tunnels.
Author: Pure-Nomad
Created: 2024-10-05
Commands:
  - Command: devtunnel host -p 3389
    Description: This will generate a dev tunnel binding it to the local service running on the provided port. Can be used to expose local services, web applications and local files etc. 
    Usecase: Exposing local services, ports, web applications etc. over the internet.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: devtunnel echo http -p 8080
    Description: By simply hosting a phishing website locally, it is possible to expose it via a Microsoft Domain.
    Usecase: Hosting malicious binaries/payloads locally and exposing them via Dev Tunnel URLs.
    Category: Phishing
    Privileges: User
    OperatingSystem: Windows, Mac, Linux
Full_Path:
  - Path: Downloaded version of Dev Tunnels, which gets executed anywhere on the system.
Detection:
  - Domain: '*.devtunnels.ms'
  - Domain: '*.data.rel.tunnels.api.visualstudio.com'
  - Domain: '*.rel.tunnels.api.visualstudio.com'
  - Domain: '*.global.rel.tunnels.api.visualstudio.com'
  - Command: Execution of the binary and/or with arguments.
Resources:
  - Link: https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/get-started?tabs=windows
  - Link: https://www.youtube.com/watch?v=jNgFmAY20wY 
Acknowledgement:
  - Person: Ergo Proxy
    Handle: '@_erg0sum'
  - Person: Brian Almond
    Handle: '@BriPwn'
---