vcsa.certificate
=========

This role is used to change the vCenter certificate 

Requirements
------------


Role Variables
--------------

| Name           | Description                                | Mandatory | Type   |
| -------------- | ------------------------------------------ | --------- | ------ |
| site |  Site.. | true | string
| domain | Domain with ADsite | true | string
| digicert_url | https://cacerts.digicert.com/ | true  | string
| root_ca_file | root ca .crt file | true | file
| datacenter | Name of the Datacenter for snapshotrole | true | string
| vmNameToSnap | vCenter VM name for snapshot role | true | string
| snapshot | snapshot name | true | string
| vcenter | vCenter to change certificate | true | string


A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.


Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

```yaml
# Role to change vCenter Server certificate
---
- name: Change vCenter Certificates
  hosts: localhost
  connection: local

  vars_files:
    - /home/jw/github/Ansible/roles/vcsa/roles/vcsa.general/vault/secrets.yml

  roles:
    - roles/vcsa.general
    - roles/vcsa.vm.snapshot
    - roles/vcsa.certificate
...
```


Author Information
------------------

Julian Wendland 
Soeldner Consult GmbH 
04.02.2021
