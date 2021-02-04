# VCSA Ansible Roles

Role Structure
===============

```bash
.
├── README.md
└── vcsa
    ├── hosts
    │   └── hosts
    ├── meta
    │   └── main.yml
    ├── README.md
    ├── requirements.txt
    ├── roles
    │   ├── vcsa.backup
    │   │   ├── defaults
    │   │   │   └── main.yml
    │   │   ├── files
    │   │   ├── handlers
    │   │   │   └── main.yml
    │   │   ├── meta
    │   │   │   └── main.yml
    │   │   ├── README.md
    │   │   ├── tasks
    │   │   │   ├── main.yml
    │   │   │   └── vmware_vcsa_backup_mgmt.yml
    │   │   ├── templates
    │   │   ├── tests
    │   │   │   ├── inventory
    │   │   │   └── test.yml
    │   │   └── vars
    │   │       └── main.yml
    │   ├── vcsa.certificate
    │   │   ├── defaults
    │   │   │   └── main.yml
    │   │   ├── files
    │   │   │   ├── certBody.json
    │   │   │   └── testBody.json
    │   │   ├── handlers
    │   │   │   └── main.yml
    │   │   ├── meta
    │   │   │   └── main.yml
    │   │   ├── README.md
    │   │   ├── tasks
    │   │   │   ├── convert_digicert_from_crt_to_pem.yml
    │   │   │   ├── get_certificate_from_digicert.yml
    │   │   │   ├── get_certificate_from_github.yml
    │   │   │   ├── main.yml
    │   │   │   └── vmware_vcsa_cert_mgmt.yml
    │   │   ├── templates
    │   │   │   └── vmware_vcsa_cert_mgmt_jsonBody.j2
    │   │   ├── tests
    │   │   │   ├── inventory
    │   │   │   └── test.yml
    │   │   └── vars
    │   │       └── main.yml
    │   ├── vcsa.general
    │   │   ├── defaults
    │   │   │   └── main.yml
    │   │   ├── files
    │   │   ├── handlers
    │   │   │   └── main.yml
    │   │   ├── meta
    │   │   │   └── main.yml
    │   │   ├── README.md
    │   │   ├── tasks
    │   │   │   ├── main.yml
    │   │   │   └── vmware_vcsa_rest_login.yml
    │   │   ├── templates
    │   │   ├── tests
    │   │   │   ├── inventory
    │   │   │   └── test.yml
    │   │   ├── vars
    │   │   │   └── main.yml
    │   │   └── vault
    │   │       └── secrets.yml
    │   ├── vcsa.service
    │   │   ├── defaults
    │   │   │   └── main.yml
    │   │   ├── files
    │   │   ├── handlers
    │   │   │   ├── main.yml
    │   │   │   └── vmware_vcsa_service_restart.yml
    │   │   ├── meta
    │   │   │   └── main.yml
    │   │   ├── README.md
    │   │   ├── tasks
    │   │   │   ├── main.yml
    │   │   │   └── vmware_service_restart.yml
    │   │   ├── templates
    │   │   ├── tests
    │   │   │   ├── inventory
    │   │   │   └── test.yml
    │   │   └── vars
    │   │       └── main.yml
    │   └── vcsa.vm.snapshot
    │       ├── defaults
    │       │   └── main.yml
    │       ├── files
    │       ├── handlers
    │       │   └── main.yml
    │       ├── meta
    │       │   └── main.yml
    │       ├── README.md
    │       ├── tasks
    │       │   ├── main.yml
    │       │   └── vmware_vm_snapshot_mgmt.yml
    │       ├── templates
    │       ├── tests
    │       │   ├── inventory
    │       │   └── test.yml
    │       └── vars
    │           └── main.yml
    └── vcsa-certificateMgmt.yml
```


# Example Playbook:
```yaml
#
# How to reuse vcsa roles
# Author: Julian Wendland
#
---

- name: reuse vcsa roles 
  hosts: localhost
  connection: local

  vars_files:
    - /home/jw/github/Ansible/roles/vcsa/roles/vcsa.general/vault/secrets.yml

  roles:
    - roles/vcsa.general # Login 
    - roles/vcsa.vm.snapshot
    - roles/vcsa.certificate
...
```
