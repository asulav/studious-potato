from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MainSerializer, RelationshipSerializer, JsonDump
from .models import Person

class CreateNode(APIView):
    def post(self, request):
        first_name = request.GET["firstName"]
        last_name = request.GET["lastName"]
        age = request.GET["age"]
        person = Person.get_or_create(firstName=first_name, lastName=last_name, age=age)
        to_send = MainSerializer(person)
        return Response(to_send, status=status.HTTP_200_OK)

class GetNode(APIView):
    def get(self, request):
        user_id = request.GET["uid"]
        person = Person.nodes.get_or_none(uid=user_id)
        if person is None:
            return Response(JsonDump(person), status=status.HTTP_200_OK)
        to_send = MainSerializer(person)
        return Response(to_send, status=status.HTTP_200_OK)

class ConnectNodes(APIView):
    def post(self, request):
        user_id = request.GET["uid"]
        rel_type = request.GET["rel_type"]
        rel_object = request.GET["rel_object"]
        person = Person.nodes.get_or_none(uid=user_id)
        if person is None:
            return Response(JsonDump(person), status=status.HTTP_200_OK)
        person.connect(rel_type, rel_object)
        to_send = MainSerializer(person)
        return Response(to_send, status=status.HTTP_200_OK)

class GetRelationship(APIView):
    def get(self, request):
        user_id = request.GET["uid"]
        person = Person.nodes.get_or_none(uid=user_id)
        if person is None:
            return Response(JsonDump(person), status=status.HTTP_200_OK)
        to_send = RelationshipSerializer(person)
        return Response(to_send, status=status.HTTP_200_OK)

class GetAllNodes(APIView):
    def get(self, request):
        to_send = MainSerializer(Person.nodes.all())
        return Response(to_send, status=status.HTTP_200_OK)