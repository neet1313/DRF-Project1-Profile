from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from Profiles_API import models, serializers
from .custompermissions import CustomPermission
from rest_framework.authentication import TokenAuthentication


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of API view features."""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})


# ------- Model Viewset -------

class UserProfileViewset(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    # ---- Authentication and Permission -----
    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomPermission]
