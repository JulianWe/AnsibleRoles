VCSA Ansible Roles
==================

A Role to handle all Tasks regarding VMware vCenter Server 7.0


Role Structure
--------------

```bash
.
├── ansible.cfg
├── vcsa
│   ├── defaults
│   │   └── main.yml
│   ├── files
│   ├── handlers
│   │   ├── main.yml
│   │   └── vmware_vcsa_service_restart.yml
│   ├── hosts
│   │   └── hosts
│   ├── meta
│   │   └── main.yml
│   ├── README.md
│   ├── roles
│   │   ├── vcsa.backup
│   │   │   ├── defaults
│   │   │   │   └── main.yml
│   │   │   ├── files
│   │   │   ├── handlers
│   │   │   │   └── main.yml
│   │   │   ├── meta
│   │   │   │   └── main.yml
│   │   │   ├── README.md
│   │   │   ├── tasks
│   │   │   │   ├── main.yml
│   │   │   │   └── vmware_vcsa_backup_mgmt.yml
│   │   │   ├── templates
│   │   │   ├── tests
│   │   │   │   ├── inventory
│   │   │   │   └── test.yml
│   │   │   └── vars
│   │   │       └── main.yml
│   │   ├── vcsa.certificate
│   │   │   ├── defaults
│   │   │   │   └── main.yml
│   │   │   ├── files
│   │   │   │   ├── certBody.json
│   │   │   │   └── testBody.json
│   │   │   ├── handlers
│   │   │   │   └── main.yml
│   │   │   ├── meta
│   │   │   │   └── main.yml
│   │   │   ├── README.md
│   │   │   ├── tasks
│   │   │   │   ├── convert_digicert_from_crt_to_pem.yml
│   │   │   │   ├── get_certificate_from_digicert.yml
│   │   │   │   ├── get_certificate_from_github.yml
│   │   │   │   ├── main.yml
│   │   │   │   └── vmware_vcsa_cert_mgmt.yml
│   │   │   ├── templates
│   │   │   ├── tests
│   │   │   │   ├── inventory
│   │   │   │   └── test.yml
│   │   │   └── vars
│   │   │       └── main.yml
│   │   ├── vcsa.service
│   │   │   ├── defaults
│   │   │   │   └── main.yml
│   │   │   ├── files
│   │   │   ├── handlers
│   │   │   │   └── main.yml
│   │   │   ├── meta
│   │   │   │   └── main.yml
│   │   │   ├── README.md
│   │   │   ├── tasks
│   │   │   │   ├── main.yml
│   │   │   │   └── vmware_service_restart.yml
│   │   │   ├── templates
│   │   │   ├── tests
│   │   │   │   ├── inventory
│   │   │   │   └── test.yml
│   │   │   └── vars
│   │   │       └── main.yml
│   │   └── vcsa.vm.snapshot
│   │       ├── defaults
│   │       │   └── main.yml
│   │       ├── files
│   │       ├── handlers
│   │       │   └── main.yml
│   │       ├── meta
│   │       │   └── main.yml
│   │       ├── README.md
│   │       ├── tasks
│   │       │   ├── main.yml
│   │       │   └── vmware_vm_snapshot_mgmt.yml
│   │       ├── templates
│   │       ├── tests
│   │       │   ├── inventory
│   │       │   └── test.yml
│   │       └── vars
│   │           └── main.yml
│   ├── tasks
│   │   ├── main.yml
│   │   └── vmware_vcsa_rest_login.yml
│   ├── templates
│   │   └── vmware_vcsa_cert_mgmt_jsonBody.j2
│   ├── tests
│   │   ├── ansible.cfg
│   │   └── inventory
│   ├── vars
│   │   └── main.yml
│   └── vault
│       └── secrets.yml
└── vcsa-certificateMgmt.yml

48 directories, 56 files

```

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.


Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

```yaml
# vars file for vcsa Ansible role
site: "{{ inventory_hostname.split('.')[2] | lower }}"
domain: "{{ inventory_hostname | adsite('fqdn') }}"
digicert_url: https://cacerts.digicert.com/
root_ca_file: DigiCertGlobalRootCA.crt
interm_ca_file: DigiCertSHA2SecureServerCA.crt
snapshot: ansible_vcsa_certificate_change
datacenter: Noris
files:
  - "{{ inventory_hostname }}.pem"
  - "{{ inventory_hostname }}-key.pem"
...
```

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

PyVmomi Python module required. Install using \"pip install PyVmomi\"


Example Playbook
----------------

```yaml
---
- name: Change vCenter Certificates
  hosts: localhost
  connection: local

  vars_files:
    - /home/jw/github/Ansible/roles/vcsa/vault/secrets.yml

  roles:
    - vcsa
    - vcsa/roles/vcsa.vm.snapshot
    - vcsa/roles/vcsa.certificate
...
```

License
-------


Author Information
------------------
Julian Wendland
Soeldner Consult GmbH
19.01.2021

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
