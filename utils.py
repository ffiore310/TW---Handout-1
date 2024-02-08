def extract_route(request):
    linhas = request.split()
    caminho = linhas[1]
    caminho = caminho[1:]
    return caminho

def read_file(path):
    byte = open(path, 'rb')
    return byte.read()
