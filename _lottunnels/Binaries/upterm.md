---
Name: Upterm
Description: Upterm shares a terminal session over SSH through a relay server. By default it uses the public uptermd.upterm.dev relay, so anyone given the session's SSH connection string (or, with --authorized-user, anyone whose public key is registered on GitHub/GitLab/etc.) can join an interactive shell on the host running upterm.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: upterm host
    Description: Starts a new shared terminal session via the public uptermd.upterm.dev relay and prints the SSH connection string to join it.
    Usecase: Giving an operator interactive shell access to a compromised host through a public relay, without installing a dedicated remote-access agent.
    Category: shell-access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: upterm host --authorized-key <PUBLIC_KEY_FILE>
    Description: Restricts who can join the session to holders of the given SSH key.
    Usecase: Restricting shell access to a specific operator key.
    Category: shell-access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: ssh <SESSION_USER>@uptermd.upterm.dev
    Description: Joins an existing shared session as the viewer/operator side.
    Usecase: Connecting to a previously hosted upterm session.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: upterm
  - Path: Downloaded/installed upterm binary, executed anywhere on the system.
Detection:
  - Domain: 'uptermd.upterm.dev'
  - Command: Execution of upterm with host, session or join arguments.
  - Command: Outbound SSH connections to uptermd.upterm.dev from a host where SSH is not otherwise used.
Resources:
  - Link: https://github.com/owenthereal/upterm
  - Link: https://upterm.dev
---
