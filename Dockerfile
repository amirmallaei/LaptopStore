FROM python:3.13-bookworm

ENV PYTHONUNBUFFERED 1
ENV DJANGO_CONFIGURATION Docker
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && apt-get install -y gcc ghostscript

RUN pip install --upgrade pip

RUN mkdir /config

WORKDIR /config

ADD config/requirements.txt /config

RUN pip install -r requirements.txt

ADD ./config /config