from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Inclui as URLs do app ‘website’
    path('', include('website.urls', namespace='website')),
    # Interface administrativa
    path('admin/', admin.site.urls),
]
