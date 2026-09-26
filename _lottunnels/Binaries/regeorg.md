---
Name: reGeorg
Description: reGeorg is the successor to reDuh, a self-hosted pivoting tool that uploads a tunnel webshell (tunnel.aspx/ashx/jsp/php) to a compromised, internet-facing web server and opens a local SOCKS proxy on the operator's machine that relays traffic through it into the DMZ or internal network. Because the operator controls the compromised server, there is no vendor domain to block. It is heavily abused for tunneling into segmented networks over legitimate-looking web traffic, tracked as MITRE ATT&CK S1187 and observed with SamSam and Exchange server intrusions, among others.
Author: cyberbuff
Created: 2026-09-22
Commands:
    - Command: python reGeorgSocksProxy.py -p 8080 -u http://<TARGET>/tunnel/tunnel.jsp
      Description: Runs the reGeorg client, opening a local SOCKS proxy on port 8080 that relays traffic through the tunnel webshell hosted on the compromised web server.
      Usecase: Pivoting into an internal network through a compromised, internet-facing web server.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS
Custom_Domain_Supported: True
Full_Path:
    - Path: reGeorgSocksProxy.py client script executed on the operator host, plus a tunnel.(aspx|ashx|jsp|php) webshell uploaded to the compromised web server.
Detection:
    - Command: "Execution of reGeorgSocksProxy.py with -u pointing at a tunnel webshell, and the presence of tunnel.aspx/tunnel.ashx/tunnel.jsp/tunnel.php (including tunnel.nosocket.php) webshell files on a web server."
Resources:
    - Link: https://github.com/sensepost/reGeorg
    - Link: https://attack.mitre.org/software/S1187/
---
