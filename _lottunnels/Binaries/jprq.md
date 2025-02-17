---
Name: JPRQ
Description: JPRQ is a free and open tool for exposing local servers to public network (the internet). It can expose TCP protocols, such as HTTP, SSH, etc.
Author: Kirill Magaskin
Created: 2025-02-15
Commands:
  - Command: jprq auth <AUTHTOKEN> && jprq http <PORT>
    Description: Authenticate with token and start HTTP tunnel on PORT.
    Usecase: Quick execution of jprq.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Linux
  - Command: jprq auth <AUTHTOKEN> && jprq tcp <PORT>
    Description: Authenticate with token and start http TCP on PORT.
    Usecase: Quick execution of jprq.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Linux
Full_Path:
  - Path: Quick Start/Installed version of jprq, which gets executed anywhere on the system.
Detection:
  - Domain: '*.jprq.io'
  - Command: Execution of the binary and/or with arguments.
Resources:
  - Link: https://github.com/azimjohn/jprq
Acknowledgement:
  - Person: Kirill Magaskin
    Handle: '@k1rpi7ch'
---
