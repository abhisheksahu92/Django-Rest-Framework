from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination,CursorPagination

from .pagination import PersonPageNumberPagination,PersonLimitOffsetPagination,PersonCursorPagination
from .models import Person
from .serializers import PersonSerializer

# View with global pagenumber pagination
class PersonViews(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = PageNumberPagination

class PersonLocalPaginationViews(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = PersonPageNumberPagination

class PersonLimitOffsetViews(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = LimitOffsetPagination

    #Override LimitOffset
    # pagination_class = PersonLimitOffsetPagination

class PersonCursorViews(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = PersonCursorPagination
    

