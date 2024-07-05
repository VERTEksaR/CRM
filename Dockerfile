FROM python:3.12

#RUN apk --update add bash
#SHELL ["/bin/bash", "-c"]

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

#RUN apk add --no-cache postgresql-libs  && \
#    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev git libffi-dev openssl-dev python3-dev jpeg-dev zlib-dev


RUN pip install -r requirements.txt

COPY crm .
