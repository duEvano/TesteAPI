import Monumenta.Cliente.model
from Monumenta.Cliente.controller.Cliente import Cliente as cliRegra


class Projeto:
    def __init__(self):
        self.__titulo = ""

    def __init__(self, titulo, id, apelidocliente):
        self.__titulo = titulo
        self.__id = id
        self.__porcentagem = ''
        self.__cliente = apelidocliente
        controller = cliRegra(apelido=apelidocliente)
        self.__clienteobj = controller.loadByApelido(nickName=apelidocliente)
        self.__pit = ''

    def get_Titulo(self):
        return self.__titulo

    def set_Titulo(self, i):
        self.__titulo = i

    def get_Cliente(self):
        return self.__clienteobj

    def set_Cliente(self, c):
        self.__clienteobj = c

    def get_PIT(self):
        return self.__pit

    def set_PIT(self, p):
        self.__pit = p

    def get_ID(self):
        return self.__id

    def set_ID(self, i):
        self.__id = i

    titulo = property(get_Titulo, set_Titulo)
