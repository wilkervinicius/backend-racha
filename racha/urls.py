
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from core.api.viewsets import RachaViewSet, UserViewSet, MembrosViewset
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'racha',RachaViewSet)
router.register(r'users',UserViewSet)
router.register(r'membros',MembrosViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
]
