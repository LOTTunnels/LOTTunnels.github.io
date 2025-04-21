---
Name: Tmate
Description: Tmate.io provides a simple binary to expose local terminal via tmate.io domains. These domains are accessible over the internet. Providing opportunity for insiders to expose local system, exfiltrate data, create backdoors via SSH etc.
Author: Kamran Saifullah
Created: 2024-10-08
Commands:

  - Command: tmate
    Description: This will generate instant tmate tunnel which is accessible via web browser as well as via SSH client. Insider threat or external threat actor can used this for accessing and monitoring the terminals using the read-only tunnel links.
    Usecase: Accessing the terminal via web browser or ssh remotely.
    Category: Access
    Privileges: User
    OperatingSystem: Mac, Linux

  - Command: tmate
    Description: This will generate instant tmate tunnel which is accessible via web browser as well as via SSH client. Insider threat or external threat actor can used this for data exfiltration.
    Usecase: Exposing file system over the internet.
    Category: exfiltrate
    Privileges: User
    OperatingSystem: Mac, Linux

  - Command: tmate -F
    Description: This will generate instant tmate tunnel which is accessible via web browser as well as via SSH client. Insider threat or external threat actor can used this for backdoor as `-F` will foreground the current process.
    Usecase: Maintaning access via Web or via SSH.
    Category: shell-access
    Privileges: User
    OperatingSystem: Mac, Linux

Full_Path:
  - Path: Downloaded/Installed version of tmate, which gets executed anywhere on the system.
Detection:
  - Domain: '*.tmate.io'
  - URL: 'https://tmate.io/t/*'
  - Command: Execution of the binary and/or with arguments.
Resources:
  - Link: https://dfir.ch/posts/tmate_as_a_backdoor/
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
---