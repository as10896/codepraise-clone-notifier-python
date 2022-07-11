# CodePraise Python Clone Notifier
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

---

**Documentation**: <a href="https://as10896.github.io/codepraise-clone-notifier-python" target="_blank">https://as10896.github.io/codepraise-clone-notifier-python</a>

**Source Code**: <a href="https://github.com/as10896/codepraise-clone-notifier-python" target="_blank">https://github.com/as10896/codepraise-clone-notifier-python</a>

---

Daily clone report notifier for <a href="https://as10896.github.io/codepraise-app-python/" target="_blank">codepraise-app-python</a> and <a href="https://as10896.github.io/codepraise-api-python/" target="_blank">codepraise-api-python</a>, based on <a href="https://devcenter.heroku.com/articles/scheduler" target="_blank">Heroku Scheduler</a>.

## Prerequisite
### Install Docker
Make sure you have the latest version of <a href="https://www.docker.com/get-started" target="_blank">Docker 🐳</a> installed on your local machine.

### Secrets setup
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

#### Set up Report Queue with Amazon SQS
1. Create an AWS account and an IAM user (<a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-setting-up.html" target="_blank">Ref</a>).
2. Create `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` under `config/secrets/<env>/` with the generated credentials (or just setting environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`).
3. Select a region where FIFO Queues are available (e.g. `us-east-1`, see <a href="https://aws.amazon.com/about-aws/whats-new/2019/02/amazon-sqs-fifo-qeues-now-available-in-15-aws-regions/" target="_blank">here</a> for more info), then creating `AWS_REGION` under `config/secrets/<env>/` with the region name (or just setting the environment variable `AWS_REGION`).
3. Create a **FIFO** Amazon SQS queue (<a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-create-queue.html" target="_blank">Ref</a>).
    * Notice that the name of a FIFO queue must end with the `.fifo` suffix.
4. Create `REPORT_QUEUE` under `config/secrets/<env>/` with the created queue's name (or just setting the environment variable `REPORT_QUEUE`).

#### Set up Slack Webhook URL
1. Follow this <a href="https://api.slack.com/messaging/webhooks" target="_blank">tutorial</a> to create a Slack App and get your Webhook URL.
2. Create `SLACK_WEBHOOK_URL` under `config/secrets/<env>/` with the webhook url (or just setting the environment variable `SLACK_WEBHOOK_URL`).

## Run with Docker
You can use the notifier easily with Docker Compose.<br>
Before that, make sure you have all the configurations set up as mentioned before.

For convenience, you can use a `.env` file with all the necessary variables configured as follows:

```shell
export AWS_ACCESS_KEY_ID=<aws credentials>
export AWS_SECRET_ACCESS_KEY=<aws credentials>
export AWS_REGION=<aws credentials>
export CLONE_QUEUE=<aws sqs queue>
export SLACK_WEBHOOK_URL=<slack webhook url>
```

Then `source` the configuration file:

```shell
source .env
```

Notice that it is not recommended to `export` all these credentials directly in the shell since these will be logged into shell history if not inserted through secure input.<br>
Don't do that especially when you're using a shared device that might be accessed by multiple users.

### Example usage

```shell
docker compose run --rm worker  # send daily clone reports based on development configurations
ENV=production docker compose run --rm worker  # send daily clone reports based on production configurations
docker compose run --rm console  # run console
```

After execution, the clone report will be sent to your Slack channel.


## Invoke tasks
Here we use <a href="https://docs.pyinvoke.org/" target="_blank">Invoke</a> as our task management tool.

You can use the container's bash to test these commands.
```shell
docker compose run --rm bash
```

### Commands
```shell
inv -l  # show all tasks
inv [task] -h  # show task help message
inv console -e [env]  # run application console (ipython)
inv worker -e [env]  # execute the scheduled worker
inv quality.style  # examine coding style with flake8
inv quality.metric  # measure code metric with radon
inv quality.all  # run all quality tasks (style + metric)
inv quality.reformat  # reformat your code using isort and the black coding style
inv quality.typecheck  # check type with mypy
inv quality  # same as `inv quality.all`
```
