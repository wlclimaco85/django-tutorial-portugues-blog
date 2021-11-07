from  rest_framework import serializers
from users.models import MyUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id','username','status','cnpj','nome','first_name','last_name','email','password']