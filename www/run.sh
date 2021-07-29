#!/usr/bin/env bash

if [[ "$MIGRATE_AND_COLLECT_STATIC_FILES" = "true" ]]
then
    echo "Migrating and collecting static files"
    python manage.py migrate --settings=www.settings.production --noinput -v 2
    python manage.py collectstatic --settings=www.settings.production --noinput -v 2
    # collectstatic remotely
    # python manage.py collectstatic --settings=www.settings.production --noinput -v 2 -i admin -i cms -i django* -i filer -i sortedm2m -i treebeard
else
    echo "Bypassing migration and static files collection"
fi

gunicorn www.wsgi:application --bind 0.0.0.0:8000 --env DJANGO_SETTINGS_MODULE=www.settings.production
