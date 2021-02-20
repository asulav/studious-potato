from django.conf.urls import url
from . import views

app_name = 'core'
urlpatterns = [
    url("get_all_nodes", views.GetAllNodes.as_view(), name='get_all_nodes'),
    url("get_node", views.GetNode.as_view(), name='get_node'),
    url("get_relationship", views.GetRelationship.as_view(), name='get_relationship'),
    url("create_node", views.CreateNode.as_view(), name='create_node'),
    url("connect_nodes", views.ConnectNodes.as_view(), name='connect_nodes'),
]