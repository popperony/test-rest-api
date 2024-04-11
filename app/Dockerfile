FROM python:3.10-alpine AS app-base

ENV PYTHONUNBUFFERED 1

WORKDIR /srv/app/

RUN apk add --no-cache build-base python3-dev openssl-dev libffi-dev cargo postgresql-dev postgresql-client

RUN pip install --no-cache-dir -U pip uwsgi tox

COPY requirements.txt /srv/app/

RUN pip install -r requirements.txt

ENTRYPOINT ["./scripts/docker-entrypoint.sh"]
