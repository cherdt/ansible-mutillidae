ansible-mutillidae
=========

An Ansible role to install [Mutillidae II](https://github.com/webpwnized/mutillidae), a deliberately vulnerable web application, on an Ubuntu 18.04 host. This may work on other Debian-based derivatives, but has not been tested.

Why? I wanted to set up a copy of Mutillidae II on an ESXi 6.5 host (moving it to an isolated network after installation). I tried using the [Metasploitable 2](https://sourceforge.net/projects/metasploitable/files/Metasploitable2/) virtual machine, but it is intended for VMWare Player or Virtual Box, not ESXi. I also tried the [OWASP BWA 1.2](https://sourceforge.net/projects/owaspbwa/files/1.2/) .ova file, but it is apparently not compatible with ESXi 6.5.

An Ansible playbook to install Mutillidae II seemed like a good, repeatable solution. Suggestions and pull requests welcomed.

Requirements
------------

None yet.

Role Variables
--------------

None yet.

Dependencies
------------

None yet.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: target_hosts
      roles:
         - ansible-mutillidae

License
-------

MIT

Author Information
------------------

Blame Chris Herdt. [Accidental Developer](https://osric.com/chris/accidental-developer/).
