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
        echo pytest
        ;;
    *)
        echo "Argumento inválido. Use 'lint' ou 'fome'"
        exit 1
        ;;
esac