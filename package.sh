#!/bin/bash

# Verifica se foi passado um argumento
if [ $# -eq 0 ]; then
    echo "Por favor, forneça um argumento"
    exit 1
fi

# Verifica qual argumento foi passado
case $1 in
    "test_print")
        pytest -v -s
        ;;
    "test") 
        pytest
        ;;
    "run") 
        export FLASK_APP=run
        export FLASK_RUN_PORT=8001
        flask run
        ;;
    *)
        echo "Argumento inválido"
        exit 1
        ;;
esac