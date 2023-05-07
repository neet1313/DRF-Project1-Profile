from rest_framework import serializers
from Profiles_API import models


class helloSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=10)


# Model Serializer
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes User profile object"""
    class Meta:
        model = models.UserProfile
        fields = ['id', 'email', 'name']

        # Custom Field level validation
        # extra_kwargs = {
        #     'password': {
        #         'write_only': True,
        #         'style': {'input_type': 'password'}
        #     }
        # }


    # Overriding the default create() function so that
    # the password is created as a Hash and not a clear text.

    # def create(self, validated_data):
    #     """Create and return a new user"""
    #     user = models.UserProfile.objects.create_user(
    #         email=validated_data['email'],
    #         name=validated_data['name'],
    #         password=validated_data['password']
    #     )

    #     return user
