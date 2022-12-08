#!/bin/bash

echo "DB Connection --- Establishing . . ."

while ! nc -z db 5432; do

    echo "DB Connection -- Failed!"

    sleep 1

    echo "DB Connection -- Retrying . . ."

done

echo "DB Connection --- Successfully Established!"

exec "$@"
