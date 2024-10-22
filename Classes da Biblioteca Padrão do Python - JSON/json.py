# PARA ESCREVER DADOS EM UM ARQUIVO JSON USANDO O PYTHON.

import json # Importação da biblioteca JSON.

# Dicionário (dados), para criar lista ordenada de valores; para guardar as informações que serão utilizadas no código em Python.
dados = { 
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

arquivo = open("dados.json", "w") # "dados.json" foi o arquivo criado para conter as informações que estão no dicionário "dados". Enquanto o "w" (modo write, ou gravação) foi utilizado para abrir o arquivo em modo de escrita.
json.dump(dados, arquivo) # dump() transfere as informações do dicionário dados para o arquivo dados.json.
arquivo.close() # Fecha o arquivo.


# LER O ARQUIVO JSON NO PYTHON.

import json

arquivo = open("dados.json", "r") # "r" significa modo de leitura.
dados = json.load(arquivo) # json.load() carrega os dados na variável. 
arquivo.close() 

print(dados)

