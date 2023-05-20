
from django.contrib import admin
from django.urls import path, include
from posts.api.urls import urlpatterns




urlpatterns = [
    path('admin/',admin.site.urls),
    path('api/',include(urlpatterns))
]
