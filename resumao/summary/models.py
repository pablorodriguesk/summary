from django.db import models

# Create your models here.


class User(models.Model):
    SEXO_CHOICE = (
        ("feminino","Feminino"),
        ("masculino","Masculino"), )

    nome = models.CharField(max_length=20, null=False)
    data_nascimento = models.DateField(null=False, verbose_name="Data de Nascimento")
    sexo = models.CharField(max_length=15, null=False, choices=SEXO_CHOICE )
    formacao = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    likendin = models.CharField(max_length=20)
    instagram = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)

    def __str__(self):
       return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Summary(models.Model):
    ESTADO_CHOICE=(

        ("Otimo","Otimo"),
        ("bom","Bom"),
        ("ruim","Ruim"),
    )
    titulo = models.CharField(max_length=20)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria)
    data_de_cr = models.DateTimeField(auto_now_add=True)
    keyword = models.CharField(max_length=20)
    avaliacao = models.CharField(max_length=20, choices=ESTADO_CHOICE, null=False)
    likes = models.CharField(max_length=20)
    comentario = models.CharField(max_length=20)


    def __str__(self):
        return self.titulo
    
    
    class discart(models.Model):
        Discart = models.charfild(max_langth=300)
        
        def __str__(self):
            return sel.discart
        
