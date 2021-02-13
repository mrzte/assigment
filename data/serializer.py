from rest_framework import serializers
from .models import DataDiri

class DataDiriSerializer(serializers.ModelSerializer):
    class Meta:
        model =  DataDiri
        fields=['id','nama_depan', 'nama_belakang', 'kelamin', 'pemilik','umur','kota','alamat','phone']