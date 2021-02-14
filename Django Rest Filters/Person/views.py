from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter,OrderingFilter

from .models import Person
from .serializers import PersonSerializer

# Create your views here.
class PersonViews(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['first_name','phone']
    filterset_fields = ['first_name','last_name']

class PersonSearchView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['first_name','last_name']

    #Starts with
    # search_fields = ['^first_name','^last_name']

