from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    status_escolhas = [
        ('N_FEITO', 'Não feito'),
        ('FAZENDO', 'Fazendo'),
        ('FEITO', 'Feito'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # 🔑 aqui
    title = models.CharField(max_length=200)
    descricao = models.TextField()
    prazo = models.DateTimeField()
    status = models.CharField(
        max_length=15,
        choices=status_escolhas,
        default='N_FEITO'
    )

    def __str__(self):
        return f"{self.title} - {self.status}"


    

# Create your models here.
