vcsa.service
============

VCSA Ansible role to restart vCenter services


Role Variables
--------------
| Name | Description | Mandatory | Type
| -------------- | ------------------------------------------ | --------- | ------ |
| vcenter | vcenter FQDN or IP | true | string
| service | vcenter service to restart | true | string

Role Structure
--------------

```bash
.
├── defaults
│   └── main.yml
├── files
├── handlers
│   ├── main.yml
│   └── vmware_vcsa_service_restart.yml
├── meta
│   └── main.yml
├── README.md
├── tasks
│   ├── main.yml
│   └── vmware_service_restart.yml
├── templates
├── tests
│   ├── inventory
│   └── test.yml
└── vars
    └── main.yml

8 directories, 10 files
```


Example Playbook
----------------
```yaml
# Author: Julian Wendland
#
---

- name: Schedule vcsa backup
  hosts: localhost
  connection: local

  vars_files:
    - /home/jw/github/AnsibleRoles/vcsa/roles/vcsa.general/vault/secrets.yml

  roles:
    - { role: vcsa.general, vcenter: 10.0.20.94 }
    - { role: vcsa.service, vcenter: 10.0.20.94 }
...
```


Author Information
------------------
Julian Wendland
Soeldner Consult GmbH
09.02.2021

