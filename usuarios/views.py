from .logic import usuarios_logic as ul
from django.core import serializers
from django.http import HttpResponse
import json
def usuarios_view(request):
    if request.method=='GET':
        usuarios=ul.get_usuarios()
        usuarios_dto=serializers.serialize('json',usuarios)
        return HttpResponse(usuarios_dto,'application/json')


def usuario_view(request,pk):
    if request.method=='GET':
        usuario=ul.get_usuario(pk)
        usuario_dto=serializers.serialize('json',usuario)
        return HttpResponse(usuario_dto,'application/jason')
    if request.method =='PUT':
        usuario_dto = ul.update_variable(pk, json.loads(request.body))
        usuario = serializers.serialize('json', [usuario_dto,])
        return HttpResponse(usuario, 'application/json')