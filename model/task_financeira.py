class task_financeira:
    def __init__(self, qtd, valor, custo_interno, percertualHonor):
        self.valorhonorario = None
        self.custo_interno = custo_interno
        self.percentualHonor = percertualHonor
        self.valor = valor
        self.qtd = qtd
        self.valorTotal = self.qtd = qtd * self.valor

        # calculo do honorario
        if not (self.custo_interno == 'true'):
            self.valorhonorario = self.valorTotal * (self.percentualHonor/100)
            self.receita = self.valorhonorario
            self.valototalReal = self.valorTotal + self.valorhonorario
        else:
            self.valorhonorario = 0
            self.receita = self.valorTotal
            self.valototalReal = self.valorTotal

    def get_valorHonorario(self):
        return self.valorhonorario

    def get_valorTotal(self):
        return self.valorTotal

    def get_valorReceita(self):
        return self.receita

    def get_valorTotalReal(self):
        return self.valototalReal
