
from django.db import models

class PomBensin(models.Model):
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

class Pembeli (models.Model):
    PomBensin= models.ForeignKey(PomBensin, related_name="pembeli", on_delete=models.CASCADE)
    nama = models.CharField(max_length=200)

    def __str__(self):
        return self.nama
