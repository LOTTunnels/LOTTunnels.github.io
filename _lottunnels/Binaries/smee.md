---
Name: Smee.io
Description: Smee.io is a public webhook payload delivery service built around Server-Sent Events. The smee-client CLI forwards payloads received by a smee.io channel to a local URL, which gives a host behind NAT or a firewall a way to receive inbound HTTP callbacks without exposing a listening port.
Author: elhoim
Created: 2026-11-09
Commands:
  - Command: npx smee-client --url https://smee.io/<CHANNEL> --target http://localhost:<PORT>
    Description: Subscribes to a smee.io channel and forwards every payload it receives to a local HTTP endpoint.
    Usecase: Receiving inbound commands or data on a host that has no open inbound port, using smee.io as a one-way relay.
    Category: access
    Privileges: User
    OperatingSystem: Windows, Linux, MacOS
Full_Path:
  - Filename: smee-client
  - Path: npm-installed/npx-invoked smee-client, executed anywhere on the system.
Detection:
  - Domain: 'smee.io'
  - Command: Execution of smee-client (or npx smee-client) with --url pointing at smee.io and --target.
Resources:
  - Link: https://github.com/probot/smee-client
  - Link: https://smee.io
---
