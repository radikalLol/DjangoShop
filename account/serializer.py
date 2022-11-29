from rest_framework import serializers
from .models import user
 
 
class UserSerializer(serializers.ModelSerializer):
 
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    password2 = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=False
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = user
        fields = ['username',  'first_name', 'email', 'password', 'password2', 'token']
        #user.cleaned_data['password2']

    def create(self, validated_data):
        return user.objects.create_user(**validated_data)
