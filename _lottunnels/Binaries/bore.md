Name: Bore
Description: Bore is a modern, simple TCP tunnel in Rust that exposes local ports to a remote server, bypassing standard NAT connection firewalls.
Author: Kirill Magaskin
Created: 2025-02-15
Commands:
  - Command: bore local <PORT> --to bore.pub
    Description: This is quick way to start the bore and connect local PORT to the public internet at bore.pub:<PORT>, where the port number is assigned randomly.
    Usecase: Quick execution of bore.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Path: Quick Start/Installed version of bore, which gets executed anywhere on the system.
Detection:
  - Domain: 'bore.pub:*'
  - Command: Execution of the binary and/or with arguments.
Resources:
  - Link: https://github.com/ekzhang/bore
Acknowledgement:
  - Person: Kirill Magaskin
    Handle: '@k1rpi7ch'