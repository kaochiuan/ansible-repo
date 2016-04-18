# Ansible Cloud Modules

These modules have been moved from other projects.


## Requirements
- python >= 2.6
- ansible >= 2.0
- boto3 >= 1.2.3

## Modules

### lambda_event:

Use to create, update or delete lambda function source event mappings, which include Kinesis/DynamoDB streams, S3 events and SNS topics.

##### Example Playbook
```yaml
- hosts: localhost
  gather_facts: no
  vars:
    state: present
  tasks:
  - name: S3 event mapping
    lambda_event:
      state: "{{ state | default('present') }}"
      event_source: s3
      function_name: ingestData
      alias: Dev
      source_params:
        id: lambda-s3-myBucket-create-data-log
        bucket: buzz-scanner
        prefix: twitter
        suffix: log
        events:
        - s3:ObjectCreated:Put

  - name: show source event config
    debug: var=lambda_s3_events

  - name: DynamoDB stream event mapping
    lambda_event:
      state: "{{ state | default('present') }}"
      event_source: stream
      function_name: "{{ function_name }}"
      alias: Dev
      source_params:
        source_arn: arn:aws:dynamodb:us-east-1:123456789012:table/tableName/stream/2016-03-19T19:51:37.457
        enabled: True
        batch_size: 120
        starting_position: TRIM_HORIZON

  - name: show source event config
    debug: var=lambda_stream_events

  - name: SNS event mapping
    lambda_event:
      state: "{{ state | default('present') }}"
      event_source: sns
      function_name: SaveMessage
      alias: Prod
      source_params:
        id: lambda-sns-topic-notify
        topic_arn: arn:aws:sns:us-east-1:123456789012:sns-some-topic

  - name: show SNS event mapping
    debug: var=lambda_sns_event

```

### iam:

Modified *iam* core module which allows specification of a custom trust policy. View pull request [here](https://github.com/ansible/ansible-modules-core/pull/3264)


### s3_event:

Work in progress -- creating separate module for S3 events from Lambda_event module.


## Installation

Do the following to install the lambda modules in your Ansible environment:

1. Clone this repository or download the ZIP file.

2. Copy the *.py files from the modules directory to your installation custom module directory.  This is, by default, in `./library` which is relative to where your playbooks are located. Refer to the [docs](http://docs.ansible.com/ansible/developing_modules.html#developing-modules) for more information.

3. Make sure boto3 is installed.








