from django.db import models


class Loja(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Alternativa(models.Model):
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    nome_alternativa = models.CharField(max_length=50, verbose_name="Alternativa")
    emoji = models.CharField(max_length=100, verbose_name="Código Emoji", null=True, blank=True)
    # https://www.w3schools.com/charsets/ref_emoji.asp

    def __str__(self):
        return self.nome_alternativa + " | " + self.loja.nome

    class Meta:
        verbose_name = "Alternativa"
        verbose_name_plural = "Alternativas"
        ordering = ['nome_alternativa']


class Voto(models.Model):
    alternativa = models.ForeignKey(Alternativa, on_delete=models.CASCADE)
    quant_votos = models.IntegerField(default=0, null=True, blank=True)
    data_voto = models.DateField(auto_now=True)

    def __str__(self):
        return self.alternativa.loja.nome + " | " + self.alternativa.nome_alternativa + " | Votos: " + \
               str(self.quant_votos) + " | " + str(self.data_voto)

    class Meta:
        verbose_name = "Voto"
        verbose_name_plural = "Votos"