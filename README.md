# Ansible Worker Node Provisioning role [![Build Status](https://travis-ci.org/EGI-Foundation/ansible-role-wn.svg?branch=master)](https://travis-ci.org/EGI-Foundation/ansible-role-wn) [![Maintainability](https://api.codeclimate.com/v1/badges/d6a249676a9d0a1894aa/maintainability)](https://codeclimate.com/github/EGI-Foundation/ansible-role-wn/maintainability)


This is an Ansible role for the provisioning of a UMD worker node.
It ensures that the relevant repositories are installed and configured and that the worker-node metapackage is installed.

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
         - { role: EGI-Foundation.voms-client }
         - { role: EGI-foundation.wn }
```

## License

Apache-2.0

## Author Information

See [`AUTHORS.md`](AUTHORS.md)