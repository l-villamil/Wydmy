from ..models import Usuario

def get_usuarios():
    usuarios=Usuario.objects.all()
    return usuarios

def get_usuario(var_pk):
    usuario=Usuario.objects.get(pk=var_pk)
    return usuario

def update_usuario(sol_pk, new_sol):
    usuario = get_usuario(sol_pk)
    usuario.cedula = new_sol["cedula"]
    usuario.nombre = new_sol["nombre"]
    usuario.telefono = new_sol["telefono"]
    usuario.correo = new_sol["correo"]
    usuario.direccion = new_sol["direccion"]
    usuario.save()
    return usuario

