from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from .models import Person
from .serializers import PersonSerial

# Create your views here.
class PersonView(APIView):
    parser_classes = [JSONParser]

    def get(self,request,format = None):
        person = Person.objects.all()
        serial = PersonSerial(person,many=True)
        return Response(serial.data)
    
    def post(self,request,format = None):
        serial = PersonSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        else:
            return Response({'msg':serial.errors})

# Create your views here.
class PersonDetailView(APIView):
    parser_classes = [JSONParser]

    def get(self,request,pk=None,format = None):
        person = Person.objects.filter(pk=pk)
        if person.exists():
            serial = PersonSerial(person.first())
            return Response(serial.data)
        else:
            return Response({'msg':'ID not found'},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format = None):
        person = Person.objects.filter(pk=pk)
        if person.exists():
            serial = PersonSerial(data=request.data,instance=person.first())
            if serial.is_valid():
                serial.save()
                return Response({'msg':'Data Updated'},status=status.HTTP_201_CREATED)
            else:
                return Response({'msg':serial.errors})
        return Response({'msg':'ID not found'},status=status.HTTP_400_BAD_REQUEST)


    def patch(self,request,pk,format = None):
        person = Person.objects.filter(pk=pk)
        if person.exists():
            serial = PersonSerial(data=request.data,instance=person.first(),partial=True)
            if serial.is_valid():
                serial.save()
                return Response({'msg':'Data Updated'},status=status.HTTP_201_CREATED)
            else:
                return Response({'msg':serial.errors})
        return Response({'msg':'ID not found'},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format = None):
        person = Person.objects.filter(pk=pk)
        if person.exists():
            person.first().delete()
            return Response({'msg':'Data Deleted'},status=status.HTTP_201_CREATED)
        return Response({'msg':'ID not found'},status=status.HTTP_400_BAD_REQUEST)