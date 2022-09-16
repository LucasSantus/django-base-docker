# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST 1

# update pip
RUN pip install --upgrade pip

# install dependencies
RUN apk add --update --no-cache postgresql-client jpeg-dev

RUN apk add --update --no-cache --virtual .tmp-build-deps \ 
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

# copy requirements files
COPY ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install -r /usr/src/app/requirements.txt

RUN apk del .tmp-build-deps

# add user celery
RUN adduser --disabled-password --no-create-home --gecos '' celery
USER celery

# copy project
COPY . /usr/src/app/