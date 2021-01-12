from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
import json


class GetNodesData(APIView):
    def get(self, request):
        name = request.GET.get('name')
        person = Person.nodes.get_or_none(name=name)
        return Response(person)


class GetAllNodes(APIView):
    def get(self, request):
        return Response(Person.nodes.all())


class CreateNode(APIView):
    def post(self, request):
        data = json.loads(request.body)
        name = data['name']
        age = int(data['age'])
        response = ""
        try:
            response = Person(name=name, age=age).save()
        except:
            response = {"error": "Person already exists"}
        return Response(response)


class DeleteNode(APIView):
    def post(self, request):
        data = json.loads(request.body)
        name = data['name']
        response = ""
        try:
            response = Person.nodes.get(name=name).delete()
        except:
            response = {"error": "Person not found"}
        pass


class CreateRelations(APIView):
    def post(self, request):
        data = json.loads(request.body)
        relation = data['relationType']
