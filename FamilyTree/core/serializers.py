from neomodel.relationship_manager import RelationshipManager
import json

def PersonSerializer(self):
    node = {}
    node["uid"] = self.uid
    node["firstName"] = self.firstName
    node["lastName"] = self.lastName
    node["age"] = self.age

    return node


def RelationshipSerializer(self):
    relations = {}
    for rel_type in self.__dict__.keys():
        if isinstance(self.__getattribute__(rel_type), RelationshipManager):
            if not(self.__getattribute__(rel_type).all() is []):
                relations[rel_type] = []
                # rel_list = []
                for person in self.__getattribute__(rel_type).all():
                    relations[rel_type].append(PersonSerializer(person))
                    # rel_list.append({
                    #     f"{rel_type}": 
                    # })
                if len(relations[rel_type]) == 0:
                    relations.pop(rel_type)
    return relations if len(relations) is not 0 else "None"

def MainSerializer(self):
    node_properties = []
    try:
        for eachPerson in self:
            person = PersonSerializer(eachPerson)
            person["relations"] = {}
            person["relations"] = RelationshipSerializer(eachPerson)
            node_properties.append(person)
    except TypeError:
        person = PersonSerializer(self)
        person["relations"] = {}
        person["relations"] = RelationshipSerializer(self)
        node_properties.append(person)

    return json.dumps({
        "response": {
            "data": node_properties
        }
    })
