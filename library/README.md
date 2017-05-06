# Ansible Cloud Modules

These modules have been moved from other projects.


## Requirements
- python >= 2.6
- ansible >= 2.0
- boto3 >= 1.2.3

## Modules

### s3_event:

Use to create, update or delete S3 event notifications for SNS, SQS or Lambda.

##### Example Playbook
```yaml
# Example that creates lambda event notifications for an S3 bucket
- hosts: localhost
  gather_facts: no
  vars:
    state: present
    bucket: myBucket
  tasks:
  - name: S3 event notification
    s3_event:
      state: "{{ state | default('present') }}"
      bucket: "{{ bucket }}"
      id: lambda-s3-myBucket-data-log
      lambda_function_arn: ingestData
      prefix: twitter
      suffix: log
      events:
      - s3:ObjectCreated:Put

  - name: S3 event notification for SNS
    s3_event:
      state: "{{ state | default('present') }}"
      bucket: "{{ bucket }}"
      id: lambda-s3-myBucket-delete-sns-log
      topic_arn: arn:aws:sns:xx-east-1:123456789012:NotifyMe
      prefix: twitter
      suffix: log
      events:
      - s3:ObjectRemoved:Delete

  - name: S3 event notification for SQS
    s3_event:
      state: "{{ state | default('present') }}"
      bucket: "{{ bucket }}"
      id: lambda-s3-myBucket-copy-sqs-log
      queue_arn: myQueue
      prefix: twitter
      suffix: log
      events:
      - s3:ObjectCreated:Copy

  - name: show source event config
    debug: var=s3_event

```

### lambda_event: _(Deprecated)_

Use to create, update or delete lambda function source event mappings, which include Kinesis/DynamoDB streams, S3 events and SNS topics.

##### Example Playbook
```yaml
- hosts: localhost
  gather_facts: no
  vars:
    state: present
  tasks:
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

```

### iam:

Modified *iam* core module which allows specification of a custom trust policy. Now included in ansible-modules-core.

##### Example Playbook
```yaml
- hosts: localhost
  gather_facts: no
  vars:
    state: present
  tasks:
  # Example of role with custom trust policy for Lambda service
  - name: Create IAM role with custom trust relationship
    iam:
      iam_type: role
      name: AAALambdaTestRole
      state: present
      trust_policy:
        Version: '2012-10-17'
        Statement:
        - Action: sts:AssumeRole
          Effect: Allow
          Principal:
            Service: lambda.amazonaws.com

```

## Installation

Do the following to install the lambda modules in your Ansible environment:

1. Clone this repository or download the ZIP file.

2. Copy the *.py files from the modules directory to your installation custom module directory.  This is, by default, in `./library` which is relative to where your playbooks are located. Refer to the [docs](http://docs.ansible.com/ansible/developing_modules.html#developing-modules) for more information.

3. Make sure boto3 is installed.








