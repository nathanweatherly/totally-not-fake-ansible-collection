==============================================
Nathanweatherly.Totally_Not_Fake Release Notes
==============================================

.. contents:: Topics


v0.0.1
======

Release Summary
---------------

Initial migration of Grafana content from Ansible core (2.9/devel)


Minor Changes
-------------

- Python 2.6 Target Support - Deprecate Python 2.6 for targets, requiring Python 2.7 or newer. ``ansible-core==2.13`` will drop support for Python 2.6. (https://github.com/ansible/ansible/pull/74165)
- ssh - added pkcs11 support by adding the pkcs11_provider option in the ssh connection module. (https://www.github.com/ansible/ansible/pull/32829)

Bugfixes
--------

- register - Ensure that ``register`` used on ``set_fact`` or ``include_vars`` does not automatically wrap the facts as unsafe. (https://github.com/ansible/ansible/issues/21088)
- subversion - fix stack trace when getting information about the repository (https://github.com/ansible/ansible/issues/36498)
