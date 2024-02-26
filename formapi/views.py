from rest_framework import generics
from .models import FormModel
from .serializers import FormModelSerializer


class FormModelView(generics.ListCreateAPIView):
    queryset = FormModel.objects.all()
    serializer_class = FormModelSerializer
