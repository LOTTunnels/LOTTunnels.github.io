---
Name: sshx
Description: sshx is a web-based collaborative terminal sharing tool. Running a single command shares the current terminal session as a link served through sshx's hosted relay mesh (sshx.io), letting anyone with the link view and type into the session from a browser.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: sshx
    Description: Shares the current terminal session and prints a URL on sshx.io that gives interactive access to it.
    Usecase: Giving an operator interactive shell access to a compromised host through a browser, without installing a dedicated remote-access agent.
    Category: shell-access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: sshx
  - Path: Downloaded sshx binary (via "curl -sSf https://sshx.io/get | sh"), executed anywhere on the system.
Detection:
  - Domain: 'sshx.io'
  - Command: Execution of the sshx binary with no arguments, or via "curl ... sshx.io/get | sh" / "sshx.io/get | sh -s run".
Resources:
  - Link: https://github.com/ekzhang/sshx
  - Link: https://sshx.io
---
