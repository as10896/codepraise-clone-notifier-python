# syntax=docker/dockerfile:1

FROM python:3.9-slim AS base

WORKDIR /worker

# To install poetry
RUN apt-get update && \
    apt-get install -y curl

# To print directly to stdout instead of buffering output
ENV PYTHONUNBUFFERED=true

# Upgrade pip and install Poetry
RUN python -m pip install --upgrade pip && \
    curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY pyproject.toml poetry.lock* ./

RUN poetry install --no-root

COPY . .

CMD ["inv", "worker", "-e", "production"]

# ==================== debug ====================

FROM base AS debug

RUN poetry install --no-root --with dev

CMD ["inv", "worker", "-e", "development"]
