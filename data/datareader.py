from utils import formating as stringTeste


def readSeed(key):
    lines = []
    nomeArquivo = 'C:\Evano\Python\TesteAPI\data\seeds.txt'
    with open(nomeArquivo) as f:
        lines = f.readlines()

    retorno = 0
    for line in lines:
        if line.find(key) > -1:
            retorno = int(stringTeste.getStringKeyValue(line, '='))
    if retorno > 0:
        with open(nomeArquivo, "w") as f:
            for line in lines:
                if line.find(key) < 0:
                    f.write(line)
                else :
                    f.write(key + '=' + str(retorno+1))
    return retorno
