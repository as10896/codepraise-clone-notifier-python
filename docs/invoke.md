# Invoke tasks
Here we use <a href="https://docs.pyinvoke.org/" target="_blank">Invoke</a> as our task management tool.

You can use the container's bash to test these commands.
```shell
docker compose run --rm bash
```

## Commands
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
