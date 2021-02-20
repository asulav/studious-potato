#from django.db import models
from neomodel import StructuredNode, StringProperty, IntegerProperty
from neomodel import UniqueIdProperty, RelationshipTo

import core.relations as relations

class Picture(StructuredNode):
    uid = UniqueIdProperty()
    location = StringProperty(required=True)

class Person(StructuredNode):
    uid = UniqueIdProperty()
    firstName = StringProperty(required=True)
    lastName = StringProperty(required=True)
    age = IntegerProperty(default=0)
    picture = RelationshipTo('Picture', 'pic_location')
    
    # dynamic relationship creation
    for rel_type in relations.get_relations():
        setattr(StructuredNode, rel_type, RelationshipTo("Person", rel_type))

    def connect(self, rel_type, rel_object):
        try:
            getattr(self, rel_type).connect(rel_object)
        except KeyError:
            raise KeyError("The given relation could not be found")

    def get_name(self):
        return f"{self.firstName.capitalize()} {self.lastName.capitalize()}"

    def get_picture_location(self):
        return f"{self.picture.location}" if self.picture.location else None
