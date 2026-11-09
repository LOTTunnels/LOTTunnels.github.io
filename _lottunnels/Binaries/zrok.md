---
Name: Zrok
Description: Zrok is a sharing-as-a-service tool built on OpenZiti, a zero-trust network overlay. A single command publishes a local web service, file share or private TCP/UDP endpoint through the zrok.io service (or a self-hosted instance), without any firewall or port-forwarding changes on the host.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: zrok enable <TOKEN>
    Description: Links the local environment to a zrok account using an invite/enable token.
    Usecase: One-time setup before sharing.
    Category: install
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: zrok share public localhost:<PORT>
    Description: Publishes a local web service to the internet via zrok.io and prints the resulting public URL.
    Usecase: Exposing a local service, including a hosted phishing page or payload server.
    Category: Phishing
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: zrok share public --backend-mode drive <LOCAL_DIRECTORY>
    Description: Publishes a local directory as a shareable network drive.
    Usecase: Exfiltrating a directory of files by exposing it for download.
    Category: exfiltrate
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: zrok share private localhost:<PORT>
    Description: Shares a TCP/UDP service privately with other zrok identities, without public internet exposure.
    Usecase: Reaching an internal service from another zrok-enabled host under the operator's control.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: zrok
  - Filename: zrok.exe
  - Path: Downloaded/installed zrok binary, executed anywhere on the system.
Detection:
  - Domain: '*.zrok.io'
  - Domain: 'api.zrok.io'
  - Command: Execution of zrok with enable, share, or access subcommands.
Resources:
  - Link: https://github.com/openziti/zrok
  - Link: https://docs.zrok.io
---
