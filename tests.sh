#!/bin/sh

if [ $1 -eq 0 ]
  then
    echo "First argument that should be a .py file or directory"
  else
    prospector --strictness high "$1"
    pylint "$1"
    flake8 "$1"
    mypy "$1"
    pyflakes "$1"
    coverage run "$1"
    coverage report -m
fi

# Print solved in README.md
README="README.md"
echo '# Solved' > $README
grep -Ril 'src/' -e 'Solution' | sort | tee -a $README > /dev/null

printf '\nFinished.\n'
