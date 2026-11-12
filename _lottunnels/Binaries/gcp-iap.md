---
Name: GCP IAP TCP Forwarding
Description: Identity-Aware Proxy (IAP) TCP forwarding in Google Cloud tunnels SSH, RDP or arbitrary TCP connections to VMs through Google's endpoints, without public IPs on the target. With the right IAM permissions it can be used as an access path that is difficult to distinguish from administration.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: gcloud compute start-iap-tunnel <INSTANCE> <PORT> --local-host-port=localhost:<LOCAL_PORT> --zone=<ZONE>
    Description: Opens a local listener that forwards to the given port on the instance over IAP.
    Usecase: Reaching internal VMs and services that have no external IP.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: gcloud compute ssh <INSTANCE> --tunnel-through-iap --zone=<ZONE>
    Description: SSH to an instance through IAP.
    Usecase: Shell access to private instances.
    Category: shell-access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: gcloud
  - Filename: gcloud.cmd
Detection:
  - Domain: 'tunnel.cloudproxy.app'
  - Command: Execution of gcloud with start-iap-tunnel or --tunnel-through-iap.
  - Command: Cloud Audit Logs for IAP TCP forwarding (iap.googleapis.com) showing new principals or source IP addresses.
Resources:
  - Link: https://cloud.google.com/iap/docs/using-tcp-forwarding
---
