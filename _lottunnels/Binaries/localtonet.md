Name: LocaltoNet
Description: LocaltoNet is a reverse proxy that enables you to expose your localhost services to the internet.
Author: Kirill Magaskin
Created: 2025-02-15
Commands:
  - Command: localtonet.exe
    Description: This is a way to start the LocaltoNet in Windows. You will be prompted for your AuthToken. Then you should configure your service port in LocaltoNet Web Dashboard and generate link.
    Usecase: Quick execution of LocaltoNet.
    Category: Access
    Privileges: User
    OperatingSystem: Windows

  - Command: localtonet authtoken <AUTHTOKEN>
    Description: This is a quick way to start the LocaltoNet by directly executing the LocaltoNet. Then you should configure your service port in LocaltoNet Web Dashboard and generate link.
    Usecase: Quick execution of LocaltoNet.
    Category: Access
    Privileges: User
    OperatingSystem: Linux

  - Command: localtonet
    Description: This is a way to start the LocaltoNet in MacOS. You will be prompted for your AuthToken. Then you should configure your service port in LocaltoNet Web Dashboard and generate link.
    Usecase: Quick execution of LocaltoNet.
    Category: Access
    Privileges: User
    OperatingSystem: MacOS
Full_Path:
  - Path: Quick Start/Installed version of LocaltoNet, which gets executed anywhere on the system.
Detection:
  - Domain: '*.localto.net'
  - Domain: '*.localtonet.com'
  - Command: Execution of the binary and/or with arguments.
Resources:
  - Link: https://localtonet.com/documents
Acknowledgement:
  - Person: Kirill Magaskin
    Handle: '@k1rpi7ch'