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
| vm_name_to_snap | vCenter VM name for snapshot role | true | string
| snapshot_name | snapshot name | true | string
| vcenter_fqdn | vCenter to change certificate | true | string
| cert | Certificate | true | string
| key | private_key | false | string
| root_cert | root_cert | false | string

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

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
│   ├── convert_digicert_from_crt_to_pem.yml
│   ├── get_certificate_from_digicert.yml
│   ├── get_certificate_from_github.yml
│   ├── main.yml
│   ├── old_vmware_vcsa_cert_mgmt.yml
│   ├── vmware_lookupservice_issue.yml
│   └── vmware_vcsa_cert_mgmt.yml
├── templates
│   └── vmware_vcsa_cert_mgmt_jsonBody.j2
├── tests
│   ├── inventory
│   └── test.yml
└── vars
    └── main.yml

8 directories, 15 files
```


Dependencies
------------
 - { role: vcsa.general, vcenter_fqdn: fqdn, vc_username: username, vc_pssword: password }
 - { role: vcsa.vm.snapshot, vm_name_to_snap: vcsa, snapshot_name: name, datacenter: Datacenter }


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
    - roles/vcsa.certificate
...
```

[API Documentation](https://developer.vmware.com/docs/vsphere-automation/latest/vcenter/rest/vcenter/certificate-management/vcenter/tls/put/)
--------------------------------------------------------------------------------------------------------------------------------------------
Replaces the rhttpproxy TLS certificate with the specified certificate. This operation can be used in three scenarios : 1. When the CSR is created and the private key is already stored, this operation can replace the certificate. The certificate but not the private key and root certificate must be provided as input. 2. When the certificate is signed by a third party certificate authority/VMCA and the root certificate of the third party certificate authority/VMCA is already one of the trusted roots in the trust store, this operation can replace the certificate and private key. The certificate and the private key but not the root certificate must be provided as input. 3. When the certificate is signed by a third party certificate authority and the root certificate of the third party certificate authority is not one of the trusted roots in the trust store, this operation can replace the certificate, private key and root CA certificate. The certificate, private key and root certificate must be provided as input. After this operation completes, the services using the certificate will be restarted for the new certificate to take effect. The above three scenarios are only supported from vsphere 7.0 onwards. if you do not have all of the privileges described as follows: - Operation execution requires CertificateManagement.Administer.

Author Information
------------------

Julian Wendland 
Soeldner Consult GmbH 
04.02.2021
