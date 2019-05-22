#!/bin/sh
set -e

function web {
    python manage.py runserver -h 0.0.0.0
}

function upgrade_db {
    python manage.py db upgrade
}

function sh {
    /bin/sh
}

case "$1" in 
    "web")
        upgrade_db
        web
        ;;
    "upgrade_db")
        upgrade_db
        ;;
    "sh")
        sh
        ;;
    *)
        echo "
        Usage: $0 [ARG]
          [ARG]:
            - 'web' to run the webapp
            - 'upgrade_db' to run all migration on database
            - 'sh' to start a sh shell
        "
        exit 1

esac