from rest_framework import serializers

from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True,
                'max_length': 128,
                'min_length': 8,
            }
        }
