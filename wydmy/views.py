from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("Hello World Django views")

def healthCheck(reuqest):
    return HttpResponse('ok')