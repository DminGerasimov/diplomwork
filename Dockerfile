# pull official base image
FROM python:3.8.13-alpine3.15

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk add libffi-dev
# RUN pip install --upgrade pip wheel
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .