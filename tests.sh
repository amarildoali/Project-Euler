#!/bin/sh

if [ "$#" -eq 0 ]
  then
    echo "First argument that should be a .py file or directory"
  else
    prospector --strictness high "$1"
    pylint "$1"
    flake8 "$1"
    mypy "$1"
    pyflakes "$1"
    coverage run --branch "$1"
    coverage html
fi

printf '\nFinished.\n'
