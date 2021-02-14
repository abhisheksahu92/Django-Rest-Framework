from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

from .models import Person
from .serializers import PersonSerializer

# Create your views here.
class PersonListCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

class PersonRetrieveUpdateDelete(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)

    def patch(self,request,*args, **kwargs):
        return self.partial_update(request,*args, **kwargs)