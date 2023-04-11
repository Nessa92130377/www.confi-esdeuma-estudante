from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Funcionario(models.Model):
    nome = models.CharField(
    max_length=255,
    null=False,
    blank=False
    )
    sobrenome = models.CharField(
    max_length=255,
    null=False,
    blank=False
    )
    cpf = models.CharField(
    max_length=14,
    null=False,
    blank=False
    )
    tempo_de_servico = models.IntegerField(
    default=0,
    null=False,
    blank=False
    )
    remuneracao = models.DecimalField(
    max_digits=8,
    decimal_places=2,
    null=False,
    blank=False
    )
    objetos = models.Manager()


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)



