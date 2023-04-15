from ..models import Plantilla

def get_plantillas():
    plantillas=Plantilla.objects.all()
    return plantillas

def get_plantilla(var_pk):
    plantilla=Plantilla.objects.get(pk=var_pk)
    return plantilla

def update_plantilla(sol_pk, new_sol):
    plantilla=get_plantilla(sol_pk)
    plantilla.nombre=new_sol["nombre"]
    plantilla.medico=new_sol["medico"]
    plantilla.procedimiento=new_sol["procedimiento"]
    plantilla.hospital=new_sol["hospital"]
    plantilla.save()
    return plantilla



def create_plantilla(sol):
    plantilla=Plantilla(
        nombre=sol["nombre"],
        medico=sol["medico"],
        procedimiento=sol["procedimiento"],
        hospital=sol["hospital"]
    )
    plantilla.save()
    return plantilla
