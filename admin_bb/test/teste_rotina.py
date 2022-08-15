import admin_bb.controller.admin
import admin_bb.model.Demanda

__admin = admin_bb.controller.admin.admin(idTarefa='IEADYSXZKQ2EQOCQ')
item = __admin.loadTarefa()
print( item.get_Titulo())