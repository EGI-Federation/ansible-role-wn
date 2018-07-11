# Ansible Worker Node Provisioning role [![Build Status](https://travis-ci.org/EGI-Foundation/ansible-role-wn.svg?branch=master)](https://travis-ci.org/EGI-Foundation/ansible-role-wn)


This is an Ansible role for the provisioning of a UMD worker node.
It ensures that the relevant repositories are installed and configured.

## Requirements

No specific requirements

## Role Variables

None yet.

## Dependencies

This role uses the following roles as dependencies:

- EGI-Foundation.umd
- EGI-Foundation.voms-client

## Example Playbook

```yaml
    - hosts: worker-nodes
      roles:
         - { role: EGI-Foundation.umd, release: 4}
         - { role: EGI-foundation.wn }
```

## License

Apache-2.0

## Author Information

See [`AUTHORS.md`](AUTHORS.md)