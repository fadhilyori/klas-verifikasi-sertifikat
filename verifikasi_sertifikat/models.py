from django.db import models

# Create your models here.
class Peserta(models.Model):
    namaDepan = models.TextField(max_length=60)
    namaBelakang = models.TextField(max_length=80)
    bergabungTanggal = models.DateTimeField(auto_now_add=True)
    lastUpdate = models.DateTimeField(auto_now=True)

class Kegiatan(models.Model):
    nama = models.TextField(max_length=120)
    deskripsi = models.TextField(max_length=500)
    tanggalMulai = models.DateField()
    tanggalSelesai = models.DateField()
    jamMulai = models.TimeField()
    jamSelesai = models.TimeField()

class Sertifikat(models.Model):
    tipe = models.CharField()
    kode = models.CharField()
    step = models.IntegerField()
    tanggalTerbit = models.DateField()