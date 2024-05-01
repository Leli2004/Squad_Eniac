from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

STATUS = (
    ('p', 'Pendente'),
    ('a', 'Aprovado'),
    ('r', 'Recusado'),
)

class Voluntario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefone = PhoneNumberField()
    profissão = models.CharField(max_length=500)
    info_geral = models.CharField('Informação', max_length=500)
    ativo = models.BooleanField(default=True)
    status = models.CharField(max_length=1,choices=STATUS, default="p")


    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Inscrição de voluntario'
        verbose_name_plural = 'Inscrição de voluntarios'