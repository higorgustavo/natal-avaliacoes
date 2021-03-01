from django.db import models


class Estabelecimento(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Enquente(models.Model):
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    enquete_texto = models.TextField(max_length=500, verbose_name="Enquete")
    isAtiva = models.BooleanField(default=True, verbose_name="Enquete Ativa")
    data_enquete = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " | " + self.enquete_texto

    class Meta:
        verbose_name = "Enquete"
        verbose_name_plural = "Enquetes"
        ordering = ['-data_enquete']


class Alternativa(models.Model):
    enquete = models.ForeignKey(Enquente, on_delete=models.CASCADE)
    nome_alternativa = models.CharField(max_length=50, verbose_name="Alternativa", null=True, blank=True)
    emoji = models.CharField(max_length=100, verbose_name="Emoji", null=True, blank=True)
    # https://www.w3schools.com/charsets/ref_emoji.asp

    def __str__(self):
        return self.nome_alternativa + " | " + self.enquete.estabelecimento.nome

    class Meta:
        verbose_name = "Alternativa"
        verbose_name_plural = "Alternativas"
        ordering = ['nome_alternativa']


class Voto(models.Model):
    alternativa = models.ForeignKey(Alternativa, on_delete=models.CASCADE)
    quant_votos = models.IntegerField(default=0, null=True, blank=True)
    data_voto = models.DateField(auto_now=True)

    def __str__(self):
        return self.alternativa.enquete.enquete_texto + " | " + self.alternativa.nome_alternativa + " | Votos: " + \
               str(self.quant_votos) + " | " + str(self.data_voto)

    class Meta:
        verbose_name = "Voto"
        verbose_name_plural = "Votos"