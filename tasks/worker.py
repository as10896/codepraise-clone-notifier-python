from invoke import task


@task(
    default=True,
    help={
        "env": "Environment of the scheduled worker to execute. ['development'|'production'] [default: 'development']"
    },
)
def worker(c, env="development"):
    """
    Execute the scheduled worker
    """
    c.run(f"ENV={env} python -m application.clone_notifier")
