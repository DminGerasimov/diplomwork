# pull official base image
FROM ubuntu:20.04

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
# RUN pip install --upgrade pip wheel
RUN apt install python
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .