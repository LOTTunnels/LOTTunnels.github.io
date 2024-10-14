---
Name: Burrow
Description: Burrow is subscription based tool which enables local services/applications to be exposed over the internet. Insiders as well as threat actors can use this tool to perform variety of malicious tasks. Although, the tool requires an authentication token of which free token can be obtained from the website. The tunnels are required to be created from the dashboard first which generates a command to be executed locally onto the system to bind the service/port to the burrow tunnels.
Author: Kamran Saifullah
Created: 2024-10-14
Commands:
  - Command: curl -Ls https://burrow.io/<RANDOM> | bash -s
    Description: The URLs generated can be binded to a locally hosting services via bash. 
    Usecase: Binding the local machine to the externally generated burrow tunnels.
    Category: Access
    Privileges: User
    OperatingSystem: Mac, Linux

Full_Path:
  - Path: Installed version/In memory execution of telebit.
Detection:
  - Domain: '*.burrow.io'
  - Domain: '*.burrow.link'
  - Domain: 'io.burrow.link:*'
  - Command: Execution of the binary and/or with arguments.
Resources:
  - Link: https://burrow.io/
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
---