---
Name: Netsh PortProxy
Description: The Windows built-in netsh utility can configure a port proxy (interface portproxy) that forwards TCP connections from a listening address and port to another host and port. No additional binary is required and the rule survives reboots.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=<PORT> connectaddress=<TARGET_IP> connectport=<TARGET_PORT>
    Description: Forwards inbound connections on the compromised host to an internal system, turning it into a pivot or relay.
    Usecase: Pivoting to internal hosts using only built-in tooling.
    Category: access
    Privileges: Administrator
    OperatingSystem: Windows

  - Command: netsh interface portproxy show all
    Description: Lists configured port proxy rules. Useful for both attackers and defenders.
    Usecase: Enumerating existing forwards.
    Category: access
    Privileges: User
    OperatingSystem: Windows
Full_Path:
  - Path: C:\Windows\System32\netsh.exe
  - Path: C:\Windows\SysWOW64\netsh.exe
Detection:
  - Command: Execution of netsh.exe with the "interface portproxy add" arguments (also the shorthand "int p a v4tov4").
  - Command: Registry values created under HKLM\SYSTEM\CurrentControlSet\Services\PortProxy\v4tov4\tcp (and v6tov4, v4tov6, v6tov6).
  - Command: Unexpected listening sockets owned by the IP Helper service (iphlpsvc), typically svchost.exe.
Resources:
  - Link: https://learn.microsoft.com/en-us/windows-server/networking/technologies/netsh/netsh-interface-portproxy
  - Link: https://attack.mitre.org/techniques/T1090/001/
---
