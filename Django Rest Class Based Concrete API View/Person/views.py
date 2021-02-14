from .models import Person
from .serializers import PersonSerial

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.
class PersonView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerial

class PersonDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerial