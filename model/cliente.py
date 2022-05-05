class cliente:
    def __init__(self, nome, apelido, cnpj, email, endereco, enderecoCobranca, Inscricao_estadual, prefixo, RazaoSocial ,Seed, Telefone):
        self.nome = nome
        self.Telefone = Telefone
        self.Seed = Seed
        self.RazaoSocial = RazaoSocial
        self.prefixo = prefixo
        self.Inscricao_estadual = Inscricao_estadual
        self.email = email
        self.endereco = endereco
        self.enderecoCobranca = enderecoCobranca
        self.cnpj = cnpj
        self.__descricao =None
        self.__apelido = apelido
