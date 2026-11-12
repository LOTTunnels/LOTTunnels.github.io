---
Name: Ptunnel-ng
Description: Ptunnel-ng is a maintained fork of the original ptunnel. It tunnels TCP connections (most commonly SSH) through ICMP echo request/reply packets via a proxy host, allowing traffic to pass through firewalls that permit outbound ping but block other protocols.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: sudo ptunnel-ng -r<DESTINATION_IP> -R<DESTINATION_PORT>
    Description: Runs the proxy on an operator-controlled host, forwarding incoming ICMP-tunneled connections to the given destination and port (for example an SSH server on the compromised network).
    Usecase: Proxy side of an ICMP tunnel used as a reverse pivot into an internal service.
    Category: access
    Privileges: Administrator/root
    OperatingSystem: Linux, MacOS, Windows

  - Command: sudo ptunnel-ng -p<PROXY_IP> -l<LOCAL_PORT> -r<DESTINATION_IP> -R<DESTINATION_PORT>
    Description: Client side. Opens a local TCP listener that is tunneled over ICMP to the proxy, which forwards it to the destination host and port.
    Usecase: Tunneling SSH or another TCP service through a firewall that only permits ICMP.
    Category: access
    Privileges: Administrator/root
    OperatingSystem: Linux, MacOS, Windows
Full_Path:
  - Filename: ptunnel-ng
  - Filename: ptunnel-ng.exe
  - Path: Compiled/downloaded ptunnel-ng binary, executed anywhere on the system.
Detection:
  - Command: Execution of ptunnel-ng (or ptunnel) with -p, -l, -r or -R arguments, requiring raw socket/administrator privileges.
  - Command: Sustained bidirectional ICMP echo request/reply traffic carrying encoded payload data to or from a single host, outside normal ping usage.
Resources:
  - Link: https://github.com/utoni/ptunnel-ng
---
