
from django.contrib import admin
from django.urls import path
from information_app.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('office/', office),
    path('office/<name>',info)

]
