import Monumenta.Projetos.model.Projeto
import Monumenta.Projetos.controller.Projeto
import Monumenta.Cliente.controller.Cliente

__projetoNew = Monumenta.Projetos.controller.Projeto.Projeto(id='IEADYSXZI42PPQZX')
pro = __projetoNew.loadProjeto()
cli = pro.get_Cliente()
print(pro.get_PIT())