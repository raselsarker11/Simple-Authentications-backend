from rest_framework import serializers
from .models import UserModel

class UserSignUpSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = UserModel
        fields = ['user_type', 'username', 'first_name', 'last_name', 'profile_picture', 'email', 'password', 'confirm_password', 'address_line', 'city', 'state', 'pincode']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = UserModel.objects.create_user(**validated_data)
        return user
