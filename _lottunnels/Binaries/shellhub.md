---
Name: ShellHub
Description: ShellHub is an online service/subscription based that enables local services/applications to be exposed over the internet. Insiders as well as threat actors can use this tool to perform variety of malicious tasks. Although, the tool requires an authentication token of which free token can be obtained from the website.

Author: Kamran Saifullah
Created: 2024-10-13
Commands:

  - Command: curl -sSf "https://cloud.shellhub.io/install.sh?tenant_id=<TENANT ID>" | sh 
    Description: Installating of ShellHub on the local system to be added as an approved device.
    Usecase: Executing the installation script to install ShellHub on the local system.
    Category: install
    Privileges: User
    OperatingSystem: Mac, Linux

  - Command: ShellHub Dashboard
    Description: Accessing the local system via ShellHub dashboard. Requires to know the username and password or SSH private keys.
    Usecase: Knowing the credentials or SSH private key, users/threat actors can connect to the local terminal via ShellHub Cloud Terminal.
    Category: shell-access
    Privileges: User
    OperatingSystem: Mac, Linux

Full_Path:
  - Path: Installed ShellHub script/docker container, which gets executed anywhere on the system.
Detection:
  - Domain: '*.shellhub.io*'
  - Command: Execution of the installation command.
Resources:
  - Link: https://cloud.shellhub.io/
  - Link: https://www.shellhub.io/
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
---