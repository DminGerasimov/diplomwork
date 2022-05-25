# pull official base image
FROM ubuntu:20.04

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt update \
	&& apt install python3 python3-pip python3-dev postgresql-server-dev-all gcc libpq-dev netcat -y
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#copy entrypoint.sh
#COPY ./entrypoint.sh .
#RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
#RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
