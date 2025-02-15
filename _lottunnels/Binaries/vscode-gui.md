---
Name: VSCode GUI
Description: Insiders as well as threat actors having GUI access to system can leverage this technique to create Visual Studio Remote Tunnel links to exfiltrate the data.
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

  - Command: CTRL + SHIFT + P, Searching for Foreward a port, Click on forward the port and provide a local port on which a local server is running. An example, 'python -m http.server 8080'.  
    Description: Threat actors can host malicious binaries/payloads locally and can use Microsoft Tunnels domains to download them onto the victim machine. 
    Usecase: Downloading malicious binaries/payloads on victim system by hosting them locally. 
    Category: Download
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

Full_Path:
  - Path: Downloaded version of Visual Studio Code, which gets executed anywhere on the system.
Detection:
  - Domain: '*.devtunnels.ms*'
  - Domain: '*.tunnels.api.visualstudio.com'
  - Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_devtunnels.yml
Resources:
  - Link: https://valhalla.nextron-systems.com/info/sigma-rule/9501f8e6-8e3d-48fc-a8a6-1089dd5d7ef4
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
  - Person: Kirill Magaskin
    Handle: '@k1rpi7ch'
---
