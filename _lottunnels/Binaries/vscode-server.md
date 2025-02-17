---
Name: VSCode CLI
Description: Utilizing Visual Studio Code Remote Tunnels for exposing local development environment over the internet.
Author: Kamran Saifullah
Created: 2024-10-05
Commands:
  - Command: code.exe tunnel --accept-server-license-terms
    Description: Generating Visual Studio Code Server Tunnels via VSCode built in Tunneling functionality.
    Usecase: Generating Visual Studio Code Server Tunnels for exposing local dev environemnt over the internet.
    Category: exfiltrate
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: code.exe tunnel service install --accept-server-license-terms
    Description: Generating Visual Studio Code Server Tunnels via VSCode built in Tunneling functionality and installing it as a service.
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
    Description: Insider threat, external threat actor will be able to run commands on local system proxying via Microsoft domains using the built-in VSCode Server Terminal. 
    Usecase: Accessing & Deleting files, executing payloads, downloading payloads, running malware/ransomware etc.
    Category: shell-access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

Full_Path:
  - Path: \%UserProfile%\vscode-cli\code_tunnel.json
  - Path: code.exe (standalone executable)
Detection:
  - Domain: '*.devtunnels.ms*'
  - Domain: '*.tunnels.api.visualstudio.com'
  - Domain: 'https://vscode.dev/tunnel/*'
  - Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_devtunnels.yml
  - Command: Execution of the binary with arguments.
Resources:
  - Link: https://code.visualstudio.com/docs/remote/tunnels
  - Link: https://cydefops.com/vscode-data-exfiltration
  - Link: https://www.bleepingcomputer.com/news/security/chinese-hackers-use-visual-studio-code-tunnels-for-remote-access/
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
  - Person: Kirill Magaskin
    Handle: '@k1rpi7ch'
---
