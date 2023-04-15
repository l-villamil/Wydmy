from .logic import plantillas_logic as ul
from django.core import serializers
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render



@csrf_exempt
def plantillas_view(request):
    if request.method=='GET':
        id=request.GET.get("id",None)
        if id:
            plantilla_dto=ul.get_plantilla(id)
            plantilla=serializers.serialize('json',[plantilla_dto],)
            return HttpResponse(plantilla,'application/json')
        else:
            plantillas_dto=ul.get_plantillas( )
            plantillas=serializers.serialize('json',plantillas_dto)
            return HttpResponse(plantillas,'application/json')
    if request.method=='POST':
        plantilla_dto=ul.create_plantilla(json.loads(request.body))
        plantilla=serializers.serialize('json',[plantilla_dto,])
        return HttpResponse(plantilla,'application/json')

    return render(request, 'avanzo/base.html', context) # tiene que ser un render! por algo de segurIdad de Django -> csrf_token
    # se pueden mandar variables al html! -> context

@csrf_exempt
def plantilla_view(request,pk):
    if request.method=='GET':
        plantilla=ul.get_plantilla(pk)
        plantilla_dto=serializers.serialize('json',plantilla)
        return HttpResponse(plantilla_dto,'application/jason')
    if request.method =='PUT':
        plantilla_dto = ul.update_variable(pk, json.loads(request.body))
        plantilla = serializers.serialize('json', [plantilla_dto,])
        return HttpResponse(plantilla, 'application/json')
