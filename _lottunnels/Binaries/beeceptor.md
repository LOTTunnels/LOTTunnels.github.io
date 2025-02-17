Name: Beeceptor
Description: The Beeceptor CLI is a developer tool to help you connect the localhost port with Beeceptor's public endpoint. It is easy to install, and works on all platforms (macOS, Windows, and Linux). The Beeceptor CLI can be installed using NPM or downloaded as an independent executable file.
Author: Kirill Magaskin
Created: 2025-02-15
Commands:
  - Command: beeceptor-cli -p <PORT> [--https] [--headless]
    Description: This is quick way to start the beeceptor and connect local PORT to internet domain. After running this command you'll be required to authorize in browser on target host. Use --headless to print AuthToken and authorize on source host. This tool by default uses HTTP, for HTTPS check --https option.
    Usecase: Quick execution of beeceptor.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Path: Quick Start/Installed version of beeceptor, which gets executed anywhere on the system.
Detection:
  - Domain: '*.beeceptor.com'
  - Command: Execution of the binary and/or with arguments.
Resources:
  - Link: https://beeceptor.com/docs/local-tunneling-by-exposing-service-port/?ref=landing-page
Acknowledgement:
  - Person: Kirill Magaskin
    Handle: '@k1rpi7ch'