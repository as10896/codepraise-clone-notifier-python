from invoke import Collection

from . import console, worker, quality

ns = Collection(console, worker, quality)
