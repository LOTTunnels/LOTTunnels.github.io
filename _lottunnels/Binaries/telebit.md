---
Name: Telebit
Description: Telebit is an open source tool which enables local services/applications to be exposed over the internet. Insiders as well as threat actors can use this tool to perform variety of malicious tasks. Although, the tool requires an authentication token of which free token can be obtained from the website.

Author: Kamran Saifullah
Created: 2024-10-14
Commands:

  - Command: curl https://get.telebit.io/ | bash
    Description: Downloading and Installation of telebit on the local machine.
    Usecase: Downloading the telebit binary to be executed on the local machine.
    Category: install
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: telebit http <PORT>>
    Description: Binding telebit tunnels to the local port running on the machine to expose the local applications over the tunnels. 
    Usecase: Exposing local applications over the internet via telebit tunnels. 
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: telebit http <PORT>
    Description: Running a local server in a directory and exposing it over the telebit tunnels for data exfiltration.
    Usecase: Exposing local file system via telebit tunnels for data exfiltration.
    Category: exfiltrate
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: telebit tcp <PORT>>
    Description: Binding telebit tunnels to the local SSH/RDP ports etc. for shell access.
    Usecase: Exposing local ports over the internet via telebit tunnels for shell access. 
    Category: shell-access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: telebit http <PORT>>
    Description: Binding telebit tunnels to the local file system/web server and exposing malicious binaries to be downloaded onto the compromised host.
    Usecase: Exposing locally hosted malicious binaries over the internet via telebit tunnels to be downloaded onto compromised host.
    Category: download
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: telebit http <PORT>>
    Description: Binding telebit tunnels to the locally running phishing page to compromise users.
    Usecase: Exposing locally running phishing sites over the internet via telebit tunnels to compromise users.
    Category: phishing
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

Full_Path:
  - Path: Installed version/In memory execution of telebit.
Detection:
  - Domain: 'get.telebit.io'
  - Domain: '*.telebit.io'
  - Domain: '*.telebit.cloud'
  - Domain: '*.telebit.fun'
  - Command: Execution of the binary and/or with arguments.
Resources:
  - Link: https://telebit.cloud/
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
---