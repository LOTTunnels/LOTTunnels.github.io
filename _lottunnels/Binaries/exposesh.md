Name: Expose.sh
Description: EXPOSE is your new favourite open source tool for exposing your local services on the public Internet.
Author: Kirill Magaskin
Created: 2025-02-15
Commands:
  - Command: ssh -R 1:127.0.0.1:<PORT> expose.sh
    Description: This is quick way to start the localhost.run and connect local PORT to internet domain. By default, authentication is done by using the public SSH keys you have on your GitHub account. If you use a different username on your computer than the one you use on GitHub, add the GitHub username to your SSH command (use [USERNAME]@expose.sh instead of expose.sh)
    Usecase: Quick execution of expose.sh.
    Category: Access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

Detection:
  - Domain: 'expose.sh'
  - Domain: '*.expos.es'
  - Command: Execution of ssh with "expose.sh" argument.
Resources:
  - Link: https://github.com/exposesh
Acknowledgement:
  - Person: Kirill Magaskin
    Handle: '@k1rpi7ch'