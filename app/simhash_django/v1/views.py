from rest_framework import viewsets

from simhash_django.models import SimHash
from simhash_django.calculate_simhash import calculate_simhash
from .serializers import SimHashSerializer


class HashViewSet(viewsets.ModelViewSet):

    queryset = SimHash.objects.all()
    serializer_class = SimHashSerializer

    def create(self, request, *args, **kwargs):
        calculate_simhash(request.data)
        return super().create(request, *args, **kwargs)
