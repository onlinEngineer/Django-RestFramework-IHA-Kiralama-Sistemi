from django.db import models

from django.contrib.auth.models import User


class IHA(models.Model):
    KATEGORILER = (
        ('Küçük', 'Küçük'),
        ('Orta', 'Orta'),
        ('Büyük', 'Büyük'),
    )
    iha_id=models.AutoField(primary_key=True)
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    agirlik = models.DecimalField(max_digits=10, decimal_places=2)
    kategori = models.CharField(max_length=10, choices=KATEGORILER)
    eklenme_zamani=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.marka} {self.model}"

class Kiralama(models.Model):
    kiralama_id=models.AutoField(primary_key=True)
    iha = models.ForeignKey(IHA, on_delete=models.CASCADE)
    kiralayan_uye = models.ForeignKey(User, on_delete=models.CASCADE)
    kiralama_tarihi = models.DateField()
    iade_tarihi = models.DateField()
    kiralama_zamani=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.iha} - {self.kiralayan_uye.username}"