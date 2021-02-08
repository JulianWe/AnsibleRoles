vcsa.vm.snapshot
================

This Role is used to handle VM Snapshots



Role Variables
--------------
| Name           | Description                                | Mandatory | Type   |
| -------------- | ------------------------------------------ | --------- | ------ |
| datacenter | Datacenter Name | true | string
| vmNameToSnap | Name der VM von der ein Snapshot gemacht werden soll | true | string
| vc1Fqdn | FQDN from Managment vCenter | true | string
| snapshot | Name des Snapshots | true | string


Role Structure
--------------

```bash
.
├── defaults
│   └── main.yml
├── files
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── README.md
├── tasks
│   ├── main.yml
│   └── vmware_vm_snapshot_mgmt.yml
├── templates
├── tests
│   ├── inventory
│   └── test.yml
└── vars
    └── main.yml

8 directories, 9 files
```

Example Playbook
----------------
```yaml
#
# Role to change vCenter Server certificates
# Author: Julian Wendland
#
---

- name: snapshot a vm 
  hosts: localhost
  connection: local

  vars_files:
    - /home/jw/github/Ansible/roles/vcsa/roles/vcsa.general/vault/secrets.yml

  roles:
    - roles/vcsa.vm.snapshot
...
```



Author Information
------------------
Julian Wendland
Soeldner Consult GmbH
03.02.2021
