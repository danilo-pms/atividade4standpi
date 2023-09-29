from django.db import models

class Stand(models.Model):
    localizacao = models.CharField(max_length=100)
    valor = models.FloatField()

    def __str__(self):
        return f"Stand {self.id}"

class Reserva(models.Model):
    cnpj = models.CharField(max_length=14)
    nome = models.CharField(max_length=100)
    categoria_empresa = models.CharField(max_length=50)
    quitado = models.BooleanField(default=False)
    stand = models.OneToOneField(Stand, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Reserva {self.id} - {self.nome}"
