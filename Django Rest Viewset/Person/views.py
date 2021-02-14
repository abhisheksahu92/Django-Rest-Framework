from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
 
# Create your views here.
class PersonViewSet(viewsets.ViewSet):
    def list(self,request):
        stu = Person.objects.all()
        serial = PersonSerializer(stu,many=True)
        return Response(serial.data)

    def create(self,request):
        serial = PersonSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        else:
            return Response({'msg':serial.errors})

    def retrieve(self,request,pk=None):
        person = Person.objects.filter(pk=pk)
        if person.exists():
            serial = PersonSerializer(person.first())
            return Response(serial.data)
        else:
            return Response({'msg':'ID not found'},status=status.HTTP_400_BAD_REQUEST)

    def delele(self,request,pk=None):
        person = Person.objects.filter(pk=pk)
        if person.exists():
            person.first().delete()
            return Response({'msg':'Data Deleted'},status=status.HTTP_201_CREATED)
        return Response({'msg':'ID not found'},status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        person = Person.objects.filter(pk=pk)
        if person.exists():
            serial = PersonSerializer(data=request.data,instance=person.first())
            if serial.is_valid():
                serial.save()
                return Response({'msg':'Data Updated'},status=status.HTTP_201_CREATED)
            else:
                return Response({'msg':serial.errors})
        return Response({'msg':'ID not found'},status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk=None):
        person = Person.objects.filter(pk=pk)
        if person.exists():
            serial = PersonSerializer(data=request.data,instance=person.first(),partial=True)
            if serial.is_valid():
                serial.save()
                return Response({'msg':'Data Updated'},status=status.HTTP_201_CREATED)
            else:
                return Response({'msg':serial.errors})
        return Response({'msg':'ID not found'},status=status.HTTP_400_BAD_REQUEST)