from neomodel.relationship_manager import RelationshipManager
import json

def PersonSerializer(self):
    node = {}
    node["uid"] = self.uid
    node["first_name"] = self.firstName
    node["last_name"] = self.lastName
    node["age"] = self.age
    node["id"] = self.id

    return node


def RelationshipSerializer(self):
    relations = {}
    for rel_type in self.__dict__.keys():
        if isinstance(self.__getattribute__(rel_type), RelationshipManager):
            if not(self.__getattribute__(rel_type).all() is []):
                relations[rel_type] = []
                for person in self.__getattribute__(rel_type).all():
                    relations[rel_type].append(PersonSerializer(person))
                if len(relations[rel_type]) == 0:
                    relations.pop(rel_type)
    return JsonDump(relations) if len(relations) is not 0 else JsonDump("None")


def MainSerializer(self):
    node_properties = []
    try:
        for eachPerson in self:
            person = PersonSerializer(eachPerson)
            person["relations"] = RelationshipSerializer(eachPerson)
            node_properties.append(person)
    except TypeError:
        person = PersonSerializer(self)
        person["relations"] = RelationshipSerializer(self)
        node_properties.append(person)

    return JsonDump(node_properties)


def JsonDump(node_properties):
    return json.dumps({
        "response": {
            "data": node_properties
        }
    })