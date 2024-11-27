#!/bin/bash

# Verifica se foi passado um argumento
if [ $# -eq 0 ]; then
    echo "Por favor, forneça um argumento"
    exit 1
fi

# Verifica qual argumento foi passado
case $1 in
    "install") 
        FLASK_APP=run
        FLASK_RUN_PORT=8001
        BASH=package.sh
        BASH_TEST="package.sh test"
        BASH_INIT="package.sh init"
        BASH_RUN="package.sh run"
        ;;
    "test") 
        pytest -v -s
        ;;
    "init")
        echo 'Ativando ambient venv!'
        echo source venv/bin/activate
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