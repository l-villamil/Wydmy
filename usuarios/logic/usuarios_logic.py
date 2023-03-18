from ..models import Usuario

def get_usuarios():
    usuarios=Usuario.objects.all()
    return usuarios