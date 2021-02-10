# Ansible Collection - sap.vcsa
Ansible Collection: sap.vcsa for managing vmware vCenter.

## Usage
### Requirements
Install required python packages.
```
pip install -r requirements.txt
```

### Install
Install collection
```
ansible-galaxy install git+https://github.tools.sap/cia/sap.vcsa,main
```

## Content
### Roles
| Name                                      | Description                                       |
|-------------------------------------------|---------------------------------------------------|
| [sap.vcsa.general](roles/vcsa.general/)          | A role to handle general vCenter Tasks for example login via REST API |
| [sap.vcsa.service](roles/vcsa.service/)          | A role to manage vCenter Server services    	 |
| [sap.vcsa.vm.snapshot](roles/vcsa.vm.snapshot/)      | A role to manage VM snapshots 		   	 |
| [sap.vcsa.certificate](roles/vcsa.certificate/)      | A role to change vCenter root ca certificate     |
| [sap.vcsa.backup](roles/vcsa.backup/)           | A role to setup vCenter backup schadule          |


Roles Structure
===============

```bash
.
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
│   │   │   └── testBody.yml
│   │   ├── handlers
│   │   │   └── main.yml
│   │   ├── meta
│   │   │   └── main.yml
│   │   ├── README.md
│   │   ├── tasks
│   │   │   ├── main.yml
│   │   │   └── vmware_vcsa_backup_mgmt.yml
│   │   ├── templates
│   │   │   └── backup_schedule_request_body.j2
│   │   ├── tests
│   │   │   ├── inventory
│   │   │   └── test.yml
│   │   └── vars
│   │       └── main.yml
│   ├── vcsa.certificate
│   │   ├── defaults
│   │   │   └── main.yml
│   │   ├── files
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
│   │   │   ├── old_vmware_vcsa_cert_mgmt.yml
│   │   │   ├── vmware_lookupservice_issue.yml
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
├── vcsa-backup-mgmt.yml
└── vcsa-certificate-mgmt.yml

49 directories, 61 files

```


# Example Playbook:
```yaml
# How to reuse vcsa roles
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


# [API Documentation](https://developer.vmware.com/docs/vsphere-automation/latest/)
-----------------------------------------------------------------------------------
This is the vSphere REST API Reference. It provides API documentation, request/response samples, and usage and description.


Author Information
------------------

Julian Wendland
Soeldner Consult GmbH
09.02.2021
