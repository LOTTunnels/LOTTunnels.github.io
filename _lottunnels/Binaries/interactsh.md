---
Name: interactsh
Description: An OOB interaction gathering server and client library which is used by Cyber Security Professionals but have an equal opportunity for the threat actors to abuse it for data exfiltration. 
Author: Kamran Saifullah
Created: 2026-08-16
Commands:
  - Command: interactsh-client
    Description: An OOB interaction gathering server and client library which is used by Cyber Security Professionals but have an equal opportunity for the threat actors to abuse it for data exfiltration. 
    Usecase: Data Exfiltration.
    Category: Data Exfiltration
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Path: Quick Start/Installed version of interactsh, which gets executed anywhere on the system.
Detection:
  - Domain: '*.oast.pro'
  - Domain: '*.oast.live'
  - Domain: '*.oast.site'
  - Domain: '*.oast.online'
  - Domain: '*.oast.fun'
  - Domain: '*.oast.me'
  - Command: Execution of the binary and/or with arguments.
Resources:
  - Link: https://github.com/projectdiscovery/interactsh
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
---
