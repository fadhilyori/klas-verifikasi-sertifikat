from django.urls import path
from .views import check_certificate, verifikasi

# TODO: Change URL to appropriate one
urlpatterns = [
    path('verify/', check_certificate, name="verifikasi-api"),
    path('', verifikasi, name='verifikasi'),
]