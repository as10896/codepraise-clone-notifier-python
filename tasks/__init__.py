from invoke import Collection

from . import console, docker, quality, worker

ns = Collection(console, worker, docker, quality)
