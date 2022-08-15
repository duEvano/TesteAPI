import Monumenta.Financeiro.constante_financeiras


class task_financeira:
    def __init__(self, qtd, valor, tipoCusto, percertualHonor, percentualEncargo,cnpjFornecedor):
        self.cnpjFornecedor = cnpjFornecedor
        self.nomeFornecedor = None
        self.percentualEncargo = percentualEncargo
        self.valorhonorario = 0
        self.tipo_custo = tipoCusto
        self.percentualHonor = percertualHonor
        self.valor = valor
        self.qtd = qtd
        self.valorTotal = self.qtd = qtd * self.valor
        self.valototalReal = 0
        self.receita = 0
        self.valorTerceiro = 0
        self.valorEncargo = 0

        # calculo do honorario
        if self.tipo_custo == '🙃Custo Terceiro c/ honorário':
            self.valorhonorario = self.valorTotal * (self.percentualHonor / 100)
            self.receita = self.valorhonorario
            self.valototalReal = self.valorTotal + self.valorhonorario
            self.valorTerceiro = self.valorTotal
        else:
            if self.tipo_custo == '🤑Custo Interno - Agência':
                self.valorhonorario = 0
                self.receita = self.valorTotal
                self.valototalReal = self.valorTotal
                self.valorTerceiro = 0
            else:
                if self.tipo_custo == '😪Custo Terceiro s/ honorário':
                    self.valorhonorario = 0
                    self.receita = 0
                    self.valototalReal = self.valorTotal
                    self.valorTerceiro = self.valorTotal
                else:
                    if self.tipo_custo == '😊Custo Interno - Fornecedor':
                        self.valorhonorario = self.valorTotal * (self.percentualHonor / 100)
                        self.valorEncargo = self.valorTotal * (self.percentualEncargo/100)
                        self.valototalReal = self.valorTotal + self.valorhonorario + self.valorEncargo
                        self.valorTerceiro = self.valorTotal
                        self.receita = self.valototalReal
                    else:
                        #utilizado apenas para PP
                        if self.tipo_custo == '💸Pagamento':
                            self.valototalReal = self.valorTotal * -1

    def get_valorHonorario(self):
        return self.valorhonorario

    def get_valorTotal(self):
        return self.valorTotal

    def get_valorReceita(self):
        return self.receita

    def get_valorTotalReal(self):
        return self.valototalReal

    def get_valorTerceiro(self):
        return self.valorTerceiro

    def get_valorEncargo(self):
        return self.valorEncargo

    def get_NomeFornecedor(self):
        return self.nomeFornecedor
