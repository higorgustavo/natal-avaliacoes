# from django.db import models
#
#
# class Loja(models.Model):
#     nome = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.nome
#
#
# class Opcao(models.Model):
#     OPCOES = [
#         ["Ruim", "Ruim"],
#         ["Normal", "Normal"],
#         ["Bom", "Bom"]
#     ]
#     loja = models.ForeignKey(Loja, on_delete=models.CASCADE, blank=True, null=True)
#     opcao_avaliacao = models.CharField(max_length=25, verbose_name="Opções", choices=OPCOES)
#
#     def __str__(self):
#         return self.loja.nome + "|" + self.opcao_avaliacao
#
#     class Meta:
#         verbose_name = "Opção"
#         verbose_name_plural = "Opções"
#
#
# class Voto(models.Model):
#     opcao = models.ForeignKey(Opcao, on_delete=models.CASCADE)
#     quant_votos = models.IntegerField()
#     data_voto = models.DateField(auto_now=True)