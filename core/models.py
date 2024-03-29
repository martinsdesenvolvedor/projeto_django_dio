from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(verbose_name='Descrição', blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    local_evento = models.CharField(verbose_name='Local do Evento', max_length=100, default='local')
    data_criacao = models.DateTimeField(verbose_name='Data de Criação', auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y as %H:%MHs')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

