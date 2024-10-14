---
Name: Dataplicity
Description: Dataplicity is free/subscription based tool which enables connecting local systems to dataplicity cloud for remotely accessing them over the internet.
Author: Kamran Saifullah
Created: 2024-10-14
Commands:
  - Command: curl -s https://www.dataplicity.com/<TOKEN>.py | sudo python
    Description: Having an account created on the website, it is possible to connect any system to the Dataplicity cloud and access it remotely, keeping shell-access.
    Usecase: Connecting the user machine to daraplicity cloud for shell-access/remote-access.
    Category: shell-access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: curl -s https://www.dataplicity.com/<TOKEN>.py | sudo python
    Description: Having an paid account created on the website, it is possible to connect any system to the Dataplicity cloud and access it remotely, keeping persistent access.
    Usecase: Connecting the user machine to daraplicity cloud for persistence.
    Category: persistence
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

Full_Path:
  - Path: Execution of dapalicity puthon moduel from anywhere on the system.
Detection:
  - Domain: '*.dataplicity.com'
  - Command: Execution of the command.
Resources:
  - Link: https://www.dataplicity.com/
  - Link: https://github.com/wildfoundry/dataplicity-agent
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
---