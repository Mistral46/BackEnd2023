
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.http import HttpRequest
from PBE import views
def otro(request):
    return HttpResponse('otro')
def otraView(request):
    return HttpResponse('<p>HOLAAA</p>')
def requestTest(request):
    return (HttpRequest.body)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testing/',views.testing),
    path('otracosa/',views.algunaOtraCosa),
    path('otro/',otro),
    path('otraview',otraView),
    path('requestTest',requestTest)
]
