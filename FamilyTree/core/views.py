from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from django.http import JsonResponse
import json


class GetNodesData(APIView):
    def get(self, request):
        name = request.GET.get('name', ' ')
        person = Person.nodes.get_or_none(name=name)
        return JsonResponse(person, safe=False)


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
        return JsonResponse(response, safe=False)


class DeleteNode(APIView):
    def post(self, request):
        pass


class CreateRelations(APIView):
    def post(self, request):
        pass
