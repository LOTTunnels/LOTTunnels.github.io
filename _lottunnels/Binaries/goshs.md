---
Name: goshs
Description: goshs is a simple, single-binary HTTP file server written in Go. It has a built-in tunnel option that publishes the served directory to the internet through the localhost.run service, without any account or additional client.
Author: Kamran Saifullah
Created: 2026-10-27
Commands:
  - Command: goshs --tunnel
    Description: Starts goshs and exposes the served directory through a localhost.run tunnel. goshs logs a public URL on a random lhr.life subdomain that anyone with the link can reach. TLS (-s) must not be used since the tunnel requires plaintext. Short form is "goshs -t".
    Usecase: Exposing a local file server to the internet for file download, upload or exfiltration without installing a separate tunneling client.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Custom_Domain_Supported: False
Full_Path:
  - Filename: goshs
Detection:
  - Domain: '*.lhr.life'
  - Domain: '*.localhost.run'
  - Command: Execution of goshs with "--tunnel" or "-t" argument.
Resources:
  - Link: https://docs.goshs.de/usage/tunnel/index.html
  - Link: https://github.com/patrickhener/goshs
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
---
