import json
import os

def extract_route(request):
    linhas = request.split()
    caminho = linhas[1]
    caminho = caminho[1:]
    return caminho

def read_file(path):
    byte = open(path, 'rb')
    return byte.read()

def load_data(filename):
    file_path = os.path.join("data", filename)
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def load_template(filename):
    file_path = os.path.join("templates", filename)
    with open(file_path, 'r') as file:
        template = file.read()
    return template

def adicionar_anotacao(nova_anotacao):
    file_path = os.path.join("data", "notes.json")
    with open(file_path, 'r') as arquivo:
        dados = json.load(arquivo)
    dados.append(nova_anotacao)
    with open(file_path, 'w') as arquivo:
        json.dump(dados, arquivo)