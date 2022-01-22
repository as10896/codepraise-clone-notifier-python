# syntax=docker/dockerfile:1

FROM python:3.9-slim

WORKDIR /worker

COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --system --deploy --ignore-pipfile

COPY . .

CMD inv worker -e production
