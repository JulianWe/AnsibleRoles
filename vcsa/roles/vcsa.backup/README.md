vcsa.backup
===========

VCSA Ansible role to setup Appliance backup schedule 

Role Variables
--------------
| Name | Description | Mandatory | Type
| vcenter | vcenter FQDN or IP | true | string
| backup_password | Password for Backup encryption | true | string
| backup_location | *example:  sftp://ns1.sclabs.net/home/vcenter/auto_backup | true | string
| location_password | Password for backup location | true | string
| location_user | User for backup location root | true | string

The portocols supported for backup are FTPS, HTTPS, SFTP, FTP, NFS, SMB and HTTP.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

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

License
-------

BSD

Author Information
------------------

Julian Wendland
Soeldner Consult GmbH
09.02.2021
