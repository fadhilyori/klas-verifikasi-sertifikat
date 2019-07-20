from django.db import models


# TODO: Configure Models with real database that will be implemented

# Create your models here.
class Peserta(models.Model):
    nama = models.TextField(max_length=100, unique=True)
    email = models.EmailField(max_length=120, blank=True)
    alamat = models.TextField(max_length=250, blank=True)
    noTelepon = models.TextField(max_length=12, blank=True)
    pekerjaan = models.TextField(max_length=40, blank=True)
    instansi = models.TextField(max_length=50, blank=True)
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
    kode = models.CharField(max_length=120)
    kegiatan = models.ForeignKey(Kegiatan, on_delete=models.CASCADE)
    peserta = models.ForeignKey(Peserta, on_delete=models.CASCADE)
    tanggalTerbit = models.DateField()
