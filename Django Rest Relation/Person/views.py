from django.shortcuts import render

from .serializers import PersonSerializer,ThoughtsSerializer,PersonModelSerializer
from .models import Person,Thoughts

from rest_framework.viewsets import ModelViewSet

# Create your views here.
class PersonView(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonModelView(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer

class ThoughtsView(ModelViewSet):
    queryset = Thoughts.objects.all()
    serializer_class = ThoughtsSerializer