#from django.db import models
from neomodel import StructuredNode, StringProperty, IntegerProperty
from neomodel import UniqueIdProperty, RelationshipTo
from neomodel.properties import ArrayProperty

class RelationshipMixin(object):
    def __init__(self):
        self.all = {}

    def add_relationship(self, model, rel_type):
        if None in (model, rel_type):
            raise ValueError(f"RelationShip Types cannot be null")
        self.all[rel_type] = RelationshipTo(model, rel_type).save()

    def all(self):
        return self.all

    def connect(self, rel_type, rel_object):
        try:
            temp_rel = self.all[rel_type]
            temp_rel.manager.connect(rel_object).save()
        except KeyError:
            raise KeyError("The given relation could not be found")

class Picture(StructuredNode):
    uid = UniqueIdProperty()
    location = StringProperty(required=True)

class Person(StructuredNode):
    uid = UniqueIdProperty()
    firstName = StringProperty(required=True)
    lastName = StringProperty(required=True)
    age = IntegerProperty(default=0)
    picture = RelationshipTo('Picture', 'pic_location')
    relationships = RelationshipMixin()

    def get_name(self):
        return f"{self.firstName.capitalize()} {self.lastName.capitalize()}"
    
    def get_picture_location(self):
        return f"{self.picture.location}" if self.picture.location else None

    def add_personal_relationship(self, type):
        self.relationships.add_relationship("Person", type)