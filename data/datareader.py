from utils import formating as stringTeste
import os


def readSeed(key):
    nomeArquivo = 'seeds.txt'

    directory = './data/'

    file_path = os.path.join(directory, nomeArquivo)
    lines = []
    #nomeArquivo = 'C:\Evano\Python\TesteAPI\data\seeds.txt'
    with open(file_path) as f:
        lines = f.readlines()

    retorno = 0
    for line in lines:
        if line.find(key) > -1:
            retorno = int(stringTeste.getStringKeyValue(line, '='))
    if retorno > 0:
        with open(file_path, "w") as f:
            for line in lines:
                if line.find(key) < 0:
                    f.write(line)
                else :
                    f.write(key + '=' + str(retorno+1))
    return retorno
