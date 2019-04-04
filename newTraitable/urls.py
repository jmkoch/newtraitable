
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Traitable import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.)
]
