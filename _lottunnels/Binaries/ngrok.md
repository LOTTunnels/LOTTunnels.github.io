---
Name: ngrok
Description: Insiders as well as threat actors can ingress into an environment via ngrok, which functions as a reverse proxy. ngrok is no longer open source but the previous source code is still available (linked below).
Author: Dan O'Day
Created: 2025-01-31
Commands:
  - Command: ngrok authtoken 'AUTHTOKEN_GOES_HERE'
    Description: Initial ngrok configuration.
    Usecase: Configures ngrok to use specified authentication token.
    Category: Install
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: ngrok tcp|http <PORT>
    Description: Sends connection to configured upstream service on port.
    Usecase: Establishes reverse proxy via ngrok edge.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

Full_Path:
  - Path: ngrok.exe (standalone executable)
  - Path: ngrok (standalone executable)
Detection:
  - Domain: ngrok.com
  - Domain: ngrok.io
  - Sigma: https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ngrok_network_sigma.yml
  - Sigma: https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ngrok_processes_sigma.yml
Resources:
  - Link: https://ngrok.com
  - Link: https://github.com/ngrok/ngrok
  - Link: https://github.com/inconshreveable/ngrok
Acknowledgement:
  - Person: Dan O'Day
    Handle: '@4n68r'
---
