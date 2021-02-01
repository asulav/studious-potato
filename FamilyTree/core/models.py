#from django.db import models
from neomodel import StructuredNode, StringProperty, IntegerProperty, RelationshipDefinition
from neomodel import UniqueIdProperty, RelationshipTo

class Picture(StructuredNode):
    uid = UniqueIdProperty()
    location = StringProperty(required=True)


class Person(StructuredNode):
    uid = UniqueIdProperty()
    firstName = StringProperty(required=True)
    lastName = StringProperty(required=True)
    age = IntegerProperty(default=0)
    picture = RelationshipTo('Picture', 'pic_location')

    def add_relationship(self, rel_type):
        if(hasattr(self, rel_type)):
            return f"Relationship already exists"
        
        setattr(self, rel_type, RelationshipTo("Person", rel_type))
        self.__dict__[rel_type] = self.__getattribute__(rel_type).build_manager(self, rel_type)

    def connect(self, rel_type, rel_object):
        try:
            self.__getattribute__(rel_type).connect(rel_object)
            self.save()
        except KeyError:
            raise KeyError("The given relation could not be found")

    def get_name(self):
        return f"{self.firstName.capitalize()} {self.lastName.capitalize()}"

    def get_picture_location(self):
        return f"{self.picture.location}" if self.picture.location else None
