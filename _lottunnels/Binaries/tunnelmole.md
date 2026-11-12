---
Name: Tunnelmole
Description: Tunnelmole is an open-source tunneling tool with a hosted service and an npm/standalone client. A single command exposes a local port under a randomly generated *.tunnelmole.net subdomain, similar to ngrok or localtunnel.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: tmole <PORT>
    Description: Exposes the given local port via Tunnelmole's hosted service and prints the generated http/https *.tunnelmole.net URLs.
    Usecase: Exposing a local file server or phishing page over the internet.
    Category: Phishing
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: tmole <PORT> as <SUBDOMAIN>.tunnelmole.net
    Description: Requests a specific reserved subdomain instead of a random one (requires a paid subscription on the hosted service).
    Usecase: Standing up a consistent, memorable tunnel URL across sessions.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: tmole
  - Filename: tmole.exe
  - Path: npm-installed or standalone tmole binary, executed anywhere on the system.
Detection:
  - Domain: '*.tunnelmole.net'
  - Domain: 'install.tunnelmole.com'
  - Domain: 'dashboard.tunnelmole.com'
  - Command: Execution of tmole with a port number argument.
Resources:
  - Link: https://github.com/robbie-cahill/tunnelmole-client
  - Link: https://tunnelmole.com
---
