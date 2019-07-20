from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SeritifikatSerializer
from .models import Sertifikat


# NORMAL VIEWS
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

# API VIEW
@api_view(['GET', 'POST'])
@csrf_exempt
def check_certificate(request):
    """
    Check for validity of the certificate
    """
    if request.method == "GET":
        sertifikat = Sertifikat.objects.all()
        serializer = SeritifikatSerializer(sertifikat, many=True)
        return Response({
            "code": status.HTTP_200_OK,
            "message": "success",
            "status" : "success",
            "data" : serializer.data
        })
    if request.method == "POST":
        serializer = SeritifikatSerializer(data=request.data)
        if serializer.is_valid():
            return Response({
                "code": status.HTTP_200_OK,
                "message": "success",
                "status" : "success",
                "data" : serializer.data
            })
        return Response(serializer.errors, 
                        status=status.HTTP_404_NOT_FOUND)
