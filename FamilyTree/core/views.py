from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonSerializer
from .models import Person

class GetAllNodes(APIView):
    def get(self, request):
        Person.nodes.all()
        return Response('Temporary Data', status=status.HTTP_200_OK)
