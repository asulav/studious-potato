from django.apps import AppConfig
from FamilyTree.database import startup


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
    	db = startup()
