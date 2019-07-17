from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from .models import Sertifikat


# Create your views here.
def verifikasi(request):
    if request.method == "POST":
        kode = request.POST['kode']
        try:
            sertifikat = Sertifikat.objects.get(kode=kode)
            context = {'kode': kode, 'valid': True, 'sertifikat': sertifikat}
        except ObjectDoesNotExist:
            context = {'kode': kode, 'valid': False}
        return render(request, 'verifikasi_sertifikat/sertifikat_result.html', context)
    return render(request, 'verifikasi_sertifikat/sertifikat_result.html')
