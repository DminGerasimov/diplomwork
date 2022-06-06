#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for starting postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started sucsessfully"
fi

python3 manage.py flush --no-input
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser --noinput
 # python3 manage.py loaddata ./fixtures/user.json \
 #  ./fixtures/video_clip.json \
 #  ./fixtures/ban.json \
 #  ./fixtures/like.json \
 #  ./fixtures/subscription.json \
 #  ./fixtures/participant.json \
 #  ./fixtures/comment.json

exec "$@"
