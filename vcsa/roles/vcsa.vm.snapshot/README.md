vcsa.vm.snapshot
================

This Role is used to handle vCenter Snapshots

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

| Name           | Description                                | Mandatory | Type   |
| -------------- | ------------------------------------------ | --------- | ------ |
| datacenter | Datacenter Name | true | string
| vmNameToSnap | Name der VM von der ein Snapshot gemacht werden soll | true | string
| vc1Fqdn | FQDN from Managment vCenter | true | string
| snapshot | Name des Snapshots | true | string

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: vcsa.vm.snapshot }

License
-------


Author Information
------------------
Julian Wendland
Soeldner Consult GmbH
03.02.2021
