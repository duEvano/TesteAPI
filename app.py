from flask import Flask, request, abort

import bb.bcommercer
from bb import banco_do_brasil

app = Flask(__name__)
@app.route('/')
def index():
    id_space_projetos = 'IEADYSXZI4QOZRYM'
    # return banco_do_brasil.atualiza_data_trocastatus()
    # return  wrikeUtil.WrikeResponse('/folders/IEADYSXZI4QSY3QA', '')
    print('tah logado')
    return 'tamos aqui 2'


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
    #return bb.bcommercer.criar_tarefa_orcamento('IEADYSXZKQ2O2CU2').get_descricaoNova()
    if request.method == 'POST':
        print(request.json)
        if request.json[0]["oldStatus"] == 'A Fazer' and request.json[0]["status"] == 'In Progress':
            bb.bcommercer.criar_tarefa_orcamento(request.json[0]["taskId"])
        return 'success', 200
    else:
         abort(400)

if __name__ == '__main__':
    app.run()
