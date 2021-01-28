import uuid
from neomodel import Property
from neomodel.properties import validator

class RelationshipProperty(Property):
    def __init__(self, **kwargs):
        for item in ['required', 'unique_index', 'index', 'default']:
            if item in kwargs:
                raise ValueError('{} argument ignored by {}'.format(item, self.__class__.__name__))

        # kwargs['unique_index'] = True
        super(RelationshipProperty, self).__init__(**kwargs)

    @validator
    def inflate(self, value):
        uuid.UUID(value)
        return value

    @validator
    def deflate(self, value):
        uuid.UUID(value)
        return value