---
Name: Dns2tcp
Description: Dns2tcp relays TCP connections over DNS queries and responses. A server authoritative for a domain exposes configured "resources" (for example an SSH or SSL endpoint), and a client resolves a chosen resource through any DNS server that can reach it, which allows traffic out through networks that only permit DNS.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: dns2tcpd -F -d 1
    Description: Starts the dns2tcpd server using ~/.dns2tcprc-style configuration (domain, key and resources such as ssh:127.0.0.1:22).
    Usecase: Operator side of a DNS tunnel exposing an internal service.
    Category: access
    Privileges: Administrator/root
    OperatingSystem: Linux, MacOS, BSD

  - Command: dns2tcpc -r <RESOURCE> -l <LOCAL_PORT> -k <KEY> -z <TUNNEL_DOMAIN> <DNS_SERVER>
    Description: Connects to a named resource on the server and exposes it as a local TCP port, tunneled through DNS queries to the given domain.
    Usecase: Reaching an internal service (SSH, a web shell, etc.) over DNS from a network that blocks other outbound protocols.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: dns2tcpd
  - Filename: dns2tcpc
  - Path: ~/.dns2tcprc and ~/.dns2tcpdrc configuration files
Detection:
  - Command: Execution of dns2tcpc with -r/-l/-k/-z arguments, or dns2tcpd with a configuration file defining domain/key/resources.
  - Command: High-volume or high-entropy TXT/CNAME/NULL DNS query and response traffic to a single authoritative domain, inconsistent with normal resolution.
Resources:
  - Link: https://github.com/alex-sector/dns2tcp
---
