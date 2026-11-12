---
Name: AWS SSM Session Manager
Description: AWS Systems Manager Session Manager provides shell access and port forwarding to managed instances over HTTPS, without open inbound ports or SSH keys. With sufficient IAM permissions it allows tunnelling to RDP, SSH or database ports on EC2 and hybrid-activated systems, using traffic to AWS endpoints that organizations commonly allow.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: aws ssm start-session --target <INSTANCE_ID> --document-name AWS-StartPortForwardingSession --parameters portNumber=3389,localPortNumber=3389
    Description: Forwards a local port to a port on the instance through the SSM channel.
    Usecase: Reaching RDP, SSH or other services on an instance with no inbound access.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: aws ssm start-session --target <INSTANCE_ID> --document-name AWS-StartPortForwardingSessionToRemoteHost --parameters host=<INTERNAL_HOST>,portNumber=<PORT>,localPortNumber=<LOCAL_PORT>
    Description: Forwards through the instance to another host reachable from it, using the instance as a pivot.
    Usecase: Pivoting into private subnets and databases.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS

  - Command: aws ssm start-session --target <INSTANCE_ID>
    Description: Interactive shell on the instance.
    Usecase: Shell access that bypasses SSH and network security groups.
    Category: shell-access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: session-manager-plugin
  - Filename: session-manager-plugin.exe
  - Filename: aws
  - Filename: aws.exe
Detection:
  - Domain: 'ssm.*.amazonaws.com'
  - Domain: 'ssmmessages.*.amazonaws.com'
  - Domain: 'ec2messages.*.amazonaws.com'
  - Command: Execution of session-manager-plugin, or aws ssm start-session with AWS-StartPortForwarding* documents, from hosts that do not normally administer AWS.
  - Command: CloudTrail StartSession events (ssm.amazonaws.com), including the document name and target in requestParameters.
Resources:
  - Link: https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html
  - Link: https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-sessions-start.html
---
