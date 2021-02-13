from django.db import models
from authentication.models import User

class DataDiri(models.Model):

    kelamin_pilih = [
        ('Perempuan', 'Perempuan'),
        ('Laki_laki', 'Laki_laki')
    ]

    pemilik = models.ForeignKey(to=User, on_delete=models.CASCADE)
    nama_depan = models.CharField(max_length=200)
    nama_belakang = models.CharField(max_length=200)
    alamat = models.TextField()
    phone = models.CharField(max_length=13)
    kelamin = models.CharField(choices=kelamin_pilih, max_length=255)
    umur = models.IntegerField()
    kota = models.IntegerField()

    def __str__(self):
        return self.nama_depan

