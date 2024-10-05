---
Name: Visual Studio Code Server (code.exe)
Description: Utilizing installed Visual Studio Code Server Tunnels for exposing local development environment over the internet.
Author: Kamran Saifullah
Created: 2024-10-05
Commands:
  - Command: code.exe tunnels
    Description: Generating Visual Studio Code Server Tunnels via installed VSCode built in Tunneling functionality.
    Usecase: Generating Visual Studio Code Server Tunnels for exposing local dev environemnt over the internet.
    Category: exfiltrate
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: Accessing generated Visual Studio Code Server Tunnels URL. 
    Description: Insider threat, external threat actor will be accessing the link in the web browser providing access to the `vscode.dev\tunnels\*` proxying the local development environment.
    Usecase: Accessing local files on VSCode Cloud for Data Exfiltration.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: Shell Access via Visual Studio Code Server Tunnels.
    Description: Insider threat, external threat actor will be able to run commands on local system proxying via Miscrofot domains using the built-in VSCode Server Terminal. 
    Usecase: Accessing & Deleting files, executing payloads, downloading payloads, running malware/ransomware etc.
    Category: shell-access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

Full_Path:
  - Path: Installed Visual Studio Code - Custom Path.
  - Path: Visual Studio Code added into the PATH variable.
Detection:
  - Domain: 'https://vscode.dev/tunnel/*'
  - Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_devtunnels_communication.yml
Resources:
  - Link: https://cydefops.com/vscode-data-exfiltration
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
---
