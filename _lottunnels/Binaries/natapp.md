---
Name: NATApp
Description: NATApp is a Chinese ngrok-based SaaS tunneling service that exposes a local port under a generated natappfree.cc (free tier) or custom domain. It is widely used in Chinese developer tutorials for exposing local web services and WeChat callback endpoints, and is a plausible exfiltration or C2 channel for hosts reachable from a Chinese network.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: natapp -authtoken=<AUTHTOKEN>
    Description: Starts the client using a tunnel authtoken obtained from the NATApp dashboard, exposing the configured local port under a natappfree.cc (free tier) or reserved domain.
    Usecase: Exposing a local file system, web application, or phishing page over the internet.
    Category: Phishing
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: natapp
  - Filename: natapp.exe
  - Path: config.ini (authtoken configuration file in the same directory as the binary)
Detection:
  - Domain: '*.natappfree.cc'
  - Command: Execution of natapp with -authtoken, or launched with a config.ini containing an authtoken value.
Resources:
  - Link: https://natapp.cn/
---
