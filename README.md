# codepraise-clone-notifier-python
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

Scheduled worker for  [codepraise-api-python](https://github.com/as10896/codepraise-api-python).

## Prerequisite
### Create virtual environment
Here we use [Pipenv](https://pipenv.pypa.io/en/latest/) to create our virtual environment.

```bash
pip install pipenv  # install pipenv
pipenv --python 3.9  # create Python 3.9 virtualenv under current directory
pipenv shell  # activate the virtualenv of the current directory
pipenv install --dev  # install required dependencies with Pipfile
```

### Set up Report Queue with Amazon SQS 
1. Create an AWS account and an IAM user ([Ref](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-setting-up.html)).
2. Create `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` under `config/secrets/<env>/` with the generated credentials (or just setting environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`).
3. Select a region where FIFO Queues are available (e.g. `us-east-1`, see [here](https://aws.amazon.com/about-aws/whats-new/2019/02/amazon-sqs-fifo-qeues-now-available-in-15-aws-regions/) for more info), then creating `AWS_REGION` under `config/secrets/<env>/` with the region name (or just setting the environment variable `AWS_REGION`).
3. Creating a **FIFO** Amazon SQS queue ([Ref](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-create-queue.html)).
    * Notice that the name of a FIFO queue must end with the `.fifo` suffix.
4. Create `REPORT_QUEUE` under `config/secrets/<env>/` with the created queue's name (or just setting the environment variable `REPORT_QUEUE`).

### Set up Slack Webhook URL
1. Follow this [tutorial](https://api.slack.com/messaging/webhooks) to create a Slack App and get your Webhook URL.
2. Create `SLACK_WEBHOOK_URL` under `config/secrets/<env>/` with the webhook url (or just setting the environment variable `SLACK_WEBHOOK_URL`).

## Run with Docker
Use either of the following ways to build image and run container with all the credentials.
* Put all credentials under `config/secrets/prod/` directory. Then use the following command to build image and run container at the base of the project directory.
    ```bash
    docker compose run --rm worker
    ```
* Pass all credentials directly with the following command.
    ```bash
    docker compose run --rm \
        -e AWS_ACCESS_KEY_ID=<aws credentials> \
        -e AWS_SECRET_ACCESS_KEY=<aws credentials> \
        -e AWS_REGION=<aws credentials> \
        -e REPORT_QUEUE=<aws sqs queue> \
        -e SLACK_WEBHOOK_URL=<slack webhook url> \
        worker
    ```
    or
    ```bash
    export AWS_ACCESS_KEY_ID=<aws credentials>
    export AWS_SECRET_ACCESS_KEY=<aws credentials>
    export AWS_REGION=<aws credentials>
    export REPORT_QUEUE=<aws sqs queue>
    export SLACK_WEBHOOK_URL=<slack webhook url>
    docker compose run --rm worker
    ```

## CLI usage
Here we use [invoke](https://docs.pyinvoke.org/) as our task management tool

```bash
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
inv docker.build  # build Docker image for production usage
inv docker.run -e [environs] -c [cmd]  # run the local Docker container as a worker
inv docker.rm  # remove exited containers
inv docker.ps  # list all containers, running and exited
```
