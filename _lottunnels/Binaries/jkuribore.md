Name: jkuri Bore
Description: Reverse HTTP/TCP proxy tunnel via secure SSH connections.
Author: Kirill Magaskin
Created: 2025-02-15
Commands:
  - Command: bore -s bore.digital -p 2200 -ls localhost -lp <PORT>
    Description: This is quick way to start the bore and connect local PORT to the public internet at bore.digital:<PORT>, where the port number is assigned randomly. Also the links for HTTP/HTTPS access will be generated.
    Usecase: Quick execution of bore.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Linux
Full_Path:
  - Path: Quick Start/Installed version of bore, which gets executed anywhere on the system.
Detection:
  - Domain: 'bore.digital:*'
  - Domain: '*.bore.digital'
  - Command: Execution of the binary and/or with arguments.
Resources:
  - Link: https://github.com/jkuri/bore
Acknowledgement:
  - Person: Kirill Magaskin
    Handle: '@k1rpi7ch'