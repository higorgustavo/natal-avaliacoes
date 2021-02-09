from django.db import models


class Loja(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    AVALIACAO_CHOICES = [
        ["Ruim", "Ruim"],
        ["Normal", "Normal"],
        ["Bom", "Bom"]
    ]
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    avaliacao_cliente = models.CharField(max_length=25,
                                         verbose_name="Avaliação",
                                         choices=AVALIACAO_CHOICES)
    data_avaliacao = models.DateField(auto_now=True)

    def __str__(self):
        return self.loja.nome + " - " + self.avaliacao_cliente + " - " + str(self.data_avaliacao)

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"