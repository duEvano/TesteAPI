import locale


def formatMoney(valor):
    if str(valor) != '':
        retorno = real_br_money_mask(valor)
    else :
        retorno = '--'

    retorno = 'R$ ' + retorno
    return retorno


def real_br_money_mask(my_value):
    a = '{:,.2f}'.format(float(my_value))
    b = a.replace(',', 'v')
    c = b.replace('.', ',')
    return c.replace('v', '.')


def get_nome_mes(idMes):
    months = ["Desconhecido",
              "Janeiro",
              "Fevereiro",
              "Março",
              "Abril",
              "Maio",
              "Junho",
              "Julho",
              "Agosto",
              "Setembro",
              "Outubro",
              "Novembro",
              "Dezembro"]
    month = (months[idMes])
    return month

def getStringKeyValue(texto,sep) :
    posicaoInicial = texto.find(sep) + len(sep)
    posicaoFinal = len(texto)
    return texto[posicaoInicial:posicaoFinal]