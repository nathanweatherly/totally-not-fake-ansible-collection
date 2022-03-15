#!/usr/bin/python
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''

module: hello_world

short_description: hello world

author:
- "Nathan Weatherly (@nathanweatherly)"

description:
- Says hello to greeting_target, returning a full greeting string.

options:
    greeting_target:
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
- name: "Say hello to program"
  nathanweatherly.totally_not_fake.hello_world:
    greeting_target: Program
  register: full_greeting

- name: "Say hello to World"
  nathanweatherly.totally_not_fake.hello_world
  register: full_greeting
'''

RETURN = r'''
full_greeting:
  description: Full greeting to greeting_target
  returned: success
  type: str
'''

import traceback

from ansible.module_utils.basic import AnsibleModule

def execute_module(module: AnsibleModule):
    greeting_target = module.params['greeting_target']
    full_greeting = "Hello {}!".format(greeting_target)
    module.exit_json(changed=True, full_greeting=full_greeting)

def main():
    argument_spec = dict(
        greeting_target=dict(type="str", default="world"),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    execute_module(module)


if __name__ == '__main__':
    main()