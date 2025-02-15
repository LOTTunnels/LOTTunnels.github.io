Name: localhost.run
Description: localhost.run is a client-less tool to instantly make a locally running application available on an internet accessible URL.
Author: Kirill Magaskin
Created: 2025-02-15
Commands:
  - Command: ssh -R 80:127.0.0.1:<PORT> localhost.run
    Description: This is quick way to start the localhost.run and connect local PORT to internet domain. If you are using a free tunnel you can skip the SSH key check by adding "nokey" as your SSH user (use [USERNAME]@localhost.run instead of localhost.run) otherwise you need to upload your public SSH key to https://admin.localhost.run/.
    Usecase: Quick execution of localhost.run.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

Detection:
  - Domain: '*.localhost.run'
  - Command: Execution of ssh with "localhost.run" argument.
Resources:
  - Link: https://localhost.run/docs
Acknowledgement:
  - Person: Kirill Magaskin
    Handle: '@k1rpi7ch'