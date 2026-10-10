---
Name: OpenTunnel
Description: OpenTunnel is an end-to-end encrypted ("blind") TLS tunnel hosted on Cloudflare by Anomaly. Each client receives a unique <id>.opentunnel.xyz hostname and terminates TLS locally, so the relay only reads the SNI from the TLS handshake and never sees plaintext traffic. A background service (systemd/launchd or a plain background process) keeps subdomain routes connected to local ports, which makes it suitable for persistent access to internal services.
Author: cyberbuff
Created: 2026-10-07
Commands:
  - Command: curl -fsSL https://opentunnel.xyz/install | sh
    Description: Downloads and runs the install script, which fetches the prebuilt opentunnel binary from GitHub releases. The CLI is also available via npm (npm install -g opentunnel), Homebrew (brew install anomalyco/tap/opentunnel), AUR (opentunnel-bin) and Cargo (cargo install opentunnel-cli).
    Usecase: Installing the OpenTunnel CLI on a host.
    Category: Install
    Privileges: User
    OperatingSystem: Linux, MacOS
  - Command: opentunnel route add <SUBDOMAIN> <PORT>
    Description: Creates the tunnel on first use, routes <SUBDOMAIN>.<id>.opentunnel.xyz to 127.0.0.1:<PORT> and starts the background service.
    Usecase: Exposing a local service or application over the internet.
    Category: Access
    Privileges: User
    OperatingSystem: Linux, MacOS
  - Command: opentunnel route add @ <HOST>:<PORT>
    Description: Routes the tunnel's root hostname (<id>.opentunnel.xyz) to an arbitrary host and port reachable from the machine, such as another internal system.
    Usecase: Exposing internal network services through a compromised host.
    Category: Access
    Privileges: User
    OperatingSystem: Linux, MacOS
  - Command: opentunnel up
    Description: Creates the tunnel if needed and starts the background service. Where available it registers as a systemd user service (opentunnel-<profile>.service) or launchd agent (xyz.opentunnel.<profile>) that starts at login.
    Usecase: Persistent tunnel that survives logoff and reboot.
    Category: Persistence
    Privileges: User
    OperatingSystem: Linux, MacOS
  - Command: opentunnel serve
    Description: Runs the tunnel in the foreground instead of as a registered service, for containers or environments without systemd/launchd.
    Usecase: Running a tunnel inside a container or without leaving a service registration.
    Category: Access
    Privileges: User
    OperatingSystem: Linux, MacOS
Custom_Domain_Supported: False
Full_Path:
  - Path: ~/.config/opentunnel/<profile>.toml
  - Path: ~/.local/share/opentunnel/<profile>/
  - Path: ~/.local/state/opentunnel/<profile>/daemon.log
  - Path: $XDG_RUNTIME_DIR/opentunnel/<profile>.sock
  - Filename: opentunnel
Detection:
  - Domain: 'opentunnel.xyz'
  - Domain: '*.opentunnel.xyz'
  - Command: Execution of the opentunnel binary with route, up or serve arguments.
  - Command: Creation of an opentunnel-<profile>.service systemd unit or xyz.opentunnel.<profile> launchd agent.
Resources:
  - Link: https://opentunnel.xyz/
  - Link: https://github.com/anomalyco/opentunnel
  - Link: https://github.com/anomalyco/opentunnel/tree/master/packages/cli
---
