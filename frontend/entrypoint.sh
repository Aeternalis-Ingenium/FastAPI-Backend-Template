#!/bin/bash

echo "Frontend <-> Backend Connection --- Establishing . . ."

while ! nc -z backend_app 8000; do

    echo "Frontend <-> Backend Connection -- Failed!"

    sleep 1

    echo "Frontend <-> Backend Connection -- Retry . . ."

done

echo "Frontend <-> Backend Connection --- Successfully Established!"

exec "$@"
