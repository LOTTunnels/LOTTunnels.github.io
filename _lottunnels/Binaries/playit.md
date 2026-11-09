---
Name: playit.gg
Description: playit.gg is a SaaS tunneling service originally aimed at game server hosting. The playit agent installs as a background service (Windows service, macOS LaunchAgent, or systemd/OpenRC unit on Linux) that keeps outbound tunnels online and reconnects automatically, exposing local TCP/UDP ports through playit's edge network.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: playit
    Description: Starts the command-line agent, which signs in (or resumes an existing agent secret) and keeps configured tunnels online.
    Usecase: Exposing a local TCP/UDP service to the internet through playit's edge network.
    Category: exfiltrate
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: playitd
    Description: The background service/daemon installed alongside the agent, which keeps tunnels online across reboots without user interaction.
    Usecase: Persistent outbound tunnel that survives reboots.
    Category: persistence
    Privileges: Administrator/root
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: playit
  - Filename: playitd
  - Filename: playit-windows-x86_64.exe
  - Path: '%ProgramData%\playit_gg\logs'
  - Path: '~/Library/Application Support/playit_gg/playit.toml'
  - Path: '/etc/playit (Linux service configuration)'
Detection:
  - Domain: '*.playit.gg'
  - Domain: '*.ply.gg'
  - Command: Execution of playit or playitd, or installation of the playit.gg/playitd Windows service, LaunchAgent or systemd/OpenRC unit.
Resources:
  - Link: https://github.com/playit-cloud/playit-agent
  - Link: https://playit.gg
---
