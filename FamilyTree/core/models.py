import neomodel as neomodel

# Create your models here.


class Person(neomodel.StructuredNode):
    uid = neomodel.UniqueIdProperty()
    name = neomodel.StringProperty(unique_index=True)
    age = neomodel.IntegeryProperty(index=True, default=0)
    relations = []

    def createRelation(self, relationType):
        self.relations.push(neomodel.Relationship("Person", relationType))

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getRelations(self):
        return self.relations
