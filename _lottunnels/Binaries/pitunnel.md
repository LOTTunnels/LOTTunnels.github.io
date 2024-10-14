---
Name: PiTunnel
Description: PiTunnel is free/subscription based tool which enables connecting local systems to dataplicity cloud for remotely accessing them over the internet.
Author: Kamran Saifullah
Created: 2024-10-14
Commands:
  - Command: curl -s https://pitunnel.com/get/<TOKEN> | sudo bash
    Description: Having an account created on the website, it is possible to connect any system to the PiTunnel cloud and access it remotely, keeping access over tunnels.
    Usecase: Connecting the user machine to Pitunnl keeping access over tunnels.
    Category: Access
    Privileges: User
    OperatingSystem: RaspberryPi

  - Command: wget -qO- https://pitunnel.com/get/<TOKEN>> | sudo
    Description: Having an account created on the website, it is possible to connect any system to the PiTunnel cloud and access it remotely, for shell-access.
    Usecase: Connecting the user machine to PiTunnel cloud for data exfiltration.
    Category: shell-access
    Privileges: User
    OperatingSystem: RaspberryPi

  - Command: pitunnel --port=<PORT> --name=vnc --persist
    Description: Having an account created on the website, it is possible to connect any system to the PiTunnel cloud and access it remotely, for data exfiltration.
    Usecase: Connecting the user machine to PiTunnel cloud for data exfiltration.
    Category: exfiltrate
    Privileges: User
    OperatingSystem: RaspberryPi

Full_Path:
  - Path: Execution of pitunnel/bash command from anywhere on the system.
Detection:
  - Domain: '*pitunnel.com'
  - Command: Execution of the command.
Resources:
  - Link: https://www.pitunnel.com/
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
---