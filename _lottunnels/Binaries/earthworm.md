---
Name: EarthWorm
Description: EarthWorm (ew) is a small, portable SOCKS proxy/port-forwarding tool distributed as static binaries for most platforms. It is widely used as a pivoting tool because a single binary can act as a direct SOCKS server, a reverse SOCKS client that dials out to an operator host, or a relay that bridges the two, which is useful for reaching internal network segments from a compromised host that can only make outbound connections.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: ew -s ssocksd -l <LOCAL_PORT>
    Description: Runs a standalone SOCKS5 proxy directly on the compromised host.
    Usecase: Pivoting into the host's local network when the operator can reach the host directly.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: ew -s rcsocks -l <LISTEN_PORT> -e <RELAY_PORT>
    Description: Runs on the operator's host, listening for a reverse connection and exposing a SOCKS5 proxy once the target connects back.
    Usecase: Operator side of a reverse SOCKS5 pivot.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: ew -s rssocks -d <OPERATOR_IP> -e <RELAY_PORT>
    Description: Runs on the compromised host, dialing out to the operator's rcsocks listener to establish the reverse SOCKS5 tunnel.
    Usecase: Pivoting from a host that can only make outbound connections.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: ew
  - Filename: ew_for_linux64
  - Filename: ew_for_win.exe
  - Path: Downloaded/renamed ew binary, executed anywhere on the system.
Detection:
  - Command: Execution of a binary (often named ew, ew_for_* or a custom name) with -s ssocksd, rcsocks or rssocks arguments, together with -l, -d or -e.
  - Command: Outbound connections carrying SOCKS framing to an uncategorized host.
Resources:
  - Link: http://rootkiter.com/EarthWorm/
  - Link: https://github.com/rootkiter/EarthWorm
---
