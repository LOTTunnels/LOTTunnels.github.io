---
Name: Tunna
Description: Tunna is a set of tools for tunneling TCP traffic over HTTP, pairing a Python client (proxy.py) with a server-side component (ASPX, PHP, JSP or ASP) uploaded to a compromised web application server. It can tunnel traffic outbound through packet-inspecting firewalls, and the same mechanism works anywhere a web shell could be deployed. Tunna is the predecessor to the project's own reGeorg.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: python proxy.py -u <REMOTE_URL> -l <LOCAL_PORT>
    Description: Runs the client on the operator host, forwarding a local port through the uploaded server-side component on the compromised web application server.
    Usecase: Tunneling RDP, SSH or another TCP service through a compromised web application server.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: python proxy.py -u <REMOTE_URL> -l <LOCAL_PORT> -r <RDP_PORT> -b 8192
    Description: Variant tuned for tunneling RDP traffic, with an adjusted buffer size.
    Usecase: Tunneling RDP through a compromised web application server.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: proxy.py
  - Filename: webserver.py
  - Path: Tunna client script on the operator host, plus an uploaded ASPX/PHP/JSP/ASP tunnel component on the compromised web server.
Detection:
  - Command: Execution of proxy.py with -u and -l arguments, and the presence of a Tunna-style tunnel web shell (ASPX/PHP/JSP/ASP) on a web server.
  - Command: Sustained HTTP request/response traffic to a specific web application path, carrying encapsulated TCP connection data rather than ordinary page content.
Resources:
  - Link: https://github.com/SECFORCE/Tunna
  - Link: https://attack.mitre.org/techniques/T1572/
---
