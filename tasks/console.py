from invoke import task


@task(
    default=True,
    help={
        "env": "Environment of the console to run. ['development'|'production'] [default: 'development']"
    },
)
def console(c, env="development"):
    """
    Run application console (ipython)
    """
    c.run(
        f"ENV={env} ipython \
            --InteractiveShellApp.exec_lines='from config import *' \
            --InteractiveShellApp.exec_lines='from worker.representers import *' \
            --InteractiveShellApp.exec_lines='from worker.infrastructure.messaging import *'",
        pty=True,
    )
