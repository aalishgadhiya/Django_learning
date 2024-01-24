from rest_framework import serializers
from home.models import Company,Employee,User_data
from django.contrib.auth.models import User

class CompanySerializer(serializers.ModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"
        
    
class EmployeeSerializer(serializers.ModelSerializer):
        id = serializers.ReadOnlyField()
        # company_details = CompanySerializer(source='company_name', read_only=True)
        # company_url = serializers.HyperlinkedRelatedField(view_name='company_name', read_only=True)

        company_name = serializers.StringRelatedField()
        class Meta:
            model=Employee
            fields="__all__"
            
            
            
class RegisterSerializer(serializers.Serializer):
       
        username = serializers.CharField()
        email = serializers.EmailField()
        password = serializers.CharField()
    
        
        def validate(self,data):
            if data['username']:
                if User.objects.filter(username=data['username']).exists():
                    raise serializers.ValidationError('user name is taken')
                        
            if data['email']:
                if User.objects.filter(email=data['email']).exists():
                    raise serializers.ValidationError('user email is taken')
            
            
            return data   
        
        
        def create(self, validated_data):
            #  print(validated_data)
             user = User.objects.create(username=validated_data['username'],email=validated_data['email'])
             user.set_password(validated_data['password'])
             user.save()
             return validated_data 
                        
               
               
               
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()               
    