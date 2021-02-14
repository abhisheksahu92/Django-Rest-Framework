from .models import Person,Thoughts
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):
    # thoughts = serializers.StringRelatedField(many=True,read_only=True)
    # thoughts = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # thoughts = serializers.HyperlinkedIdentityField(many=True,read_only=True,view_name='thoughts-detail')
    thoughts = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='thoughts-detail')
    class Meta:
        model = Person
        fields = ['id','username','first_name','last_name','email','phone','thoughts']
    
class ThoughtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thoughts
        fields = '__all__'

class PersonModelSerializer(serializers.HyperlinkedModelSerializer):
    thoughts = ThoughtsSerializer(many=True,read_only=True)
    class Meta:
        model = Person
        fields = ['id','username','url','first_name','last_name','email','phone','thoughts']


    