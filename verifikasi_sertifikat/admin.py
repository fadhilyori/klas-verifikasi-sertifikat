from django.contrib import admin
from django import forms
from django.urls import path
from django.shortcuts import redirect, render
from .models import Peserta, Kegiatan, Sertifikat
import csv
import io

class CsvSertifikatImportForm(forms.Form):
    csv_file = forms.FileField()
    kegiatan = forms.ModelMultipleChoiceField(queryset=Kegiatan.objects.all())
    tanggalTerbit = forms.DateField()

# Register your models here.
@admin.register(Peserta)
class PesertaAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path('import-csv/', self.import_csv)
        ]
        return new_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES['csv_file']
            reader = csv.reader(csv_file)
            # Peserta(nama)
            # TODO: Insert csv value to Model Peserta
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "admin/csv_form.html", payload)

@admin.register(Sertifikat)
class SertifikatAdmin(admin.ModelAdmin):
    
    change_list_template = "verifikasi_sertifikat/sertifikat_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path('import-csv/', self.import_csv)
        ]
        return new_urls + urls
    
    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES['csv_file'].read().decode('utf-8')
            io_string = io.StringIO(csv_file)
            reader = csv.reader(io_string)
            # Skip header and blank space
            while next(reader)[0] != '1':
                pass
            for row in reader:
                print(row)
                peserta, _ = Peserta.objects.get_or_create(nama=row[1])
                kegiatan = Kegiatan.objects.get(id=request.POST['kegiatan'])
                Sertifikat.objects.create(kode=row[2], peserta=peserta,
                                          kegiatan=kegiatan, tanggalTerbit=request.POST['tanggalTerbit'])
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvSertifikatImportForm()
        payload = {"form": form}
        return render(request, "admin/csv_form.html", payload)

admin.site.register(Kegiatan)
