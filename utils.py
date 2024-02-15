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
        print(type(data))
    return data

def load_template(filename):
    file_path = os.path.join("templates", filename)
    with open(file_path, 'r') as file:
        template = file.read()
    #print(template)
    return template

def adicionar_anotacao(nova_anotacao):
    file_path = os.path.join("data", "notes.json")
    with open(file_path, 'r') as arquivo:
        dados = json.load(arquivo)
    dados.append(nova_anotacao)
    with open(file_path, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False) #esses dois argumentos são para o arquivo ficar mais legível

def build_response(body = '', code=200, reason='OK', headers=''):
    if len(headers) > 0:
        response = f'HTTP/1.1 {code} {reason}\n{headers}\n\n{body}'
    else:
        response = f'HTTP/1.1 {code} {reason}\n\n{body}'
    return response.encode()