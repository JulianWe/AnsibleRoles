vcsa.backup
===========

VCSA Ansible role to setup Appliance backup schedule 

Role Variables
--------------
| Name | Description | Mandatory | Type
| -------------- | ------------------------------------------ | --------- | ------ |
| vcenter | vcenter FQDN or IP | true | string
| backup_password | Password for Backup encryption | true | string
| backup_location | *example:  sftp://ns1.sclabs.net/home/vcenter/auto_backup | true | string
| location_password | Password for backup location | true | string
| location_user | User for backup location root | true | string

The portocols supported for backup are FTPS, HTTPS, SFTP, FTP, NFS, SMB and HTTP.

`
Role Structure
--------------

```bash
.
├── defaults
│   └── main.yml
├── files
│   └── testBody.yml
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── README.md
├── tasks
│   ├── main.yml
│   └── vmware_vcsa_backup_mgmt.yml
├── templates
│   └── backup_schedule_request_body.j2
├── tests
│   ├── inventory
│   └── test.yml
└── vars
    └── main.yml

8 directories, 11 files
```


Example Playbook
----------------

```yaml
---

- name: Schedule vcsa backup
  hosts: localhost
  connection: local

  vars_files:
    - /home/jw/github/AnsibleRoles/vcsa/roles/vcsa.general/vault/secrets.yml

  roles:
    - roles/vcsa.general
    - roles/vcsa.backup

...
```


Author Information
------------------

Julian Wendland
Soeldner Consult GmbH
09.02.2021
