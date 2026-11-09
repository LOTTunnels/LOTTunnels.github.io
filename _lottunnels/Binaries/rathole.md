---
Name: Rathole
Description: Rathole is an open source reverse proxy for NAT traversal written in Rust. It is functionally similar to frp, with a server on a public host and a client behind the firewall, and services described in TOML files. It supports TLS and Noise transports.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: rathole --server server.toml
    Description: Runs on the operator's public host and waits for client connections.
    Usecase: Operator side of a reverse tunnel.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: rathole --client client.toml
    Description: Runs on the compromised host. The configuration maps a local service (for example 127.0.0.1:22 or :3389) to a service token on the server.
    Usecase: Exposing an internal service such as SSH or RDP to the operator.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: rathole
  - Filename: rathole.exe
  - Path: Downloaded rathole binary and a client.toml or server.toml file, which get placed anywhere on the system.
Detection:
  - Command: Execution of the rathole binary with --client or --server (or -c/-s) and a .toml file argument.
  - Command: TOML files that contain [client.services.*] with local_addr, or [server.services.*] with bind_addr and token.
Resources:
  - Link: https://github.com/rapiz1/rathole
---
