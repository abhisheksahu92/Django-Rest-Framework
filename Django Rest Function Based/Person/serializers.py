from rest_framework import serializers
from .models import Person 

class PersonSerial(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def validate_phone(self,value):
        if len(str(value)) != 10:
            raise serializers.ValidationError('Please input valid Phone Number')
        return value