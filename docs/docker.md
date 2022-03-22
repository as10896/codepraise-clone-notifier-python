# Run with Docker
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

## Example usage

```shell
docker compose run --rm worker  # send daily clone reports based on development configurations
ENV=production docker compose run --rm worker  # send daily clone reports based on production configurations
docker compose run --rm console  # run console
```

After execution, the clone report will be sent to your Slack channel.
