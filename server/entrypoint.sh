#!/bin/bash
# Wait for postgres to get up and running

set -e
cmd="$@"

function check_installations(){
python << END
import sys
try:
    import django
    import psycopg2
except ImportError:
    sys.exit(-1)
sys.exit(0)
END
}

function postgres_ready(){
python << END
import sys
import psycopg2
try:
    conn = psycopg2.connect("host='db' dbname='postgres' user='postgres' password='postgres'")
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

if check_installations
    then
        until postgres_ready; do
          >&2 echo "Postgres is unavailable - sleeping"
          sleep 1
        done

        >&2 echo "Postgres is up - executing command"
        exec $cmd
else
    >&2 echo "Django or psycopg2 not installed, install requirements"
fi
