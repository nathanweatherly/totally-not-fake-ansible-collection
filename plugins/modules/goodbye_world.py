#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''

module: goodbye_world

short_description: goodbye world

author:
- "Nathan Weatherly (@nathanweatherly)"

description:
- Says goodbye to goodbye_target, returning a full greeting string.

options:
    goodbye_target:
        description:
        - This field is the name to greet.
        - It is a string.
        - The default target is world
        - Fourth line of description.
        type: str
        default: world
        required: False
'''

EXAMPLES = r'''
- name: "Say goodbye to program"
  nathanweatherly.totally_not_fake.goodbye_world:
    goodbye_target: Program
  register: full_goodbye

- name: "Say goodbye to World"
  nathanweatherly.totally_not_fake.goodbye_world:
  register: full_goodbye
'''

RETURN = r'''
full_goodbye:
  description: Full parting to goodbye_target
  returned: success
  type: str
'''

import traceback

from ansible.module_utils.basic import AnsibleModule


def execute_module(module: AnsibleModule):
    goodbye_target = module.params['goodbye_target']
    full_goodbye = "Goodbye {0}!".format(goodbye_target)
    module.exit_json(changed=True, full_goodbye=full_goodbye)


def main():
    argument_spec = dict(
        goodbye_target=dict(type="str", default="world"),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    execute_module(module)


if __name__ == '__main__':
    main()
