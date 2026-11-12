---
Name: Cpolar
Description: Cpolar is a Chinese SaaS tunneling service, functionally similar to ngrok, that exposes a local HTTP/TCP service through cpolar's edge nodes. It is one of the most widely used intranet-penetration tools in the Chinese market and is commonly bundled or scripted into tutorials for exposing local development servers, which also makes it a plausible exfiltration/C2 channel for a host reachable from a Chinese network.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: cpolar authtoken <AUTHTOKEN>
    Description: Registers the client with the account associated with the given token.
    Usecase: One-time setup before creating tunnels.
    Category: install
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: cpolar http <PORT>
    Description: Exposes a local HTTP service and prints a randomly generated public URL under a cpolar domain (the random subdomain rotates periodically unless a reserved subdomain is purchased).
    Usecase: Exposing a local service, including a hosted phishing page or payload server, over the internet.
    Category: Phishing
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: cpolar
  - Filename: cpolar.exe
  - Path: Downloaded/installed cpolar binary, or a cpolar.yml configuration file, executed anywhere on the system.
Detection:
  - Domain: '*.cpolar.cn'
  - Domain: '*.cpolar.top'
  - Command: Execution of cpolar with authtoken or http/tcp subcommands.
Resources:
  - Link: https://www.cpolar.com/
---
