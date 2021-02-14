from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonSerial
from .models import Person
# Create your views here.

@api_view(['GET','POST'])
def personapi(request):
    if request.method == 'GET':
        person = Person.objects.all()
        serial = PersonSerial(person,many=True)
        return Response(serial.data)

    if request.method == 'POST':
        for person in request.data:
            serial = PersonSerial(data=person)
            if serial.is_valid():
                serial.save()
                return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
            else:
                return Response({'msg':serial.errors})
    
@api_view(['GET','PUT','PATCH','DELETE'])
def persondetailapi(request,id=None):
    if request.method == 'GET':
        person = Person.objects.filter(id=id)
        if person.exists():
            person = person.first()
            serial = PersonSerial(person)
            return Response(serial.data)
        return Response({'msg':'ID not found'},status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        for person in request.data:
            person_instance = Person.objects.filter(id=id)
            if person_instance.exists():
                serial = PersonSerial(data=person,instance=person_instance.first())
                if serial.is_valid():
                    serial.save()
                    return Response({'msg':'Data Updated'},status=status.HTTP_201_CREATED)
                else:
                    return Response({'msg':serial.errors}) 
            return Response({'msg':'ID not found'},status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        for person in request.data:
            person_instance = Person.objects.filter(id=id)
            if person_instance.exists():
                serial = PersonSerial(data=person,instance=person_instance.first(),partial = True)
                if serial.is_valid():
                    serial.save()
                    return Response({'msg':'Data Updated'},status=status.HTTP_201_CREATED)
                else:
                    return Response({'msg':serial.errors}) 
            return Response({'msg':'ID not found'},status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        person = Person.objects.filter(id=id)
        if person.exists():
            person = person.first()
            person.delete()
            return Response({'msg':'Data Deleted'},status=status.HTTP_200_OK)
        return Response({'msg':'ID not found'},status=status.HTTP_400_BAD_REQUEST)