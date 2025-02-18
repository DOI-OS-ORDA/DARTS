FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./.docker/zscaler_cert.pem /tmp/zscaler.crt
RUN cp /tmp/zscaler.crt /usr/local/share/ca-certificates/zscaler.crt ; update-ca-certificates

RUN apt-get update && apt-get install -y \
  build-essential \
  firefox-esr \
  libpoppler-cpp-dev \
  pandoc \
  pkg-config \
  poppler-utils \
  python-dev-is-python3 \
  xpdf

COPY ./support/geckodriver-v0.35.0-linux64.tar.gz geckodriver.tar.gz
RUN tar -zxf geckodriver.tar.gz -C /usr/local/bin && chmod +x /usr/local/bin/geckodriver

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pip install pipenv
RUN pipenv install --system --dev
