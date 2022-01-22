from invoke import task

IMAGE = "codepraise-clone-notifier-python"


@task
def build(c):
    """
    Build Docker image for production usage
    """
    print("\nBUILDING WORKER IMAGE FOR PRODUCTION)")
    c.run(f"docker build -t {IMAGE} .", pty=True)


@task(
    help={
        "cmd": "The command substituted for the image's default setting.",
        "envs": "Environment variables set for the container.",
    },
    iterable=["envs"],
)
def run(c, envs, cmd=None):
    """
    Run the local Docker container as a worker
    """
    print("\nRUNNING WORKER WITH LOCAL CONTEXT")
    print(f" Running in production mode")

    if envs:
        envs.append("ENV=production")
        envarg = " ".join(map(lambda s: f"-e {s}", envs))
    else:
        envarg = "-e ENV=production"

    if cmd:
        c.run(
            f"docker run {envarg} -v $(pwd)/config:/worker/config --rm -it {IMAGE} {cmd}",
            pty=True,
        )
    else:
        c.run(
            f"docker run {envarg} -v $(pwd)/config:/worker/config --rm {IMAGE}",
            pty=True,
        )


@task
def rm(c):
    """
    Remove exited containers
    """
    c.run("docker rm -v $(docker ps -a -q -f status=exited)", pty=True)


@task
def ps(c):
    """
    List all containers, running and exited
    """
    c.run("docker ps -a", pty=True)
