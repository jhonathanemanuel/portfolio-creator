from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    """"Üm portifolio do usuário"""

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="portfolios")

    titulo_projeto = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo_projeto

class ContentSection(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="sections")

    titulo_secao = models.CharField(max_length=100, help_text="Ex: Experiência sobre mim")
    conteudo = models.TextField(help_text="Aqui entra o seu texto (futuro markdown)")

    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return f"{self.titulo_secao} - {self.portfolio.titulo_projeto}"