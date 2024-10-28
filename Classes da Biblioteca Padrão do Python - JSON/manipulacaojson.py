# PARA ESCREVER DADOS EM UM ARQUIVO JSON USANDO O PYTHON.

import json # Importação da biblioteca JSON.

# Dicionário (dados), para criar lista ordenada de valores; para guardar as informações que serão utilizadas no código em Python.
carros_json = { 
    "marca": "Honda",
    "modelo": "HRV",
    "cor": "prata"
}

carros = json.loads(carros_json)
print(carros)

