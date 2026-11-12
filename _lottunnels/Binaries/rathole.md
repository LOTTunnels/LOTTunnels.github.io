---
Name: Rathole
Description: Rathole is a reverse proxy for NAT traversal, written in Rust, functionally similar to frp. A server on a public operator-controlled host and a client on the target network are each configured with a TOML file describing the services to expose; the client dials out to the server, so no inbound access to the target network is required. It supports TLS and Noise transports.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: rathole --server server.toml
    Description: Runs on the operator's public host and waits for client connections, exposing the services configured in server.toml.
    Usecase: Operator side of a reverse proxy tunnel.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: rathole --client client.toml
    Description: Runs on the compromised host. The configuration maps a local service (for example 127.0.0.1:22 or 127.0.0.1:3389) to a service name defined on the server.
    Usecase: Exposing an internal service such as SSH or RDP to the operator through the server.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: rathole
  - Filename: rathole.exe
  - Path: Downloaded rathole binary and a client.toml or server.toml file, placed anywhere on the system.
Detection:
  - Command: Execution of the rathole binary with --client or --server (or -c/-s) and a .toml file argument.
  - Command: TOML files containing a [client.services.*] section with local_addr, or a [server.services.*] section with bind_addr and token.
Resources:
  - Link: https://github.com/rapiz1/rathole
---
