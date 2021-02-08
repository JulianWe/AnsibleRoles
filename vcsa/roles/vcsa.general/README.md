vcsa.general
===========

VCSA Ansible role to handle all generell tasks regarding vCenter Server

Role Variables
--------------
| Name | Description | Mandatory | Type
| -------------- | ------------------------------------------ | --------- | ------ |
| vcenter | vcenter FQDN or IP | true | string
| vcUsername | vCenter username | true | string
| vcPassword | vCenter password | true | string


Role Structure
--------------

```bash.
├── defaults
│   └── main.yml
├── files
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── README.md
├── tasks
│   ├── main.yml
│   └── vmware_vcsa_rest_login.yml
├── templates
├── tests
│   ├── inventory
│   └── test.yml
├── vars
│   └── main.yml
└── vault
    └── secrets.yml

9 directories, 10 files
```


Example Playbook
----------------
```yaml
---
- name: login via REST API
  hosts: localhost
  connection: local

  vars_files:
    - /home/jw/github/AnsibleRoles/vcsa/roles/vcsa.general/vault/secrets.yml

  roles:
    - roles/vcsa.general
```


Author Information
------------------
Julian Wendland
Soeldner Consult GmbH
09.02.2021
