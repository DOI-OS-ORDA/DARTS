# syntax=docker/dockerfile:1
FROM python:3.13
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
  build-essential \
  firefox-esr \
  libpoppler-cpp-dev \
  pandoc \
  pkg-config \
  poppler-utils \
  python-dev-is-python3 \
  xpdf

COPY ./binaries/geckodriver-v0.35.0-linux64.tar.gz geckodriver.tar.gz
RUN tar -zxf geckodriver.tar.gz -C /usr/local/bin && chmod +x /usr/local/bin/geckodriver

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
