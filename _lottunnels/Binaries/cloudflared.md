---
Name: Cloudflare ArgoTunnels/Cloudflared - cloudflared.exe
Description: Cloudflared is provided by CloudFlare which is a cyber security company. This tool works in a similar fashion to others and allows insiders as well as threat actors for data exfiltration.
Author: Kamran Saifullah
Created: 2024-10-05
Commands:
  - Command: cloudflared.exe tunnel --url <IP>:<PORT>
    Description: This will generate tunnels link. However, a local server on the same port is required to exfiltrate the data.
    Usecase: Exposing local file system over the internet.
    Category: exfiltrate
    Privileges: User
    OperatingSystem: Windows, Mac, Linux
  - Command: cloudflared.exe tunnel --url <IP>:<PORT>
    Description: By hosting a local server running a Phishing Website it is possible to expose it via CloudFlare URLs/Domains.
    Usecase: Hosting phishing sites locally and exposing them via CloudFlare URLs.
    Category: Phishing
    Privileges: User
    OperatingSystem: Windows, Mac, Linux
Full_Path:
  - Path: Downloaded version of cloudflared, which gets executed anywhere on the system.
Detection:
  - Domain: '*.trycloudflare.com'
Resources:
  - Link: https://defr0ggy.github.io/research/Abusing-Cloudflared-A-Proxy-Service-To-Host-&-Share-Apps/
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
---