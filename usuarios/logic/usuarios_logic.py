from ..models import Usuario

def get_usuarios():
    queryset = Usuario.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_usuario(form):
    cliente = form.save()
    cliente.save()
    return ()
