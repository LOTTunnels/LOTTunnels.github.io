---
Name: Rust LocalTunnels
Description: LocalTunnels a.k.a Rust Tunnels is an extension of LocalTunnels implemented in Rust Language. Similar to LocalTunnels, this can also be used by insiders as well as threat actors to exfiltrate data, download malciious binaries, malwares etc. Also, the rlt can be hosted on a custom server, thus the binary itself is required to be monitored as well as having network monitoring. 
Author: Kamran Saifullah
Created: 2024-10-13
Commands:

  - Command: cargo install localtunnel
    Description: This is a quick way to install localtunnel rust binary on the local machine.
    Usecase: Installation of rlt.
    Category: install
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: localtunnel client --host <host name> --subdomain <subdomain> --port <local port>
    Description: This is a quick way to connect to the hosted server running localtunnel rlt service binded to the port.
    Usecase: Connecting to malicious server hosting localtunnel rlt service.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: localtunnel server --domain init.so --port <local port> --proxy-port <proxy port> --secure
    Description: Running rlt on the server for malicious purposes.
    Usecase: Hosting and exposing the server which will then be connected by the client.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

Full_Path:
  - Path: Quick Start/Installed version of LocalTunnels rlt, which gets executed anywhere on the system.
Custom_Domain_Supported_: True
Detection:
  - Domain: '*.loca.lt'
  - Domain: '*.localtunnel.me'
  - Commands: Execution of the binary and/or with arguments.
Resources:
  - Link: https://github.com/kaichaosun/rlt
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
---