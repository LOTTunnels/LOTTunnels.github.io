---
Name: Neo-reGeorg
Description: Neo-reGeorg is an aggressive refactor of reGeorg, a self-hosted pivoting tool that generates an encrypted tunnel webshell (tunnel.php/jsp/jspx/aspx/ashx) uploaded to a compromised web server and opens a local SOCKS5 proxy that relays traffic through it into the internal network. Because the operator controls the compromised server, there is no vendor domain to block. It is heavily abused for webshell-based pivoting, tracked as MITRE ATT&CK S1189 and observed with the China-linked Houken/UNC5174 Ivanti CSA campaign, ChamelGang and Earth Estries, among others.
Author: cyberbuff
Created: 2026-09-22
Commands:
    - Command: python neoreg.py generate -k <KEY>
      Description: Generates the encrypted tunnel webshells (tunnel.php, tunnel.jsp, tunnel.jspx, tunnel.aspx, tunnel.ashx) keyed with a shared password for upload to a compromised web server.
      Usecase: Preparing the server-side webshell that the tunnel will relay through.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS

    - Command: python neoreg.py -k <KEY> -u http://<TARGET>/tunnel.php
      Description: Runs the client against the uploaded webshell, opening a local SOCKS5 proxy (default 127.0.0.1:1080) that relays traffic through the tunnel into the internal network.
      Usecase: Pivoting into an internal network through a compromised, internet-facing web server.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS
Custom_Domain_Supported: True
Full_Path:
    - Path: neoreg.py client script executed on the operator host, plus a generated tunnel.(php|jsp|jspx|aspx|ashx) webshell uploaded to the compromised web server.
Detection:
    - Command: "Execution of neoreg.py with the generate subcommand or with -k <key> -u <url>, and the presence of Neo-reGeorg tunnel.(php|jsp|jspx|aspx|ashx) webshell files on a web server."
Resources:
    - Link: https://github.com/L-codes/Neo-reGeorg
    - Link: https://attack.mitre.org/software/S1189/
---
