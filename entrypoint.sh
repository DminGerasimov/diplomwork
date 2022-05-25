#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for starting postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.5
    done

    echo "PostgreSQL started sucsessfully"
fi

python3 manage.py flush --no-input
python3 manage.py migrate

exec "$@"
