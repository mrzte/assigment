from django.shortcuts import render
from rest_framework import generics
from .serializer import DataDiriSerializer
from .models import DataDiri
from authentication.models import User
from rest_framework import permissions
from .permissions import IsPemilik

class DataDiriView(generics.ListCreateAPIView):
    serializer_class = DataDiriSerializer
    queryset = DataDiri.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsPemilik,)

    def perform_create(self, serializer):
        return serializer.save(pemilik=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(pemilik=self.request.user)



class DataDiriDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DataDiriSerializer
    queryset = DataDiri.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsPemilik)
    lookup_fields = "id"

    def get_queryset(self):
        return self.queryset.filter(pemilik=self.request.user)