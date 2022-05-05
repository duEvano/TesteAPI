class item_contrato:
    def __init__(self, descricao, numero, valor, apelido, qtd):
        self.__descricao = descricao
        self.__numero = numero
        self.__valor = valor
        self.__apelido = apelido
        self.__qtd = qtd

    def get_valorTotal(self):
        return self.__valor * self.__qtd

    def get_description(self):
        return self.__descricao

    def get_numero(self):
        return self.__numero

    def get_qtd(self):
        return self.__qtd

    def get_valorUnitario(self):
        return self.__valor

    def get_apelido(self):
        return str(self.__qtd) + " " + self.__apelido
