---
Name: Expose
Description: Expose is an open source as well as subscription based tool which enables local services/applications to be exposed over the internet. Insiders as well as threat actors can use this tool to perform variety of malicious tasks. Although, the tool requires an authentication token of which free token can be obtained from the website.

Author: Kamran Saifullah
Created: 2024-10-13
Commands:

  - Command: curl https://github.com/beyondcode/expose/raw/master/builds/expose -L --output expose
    Description: Downloading and Installation of expose binary on the local system as a PHAR archive.
    Usecase: Downloading the expose binary to be executed on the local machine.
    Category: install
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: composer global require beyondcode/expose
    Description: Downloading and Installation of expose binary on the local system.
    Usecase: Downloading the expose binary to be executed on the local machine via composer.
    Category: install
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: expose token <token>
    Description: Initiating the access via providing expose token.
    Usecase: Authenticating the session via expose token.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: expose default-server ap-1
    Description: Setting up default server via expose to connect to the nearest expose server.
    Usecase: Connecting to the nearest expoe server for better bandwidth and connection stability.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: expose share http://https://localhost:<LOCAL PORT>
    Description: Exposing the local server/services over the internet to be accessible over expose domains.
    Usecase: Exposing the services running on localhost over the internet via expose tunnel domains. 
    Category: exfiltrate
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: expose share http://https://localhost:<LOCAL PORT>
    Description: This can be used by threat actors to host malicious softwares/binaries on their local system and have it exposed via expose tunnels to be downloaded on the compromised system.
    Usecase: Threat actors hosting malicious binaries and using the links to download them onto the compromised system. 
    Category: download
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: expose share http://https://localhost:<LOCAL PORT>
    Description: This can be used by threat actors to host phishing sites locally and expose them via expose tunnels to compromise users.
    Usecase: Hosting phishing sites locally and exposing them over expose tunnels to compromise users.
    Category: phishing
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: expose share http://https://localhost:<LOCAL PORT> --server=<server>
    Description: This can be used by threat actors to connect to the nearest expose server.
    Usecase: Connecting to the nearest expose server in specific regions.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

Full_Path:
  - Path: Installed version of expose binary/docker container, which gets executed anywhere on the system.
Detection:
  - Domain: '*.sharedwithexpose.com'
  - Domain: '*.eu-1.sharedwithexpose.com'
  - Domain: '*.us-1.sharedwithexpose.com'
  - Domain: '*.us-2.sharedwithexpose.com'
  - Domain: '*.ap-1.sharedwithexpose.com'
  - Domain: '*.in-1.sharedwithexpose.com'
  - Domain: '*.sa-1.sharedwithexpose.com'
  - Domain: '*.au-1.sharedwithexpose.com'
  - Domain: '*.eu-2.sharedwithexpose.com'
  - Command: Execution of the binary and/or with arguments.
Resources:
  - Link: https://expose.dev/docs/getting-started/installation
  - Link: https://github.com/beyondcode/expose
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
---