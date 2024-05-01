from django.db import models

# Create your models here.

class Raca(models.Model):
    raca = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Raça'
        verbose_name_plural = 'Raças'

    def __str__(self):
        return self.raca

class Especie(models.Model):
    especie = models.CharField(max_length=50)

    def __str__(self):
        return self.especie

class Porte(models.Model):
    porte = models.CharField(max_length=50)

    def __str__(self):
        return self.porte
    
class Sexo(models.Model):
    sexo = models.CharField(max_length=50)

    def __str__(self):
        return self.sexo

class Animal(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField('idade')
    chip = models.CharField(max_length=15)
    info_animais = models.CharField('Sobre',max_length=500)
    image = models.ImageField(upload_to='images/')
    raca = models.ForeignKey(Raca, on_delete = models.CASCADE)
    especie = models.ForeignKey(Especie, on_delete = models.CASCADE)
    porte = models.ForeignKey(Porte, on_delete = models.CASCADE)
    sexo = models.ForeignKey(Sexo, on_delete = models.CASCADE)
    disponivel = models.BooleanField(default=True)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
        ordering = ['-data']

    def __str__(self):
        return self.nome
   
class Historico_medico(models.Model):
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)
    info_medica = models.CharField('Informacoes', max_length=50)
    voluntario_name = models.CharField('Voluntario', max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    image = models.ImageField('Foto Receita', upload_to='receita/', null=True, blank=True)
    file  = models.FileField('Pdf Receita', upload_to='receita/', null=True,blank=True)

    