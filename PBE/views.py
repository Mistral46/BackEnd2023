from django.http import HttpResponse

def testing(resquest):
    return HttpResponse('testeando app')

def algunaOtraCosa(request):
    return HttpResponse('hola')