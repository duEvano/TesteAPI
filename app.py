from flask import Flask, request, abort, send_file

import Monumenta.Financeiro.valores_itens
from Monumenta.Financeiro.View.oc import oc as ocView
import bb.bcommercer
from bb import banco_do_brasil
import os
app = Flask(__name__)


@app.route('/')
def index():

    return os.getcwd() + '\\' + 'teste'


# Função que atualiza a data da mudança de status
@app.route('/updatedatastatus', methods=['POST'])
def update_data_troca():
    if request.method == 'POST':
        print(request.json)
        banco_do_brasil.atualiza_data_trocastatus(request.json[0]["taskId"])
        return 'success', 200
    else:
        abort(400)


# Função geraDoac do BCOMMERCER - Escuta da pasta : IEADYSXZI4W4J75G
# webHook responsavel : IEADYSXZJAABC5AF
@app.route('/bcommercerDOAC', methods=['POST'])
def update_criardoacBcommercer():
    # return bb.bcommercer.criar_tarefa_orcamento('IEADYSXZKQ2O2CU2').get_descricaoNova()
    if request.method == 'POST':
        print(request.json)
        if request.json[0]["oldStatus"] == 'A Fazer' and request.json[0]["status"] == 'In Progress':
            bb.bcommercer.criar_tarefa_orcamento(request.json[0]["taskId"])
        return 'success', 200
    else:
        abort(400)


# Função dos valores financeiros baseado na troca de valores de custom
# webHook responsavel : IEADYSXZJAABDB5O (apagado)
@app.route('/financeiroValores', methods=['POST'])
def update_financeiroValores():
    # return bb.bcommercer.criar_tarefa_orcamento('IEADYSXZKQ2O2CU2').get_descricaoNova()
    if request.method == 'POST':
        # print(request.json)
        # if request.json[0]["oldStatus"] == 'A Fazer' and request.json[0]["status"] == 'In Progress':
        Monumenta.Financeiro.valores_itens.calculosValoreItens(request.json[0]["taskId"],porcentagemHonor=5)
        # bb.banco_do_brasil(request.json[0]["taskId"])
        return 'success', 200
    else:
        abort(400)


# WeebBokk das tarefas financeiras para o BB Digital
# webHook responsavel : IEADYSXZJAABDL6G
@app.route('/financeiroBBDigital', methods=['POST'])
def update_financeiroValoresBBDigital():
    # return bb.bcommercer.criar_tarefa_orcamento('IEADYSXZKQ2O2CU2').get_descricaoNova()
    if request.method == 'POST':
        # print(request.json)
        Monumenta.Financeiro.valores_itens.calculosValoreItens(request.json[0]["taskId"], porcentagemHonor=6)
        return 'success', 200
    else:
        abort(400)


# WeebBokk das tarefas financeiras para o BB Promo
# webHook responsavel : IEADYSXZJAABDM2L
@app.route('/financeiroBBPromo', methods=['POST'])
def update_financeiroValoresBBPromo():
    if request.method == 'POST':
        print(request.json)
        Monumenta.Financeiro.valores_itens.calculosValoreItens(request.json[0]["taskId"], porcentagemHonor=5)
        return 'success', 200
    else:
        abort(400)


# WeebBokk das tarefas financeiras para o BB Seguros
# webHook responsavel : IEADYSXZJAABDM2L
@app.route('/financeiroBBSeguros', methods=['POST'])
def update_financeiroValoresBBSeguros():
    if request.method == 'POST':
        print(request.json)
        Monumenta.Financeiro.valores_itens.calculosValoreItens(request.json[0]["taskId"], porcentagemHonor=5)
        return 'success', 200
    else:
        abort(400)

@app.route('/downloadOc', methods=['GET'])
def downloadOC():
    args = request.args
    id = args.get("id")
    ocV = ocView(id=id)
    n = ocV.gerarPDF()
    path = 'static/ocs/'+n
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run()
#data': [{'id': 'IEADYSXZJAABDL6G', 'accountId': 'IEADYSXZ', 'folderId': 'IEADYSXZI4QSY3QA'

# o webhook q vamos usar serã o do ProjectStatusChanged (para calculo do numero do PIT)