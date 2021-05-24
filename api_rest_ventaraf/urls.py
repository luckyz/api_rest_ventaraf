from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from anuncios import views

router = routers.DefaultRouter()
router.register(r'anuncios', views.AnuncioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
