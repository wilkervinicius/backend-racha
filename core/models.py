from django.db import models
from django.contrib.auth.models import User


class Racha(models.Model):
    nome = models.CharField(verbose_name='Nome',unique=True,max_length=150)
    descricao = models.TextField(verbose_name='Descrição', blank=True, null=True)
 #   aprovado = models.BooleanField(default=False)
    created_at = models.DateTimeField(verbose_name='Criado em',auto_now_add=True)
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    membros_ingressados = models.ManyToManyField(User,
                                     through='Membros',
                                     through_fields=('racha','usuario'))
    def __str__(self):
        return self.nome


class Membros(models.Model):
    racha = models.ForeignKey(Racha,on_delete=models.CASCADE)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    is_member = models.BooleanField(default=False)
    date_create_at = models.DateTimeField(auto_now_add=True)
    inviter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="membros_convidados",
        null=True, blank=True,
    )
    class Meta:
        unique_together = ['usuario','racha']
        verbose_name='Membros'
        verbose_name_plural = 'Membros'

        
    def __str__(self):
        return  self.usuario.username

