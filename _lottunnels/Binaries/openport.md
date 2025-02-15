Name: OpenPort
Description: Openport builds a secure tunnel from your device to the outside world, so you can connect to your device from anywhere.
Author: Kirill Magaskin
Created: 2025-02-15
Commands:
  - Command: openport register-key <AUTHTOKEN> && openport <PORT>
    Description: Authenticate with token and start tunnel on PORT.
    Usecase: Quick execution of openport.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Linux

Full_Path:
  - Path: Quick Start/Installed version of jprq, which gets executed anywhere on the system.
Detection:
  - Domain: 'https://openport.io/*'
  - Command: Execution of the binary and/or with arguments.
Resources:
  - Link: https://openport.readthedocs.io/en/latest/usage.html#installation
Acknowledgement:
  - Person: Kirill Magaskin
    Handle: '@k1rpi7ch'