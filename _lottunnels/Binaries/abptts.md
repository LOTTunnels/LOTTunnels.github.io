---
Name: ABPTTS
Description: ABPTTS (A Black Path Toward The Sun) tunnels TCP traffic over HTTP/HTTPS using a Python client script paired with a JSP/WAR or ASP.NET server-side component deployed to a web application server. Anywhere a web shell could be deployed, ABPTTS can instead establish a full TCP tunnel, which has been used to carry RDP, interactive SSH and other TCP-based access through a compromised web application server.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: python abpttsclient.py -c <CONFIG_FILE> -u <FORWARDINGURL> -f <LOCALHOST>:<LOCALPORT>/<TARGETHOST>:<TARGETPORT>
    Description: Runs the client on the operator host, forwarding a local port through the uploaded server-side component to a destination host/port reachable from the web application server.
    Usecase: Tunneling RDP, SSH or another TCP service through a compromised web application server.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: abpttsclient.py
  - Filename: abpttsfactory.py
  - Path: ABPTTS client script on the operator host, plus a generated JSP/WAR or ASP.NET tunnel component uploaded to the compromised web application server.
Detection:
  - Command: Execution of abpttsclient.py with -c/-u/-f arguments, and the presence of an ABPTTS-generated server-side component (JSP/WAR package or ASP.NET handler) on a web application server.
  - Command: Sustained HTTP/HTTPS request/response traffic to a specific web application server path, carrying encapsulated TCP connection data rather than ordinary page content.
Resources:
  - Link: https://github.com/nccgroup/ABPTTS
  - Link: https://attack.mitre.org/techniques/T1572/
---
