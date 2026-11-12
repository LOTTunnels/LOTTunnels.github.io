---
Name: Azure Bastion Native Client Tunnel
Description: Azure Bastion with the native client feature allows the Azure CLI to open a local tunnel to a VM port through the Bastion host. It gives users SSH and RDP-style access to private VMs from a workstation without a VPN or public IP.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: az network bastion tunnel --name <BASTION> --resource-group <RG> --target-resource-id <VM_ID> --resource-port 22 --port <LOCAL_PORT>
    Description: Creates a local listener that forwards to the target VM through Azure Bastion.
    Usecase: Reaching private VMs and tunnelling arbitrary TCP ports.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: az network bastion ssh --name <BASTION> --resource-group <RG> --target-resource-id <VM_ID> --auth-type ssh-key --username <USER> --ssh-key <KEY>
    Description: SSH to a VM through Bastion using the CLI.
    Usecase: Shell access to private VMs.
    Category: shell-access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: az
  - Filename: az.cmd
Detection:
  - Command: Execution of az network bastion tunnel, ssh or rdp from hosts that do not normally manage Azure resources.
  - Command: Azure Activity and Bastion diagnostic logs showing new users or source IP addresses connecting.
Resources:
  - Link: https://learn.microsoft.com/en-us/azure/bastion/native-client
---
