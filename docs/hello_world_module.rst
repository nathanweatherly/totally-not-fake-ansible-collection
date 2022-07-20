.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.nathanweatherly.totally_not_fake.hello_world_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

nathanweatherly.totally_not_fake.hello_world -- hello world
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `nathanweatherly.totally_not_fake collection <https://galaxy.ansible.com/nathanweatherly/totally_not_fake>`_ (version 0.0.3).

    To install it use: :code:`ansible-galaxy collection install nathanweatherly.totally_not_fake`.

    To use it in a playbook, specify: :code:`nathanweatherly.totally_not_fake.hello_world`.

.. version_added


.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Says hello to greeting_target, returning a full greeting string.


.. Aliases


.. Requirements


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-greeting_target"></div>
                    <b>greeting_target</b>
                    <a class="ansibleOptionLink" href="#parameter-greeting_target" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"world"</div>
                                    </td>
                                                                <td>
                                            <div>This field is the name to greet.</div>
                                            <div>It is a string.</div>
                                            <div>The default target is world</div>
                                            <div>Fourth line of description.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: "Say hello to program"
      nathanweatherly.totally_not_fake.hello_world:
        greeting_target: Program
      register: full_greeting

    - name: "Say hello to World"
      nathanweatherly.totally_not_fake.hello_world:
      register: full_greeting




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-full_greeting"></div>
                    <b>full_greeting</b>
                    <a class="ansibleOptionLink" href="#return-full_greeting" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Full greeting to greeting_target</div>
                                        <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>

..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Nathan Weatherly (@nathanweatherly)



.. Parsing errors

