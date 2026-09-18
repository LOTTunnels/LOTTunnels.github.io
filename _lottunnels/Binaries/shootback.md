---
Name: Shootback
Description: Shootback is a self-hosted reverse TCP tunnel written in Python that lets an operator reach a service on a host behind NAT or a firewall. A slaver runs on the internal host and connects out to an operator-run master, which exposes the tunneled service. Because both ends are operator-run, there is no vendor domain to block. It has been observed in MuddyWater/Seedworm post-exploitation activity.
Author: cyberbuff
Created: 2026-09-17
Commands:
    - Command: python master.py -m 0.0.0.0:10000 -c 0.0.0.0:10080
      Description: Runs the operator-controlled master, listening for slaver connections on one port and exposing the tunneled service to customers on another.
      Usecase: Standing up the tunnel endpoint that internal hosts connect back to.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS

    - Command: python slaver.py -m <MASTER_IP>:10000 -t 127.0.0.1:22
      Description: Runs on the host behind NAT, connecting out to the master and forwarding a local service such as SSH (22) so it becomes reachable through the master.
      Usecase: Exposing an internal service to the operator through the reverse tunnel.
      Category: Access
      Privileges: User
      OperatingSystem: Windows, Linux, MacOS
Custom_Domain_Supported: True
Full_Path:
    - Path: master.py and slaver.py Python scripts (or PyInstaller-packaged binaries) executed anywhere on the system.
Detection:
    - Command: Execution of master.py / slaver.py (or packaged equivalents), particularly with -m master and -t target arguments.
Resources:
    - Link: https://github.com/aploium/shootback
    - Link: https://documents.trendmicro.com/assets/white_papers/wp_new_muddywater_findings_uncovered.pdf
---
