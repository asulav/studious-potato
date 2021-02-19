from django.conf.urls import url
from . import views

app_name = 'core'
urlpatterns = [
    url("get_all_nodes", views.GetAllNodes.as_view(), name='get_all_nodes'),
]
