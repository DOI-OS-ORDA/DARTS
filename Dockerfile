# syntax=docker/dockerfile:1
FROM python:3.13
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y \
  build-essential \
  libpoppler-cpp-dev \
  pandoc \
  pkg-config \
  poppler-utils \
  python-dev-is-python3 \
  xpdf
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
