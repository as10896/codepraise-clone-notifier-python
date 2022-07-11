# Prerequisite
## Install Docker
Make sure you have the latest version of <a href="https://www.docker.com/get-started" target="_blank">Docker 🐳</a> installed on your local machine.

## Secrets setup
Placing secret values in files is a common pattern to provide sensitive configuration to an application. A secret file follows the same principal as a `.env` file except it only contains a single value and the file name is used as the key.

A secret file will look like the following:

`/var/run/database_password`:

```
super_secret_database_password
```

Here we create secret files under the secret directories (`config/secrets/<env>/`) and place secret values into the files.

You can also set up environment variables directly.<br>
The variables you set in this way would take precedence over those loaded from a secret file.

For more info, check the <a href="https://pydantic-docs.helpmanual.io/usage/settings/#secret-support" target="_blank">pydantic official document</a>.

### Set up Report Queue with Amazon SQS
1. Create an AWS account and an IAM user (<a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-setting-up.html" target="_blank">Ref</a>).
2. Create `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` under `config/secrets/<env>/` with the generated credentials (or just setting environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`).
3. Select a region where FIFO Queues are available (e.g. `us-east-1`, see <a href="https://aws.amazon.com/about-aws/whats-new/2019/02/amazon-sqs-fifo-qeues-now-available-in-15-aws-regions/" target="_blank">here</a> for more info), then creating `AWS_REGION` under `config/secrets/<env>/` with the region name (or just setting the environment variable `AWS_REGION`).
3. Create a **FIFO** Amazon SQS queue (<a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-create-queue.html" target="_blank">Ref</a>).
    * Notice that the name of a FIFO queue must end with the `.fifo` suffix.
4. Create `REPORT_QUEUE` under `config/secrets/<env>/` with the created queue's name (or just setting the environment variable `REPORT_QUEUE`).

### Set up Slack Webhook URL
1. Follow this <a href="https://api.slack.com/messaging/webhooks" target="_blank">tutorial</a> to create a Slack App and get your Webhook URL.
2. Create `SLACK_WEBHOOK_URL` under `config/secrets/<env>/` with the webhook url (or just setting the environment variable `SLACK_WEBHOOK_URL`).
