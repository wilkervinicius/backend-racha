from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from core.models import Racha, Membros
from .serializers import RachaSerializer, MembrosSerialiazer
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.response import Response


class RachaViewSet(ModelViewSet):

    queryset = Racha.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = RachaSerializer





class UserViewSet(ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer




    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)




class MembrosViewset(ModelViewSet):

    queryset = Membros.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = MembrosSerialiazer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('racha', 'usuario')


    @action(methods=['post'], detail=True)
    def aprovaIngresso(self,request,pk=None):
        pass