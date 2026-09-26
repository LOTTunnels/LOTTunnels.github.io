---
Name: suo5
Description: suo5 is a self-hosted, high-performance HTTP proxy tunnel that uses bidirectional chunked-encoding over a single connection to relay traffic through a webshell (jsp/php/aspx) uploaded to a compromised web server, giving the operator a local SOCKS5 proxy into the internal network. Because the operator controls the compromised server, there is no vendor domain to block. It is abused for webshell-based pivoting, observed with the China-linked Houken/UNC5174 Ivanti CSA campaign and the JadeProx China-nexus operation, among others.
Author: cyberbuff
Created: 2026-09-22
Commands:
    - Command: suo5 -t http://<TARGET>/suo5.jsp -l 127.0.0.1:1111
      Description: Runs the suo5 client against an uploaded webshell, opening a local SOCKS5 proxy (default 127.0.0.1:1111) that relays traffic full-duplex over HTTP into the internal network.
      Usecase: Pivoting into an internal network through a compromised, internet-facing web server.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS

    - Command: suo5 -t http://<TARGET>/suo5.jsp -r http://<REDIRECT>/suo5.jsp
      Description: Connects through a redirect webshell, allowing the tunnel to traverse multi-layer reverse proxies and load balancers in front of the target.
      Usecase: Pivoting through targets fronted by load balancers or layered reverse proxies.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS
Custom_Domain_Supported: True
Full_Path:
    - Path: Downloaded suo5 CLI or GUI binary executed on the operator host, plus a suo5 webshell (jsp/php/aspx) uploaded to the compromised web server.
Detection:
    - Command: "Execution of the suo5 binary with -t pointing at a webshell URL (optionally -r and -l), and the presence of suo5 jsp/php/aspx webshell files on a web server."
Resources:
    - Link: https://github.com/zema1/suo5
    - Link: https://www.cert.ssi.gouv.fr/cti/CERTFR-2025-CTI-009/
---
