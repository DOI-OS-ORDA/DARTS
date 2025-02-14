FROM python:3.10

COPY ./.docker/zscaler_cert.pem /tmp/zscaler.crt
RUN cp /tmp/zscaler.crt /usr/local/share/ca-certificates/zscaler.crt ; update-ca-certificates

RUN apt-get update && apt-get install -y postgresql-client

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pip install pipenv
RUN pipenv install --system --dev
