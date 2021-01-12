from django.urls import path

from . import views

urlpatterns = [
    path('createNode', views.CreateNode.as_view(), name='createNode'),
    path('getNode', views.GetNodesData.as_view(), name='getNode')
]
