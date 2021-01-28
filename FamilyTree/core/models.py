#from django.db import models
from neomodel import StructuredNode, StringProperty, IntegerProperty
from neomodel import UniqueIdProperty, Relationship, RelationshipTo
import RelationshipProperty

class Picture(StructuredNode):
    uid = UniqueIdProperty()
    location = StringProperty(required=True)


class Person(StructuredNode):
    uid = UniqueIdProperty()
    firstName = StringProperty(required=True)
    lastName = StringProperty(required=True)
    age = IntegerProperty(default=0)
    picture = RelationshipTo('Picture', 'pic_location')
    relations = RelationshipProperty()

    def add_relationship(self, rel_type):
        self.relations[rel_type] = RelationshipTo("Person", rel_type)
        self.save()

    def connect(self, rel_type, rel_object):
        try:
            temp_rel = self.relations[rel_type]
            temp_rel.connect(rel_object)
            self.save()
        except KeyError:
            raise KeyError("The given relation could not be found")

    def get_name(self):
        return f"{self.firstName.capitalize()} {self.lastName.capitalize()}"

    def get_picture_location(self):
        return f"{self.picture.location}" if self.picture.location else None
