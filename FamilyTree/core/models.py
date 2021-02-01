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
        relationshipAttr = self.__getattribute__(rel_type)

        for name in relationshipAttr.__class__.__dict__.keys():
            obj = relationshipAttr.__class__.__dict__[name]
            if isinstance(obj, RelationshipDefinition):
                setattr(relationshipAttr.__class__, name, obj.build_manager(relationshipAttr, name))

        setattr(relationshipAttr.__class__, rel_type, relationshipAttr.build_manager(relationshipAttr, rel_type))
        self.save()

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
