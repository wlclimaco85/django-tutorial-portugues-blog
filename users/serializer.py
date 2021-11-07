from  rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustumer
        fields = ['id','username','status','cnpj','nome','first_name','last_name','email','password']