---
Name: Tailscale
Description: Tailscale is a commercial overlay VPN built on WireGuard that connects devices into a private network (tailnet). The control server is closed source; the client code (tailscale/tailscaled) is open source under a BSD-3 license with a separate patents file. Can be abused for persistent remote access, SSH access to hosts, egress via exit nodes, and exposing internal services to the public internet via Tailscale Funnel.
Author: Tailscale Inc.
Created: 2026-08-17
Commands:
  - Command: tailscale up
    Description: Connects the device to the user's tailnet and authenticates if needed.
    Usecase: Enroll a host into a private overlay network.
    Category: Install
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS, BSD

  - Command: tailscale up --ssh
    Description: Enables Tailscale SSH on the device, intercepting port 22 traffic from the tailnet and permitting access per the tailnet ACL policy.
    Usecase: Remote shell access to a host without traditional SSH keys/password.
    Category: Shell Access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS, BSD

  - Command: tailscale serve 3000
    Description: Shares a local service (e.g. a web server on port 3000) with other devices on the tailnet over HTTPS.
    Usecase: Expose an internal service to the private tailnet.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS, BSD

  - Command: tailscale funnel 3000
    Description: Exposes a local service to the public internet with a generated HTTPS URL via Tailscale Funnel.
    Usecase: Publish an internal service publicly, bypassing firewalls/NAT.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS, BSD
Full_Path:
  - Filename: tailscale
  - Filename: tailscaled
  - Path: tailscale
Detection:
  - Domain: 'tailscale.com'
  - Domain: '*.tailscale.io'
  - Domain: '*.ts.net'
  - Command: Execution of the tailscale binary, e.g. with up, serve, funnel or ssh subcommands.
Resources:
  - Link: https://tailscale.com/
  - Link: https://github.com/tailscale/tailscale
Acknowledgement:
  - Person: Jeffrey Tigchelaar-Moerbeek
---