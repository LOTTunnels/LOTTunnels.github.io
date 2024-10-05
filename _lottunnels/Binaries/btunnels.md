---
Name: Broken Tunnels - Btunnels.exe
Description: Broken Tunnels enables insiders as well as threat actors to expose local ports, local file system, local application over the internet via btunnels dynamic tunnel URLs.
Author: Kamran Saifullah
Created: 2024-10-05
Commands:
  - Command: CTRL + SHIFT + P, Searching for Forward a port. Click on forward the port and provide a local port which is required to be exposed over the internet.
    Description: This will generate a microsoft tunnel link proxying the traffic to the local binded port.
    Usecase: Exposing internal application on Microsoft Tunnels over the internet.  
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: CTRL + SHIFT + P, Searching for Foreward a port, Click on forward the port and provide a local port on which a local server is running. An example, 'python -m http.server 8080'.  
    Description: Insider threat, external threat actor will be able to expose the local system over the internet and exfiltrate the sensitive files.
    Usecase: Accessing & exfiltrating the local files on VSCode Cloud for Data Exfiltration.
    Category: Exfiltrate
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

Full_Path:
  - Path: Downloaded version of Visual Studio Code, which gets executed anywhere on the system.
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
