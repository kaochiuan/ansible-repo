## Ansible lookup plugins

### lambda (lookup):
___
Returns value(s) by invoking a lambda function.

##### Example Playbook
```yaml
# Simple example of using a value returned by a lambda function invocation
- hosts: localhost
  gather_facts: no
  vars:
    state: absent
    lambda_output: "{{ lookup('lambda', 'myFunction') }}"
  tasks:
  - name: Test lookup plugin
    debug: var=lambda_output

```

## Installation

Do the following to install the lambda modules in your Ansible environment:

1. Clone this repository or download the ZIP file.

2. Copy the *.py files from the plugins directory to your installation custom plugin directory. Custom plugins will go in a directory relating to the plugin type, e.g. a lookup plugin will got into `./lookup_plugins` relative to where your playbooks are located. Refer to the [docs](http://docs.ansible.com/ansible/developing_plugins.html#distributing-plugins) for more information.

3. Make sure boto3 is installed.
