---
Name: wstunnel
Description: wstunnel tunnels TCP or UDP traffic over WebSocket or HTTP2 to an operator-run wstunnel server, blending tunneled traffic with ordinary web traffic to bypass firewalls and DPI. Because the server is self-hosted, there is no vendor domain to block. It has been observed in intrusions by Scattered Spider/UNC3944 and Octo Tempest, and in the China-aligned Shadow-Earth-053 espionage campaign.
Author: cyberbuff
Created: 2026-09-17
Commands:
    - Command: wstunnel server wss://0.0.0.0:8080
      Description: Starts the operator-controlled wstunnel server, accepting client tunnels over WebSocket Secure.
      Usecase: Standing up the WebSocket tunnel endpoint that compromised hosts connect to.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS

    - Command: wstunnel client -L socks5://127.0.0.1:1080 wss://<SERVER>:8080
      Description: Connects to the wstunnel server over WebSocket and exposes a local SOCKS5 proxy, routing traffic into the tunnel to bypass firewalls and DPI.
      Usecase: Establishing a SOCKS pivot tunneled over WebSocket.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS

    - Command: wstunnel client -L tcp://2222:127.0.0.1:22 wss://<SERVER>:8080
      Description: Forwards a local TCP port over the WebSocket tunnel to a remote service such as SSH, reaching it through the operator-controlled server.
      Usecase: Reaching an internal service through a WebSocket tunnel.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS
Custom_Domain_Supported: True
Full_Path:
    - Path: Downloaded/Installed wstunnel binary (single executable acting as client and server), executed anywhere on the system.
Detection:
    - Command: Execution of the wstunnel binary with client/server subcommands, or WebSocket upgrade traffic to an operator-controlled host used as a tunnel.
Resources:
    - Link: https://github.com/erebe/wstunnel
    - Link: https://www.microsoft.com/en-us/security/blog/2023/10/25/octo-tempest-crosses-boundaries-to-facilitate-extortion-encryption-and-destruction/
    - Link: https://www.trendmicro.com/en_us/research/26/d/inside-shadow-earth-053.html
---
