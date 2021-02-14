from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication

from .models import Person
from .serializers import PersonSerializer
from .permission import myPermission

# Create your views here.

class PersonModelViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [myPermission]