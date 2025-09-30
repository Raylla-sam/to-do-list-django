from django.db import models

class Task(models.Model):
    status_escolhas = [
                    ('N_FEITO', 'Não feito'),
                       ('FAZENDO', 'Fazendo'),
                       ('FEITO',' Feito'),
                       ]


    title = models.CharField(max_length=200)
    descricao = models.TextField()
    prazo = models.DateTimeField()
    status = models.CharField( 
        max_length = 15, 
        choices = status_escolhas, 
        default ='N_FEITO')
    
    
    def __str__(self):
        return f"{self.title} - {self.status}"

    

# Create your models here.
