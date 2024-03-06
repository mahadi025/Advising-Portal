FROM python:3.9-alpine3.13

LABEL maintainer="https://mahadi025.github.io"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./app /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt
