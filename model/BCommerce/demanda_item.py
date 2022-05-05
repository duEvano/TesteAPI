from model import item_contrato

class demanda_item:
    def __init__(self,itens):
        self.__tipo = None
        self.__itens = itens
        self.valortotal = None


    def get_tipo(self):
        return self.__tipo

    def set_tipo(self,tipo):
        self.__tipo = tipo