from rest_framework.serializers import ModelSerializer
from core.models import Racha, Membros
from django.contrib.auth.models import User

class RachaSerializer(ModelSerializer):
    class Meta:
        model = Racha
        fields = ['id', 'nome','created_at']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class MembrosSerialiazer(ModelSerializer):
    class Meta:
        model = Membros
        fields = ['id','racha','usuario','is_member','inviter','date_create_at']


    def create(self, validated_data):
        membro = Membros(
            racha = validated_data['racha'],
            usuario = validated_data['usuario'],
            is_member = validated_data['is_member'],
            inviter= validated_data['inviter'],

        )

        membro.save()

        return membro
