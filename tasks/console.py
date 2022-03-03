from invoke import task


@task(
    default=True,
    help={
        "mode": "Environment of the console to run. ['development'|'production'] [default: 'development']"
    },
)
def console(c, mode="test"):
    """
    Run application console (ipython)
    """
    c.run(
        f"ENV={mode} ipython \
            --InteractiveShellApp.exec_lines='from config import *' \
            --InteractiveShellApp.exec_lines='from worker.application.representers import *' \
            --InteractiveShellApp.exec_lines='from worker.infrastructure.messaging import *'",
        pty=True,
    )
