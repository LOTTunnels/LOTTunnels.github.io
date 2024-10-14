---
Name: Loophole
Description: Loophole is an open source tool which enables local services/applications to be exposed over the internet. Insiders as well as threat actors can use this tool to perform variety of malicious tasks. Although, the tool requires an authentication token of which free token can be obtained from the website.

Author: Kamran Saifullah
Created: 2024-10-13
Commands:

  - Command: loophole standlone binaries
    Description: Exeuction of loophole standlone binaries on the local machine. 
    Usecase: Executing the loophole standalone binaries to connect it to the tunnels.
    Category: install
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: loophole account login
    Description: Authenticating loophole account with the API key to register the device with the account.
    Usecase: Registering local machine with the loophole account. 
    Category: access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: ./loophole path ./my-directory
    Description: Hosting malicious files over the loophole tunnels and downloading them over to the compromised host.
    Usecase: Downloading locally hosted malicious binaries exposed over loophole tunnels to download.
    Category: download
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: ./loophole http 3000
    Description: Hosting phishing sites locally and exposing them over the loophole tunnels to compromise users.
    Usecase: Phishing site hosted locally and exposed over the loophole tunnels to compromise users.
    Category: phishing
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: ./loophole path ./my-directory
    Description: Exposing local file system over the loophole tunnels to exfiltrate data outside the organization.
    Usecase: Exfiltrating data outside organization via loophole tunnels.
    Category: exfiltrate
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

Full_Path:
  - Path: Installed version of expose binary/docker container, which gets executed anywhere on the system.
Detection:
  - Domain: 'loophole.eu.auth0.com/activate'
  - Domain: '*.loophole.site'
  - Command: Execution of the binary and/or with arguments.
Resources:
  - Link: https://loophole.cloud/docs
  - Link: https://github.com/loophole/cli/
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
---