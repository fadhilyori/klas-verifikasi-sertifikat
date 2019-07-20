from rest_framework import serializers
from .models import Sertifikat

class SeritifikatSerializer(serializers.ModelSerializer):
    identitas_user = serializers.SerializerMethodField('get_user')
    nomor_sertifikat = serializers.CharField(source='kode')
    nama_acara = serializers.SerializerMethodField('get_acara')
    tanggal_acara = serializers.DateField(source='tanggalTerbit')
    # TODO: Decide the right way to handle the url provided
    #alamat_menuju_sertifikat = serializers.CharField(source='')

    class Meta:
        model = Sertifikat
        fields = [
            "identitas_user",
            "nomor_sertifikat",
            "nama_acara",
            "tanggal_acara",
            #"alamat_menuju_sertifikat"
        ]

    def get_user(self, obj):
        return obj.peserta.nama

    def get_acara(self, obj):
        return obj.kegiatan.nama
