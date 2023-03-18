from .logic import usuarios_logic as ul
from django.core import serializers
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt

def usuarios_view(request):
    if request.method=='GET':
        id=request.GET.get("id",None)
        if id:
            usuario_dto=ul.get_usuario(id)
            usuario=serializers.serialize('json',[usuario_dto],)
            return HttpResponse(usuario,'application/json')
        else:
            usuarios_dto=ul.get_usuarios( )
            usuarios=serializers.serialize('json',usuarios_dto)
            return HttpResponse(usuarios,'application/json')
    if request.method=='POST':
        usuario_dto=ul.create_usuario(json.loads(request.body))
        usuario=serializers.serialize('json',[usuario_dto,])
        return HttpResponse(usuario,'application/json')


@csrf_exempt
def usuario_view(request,pk):
    if request.method=='GET':
        usuario=ul.get_usuario(pk)
        usuario_dto=serializers.serialize('json',usuario)
        return HttpResponse(usuario_dto,'application/jason')
    if request.method =='PUT':
        usuario_dto = ul.update_variable(pk, json.loads(request.body))
        usuario = serializers.serialize('json', [usuario_dto,])
        return HttpResponse(usuario, 'application/json')
