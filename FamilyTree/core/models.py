#from django.db import models
from neo4j import GraphDatabase


# Create your models here.
class ConnectDB:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def createUser(tx, user):
        s = tx.run(
            "CREATE (p:Person) {name: $user.name, age: $user.age}")

    def createRelation(tx, user):
        # from front end get the first and second user to set their relation ship
        s = tx.run("MATCH (p1:Person {name: $user.firstUser}" +
                   "MATCH (p2:Person {name: $user.secondUser})" +
                   "CREATE (p1)-[rel:$user.relationType]->(p2))")
        pass

    def reorderRelation(tx, graph):
        # do we need to reorder the tree so that the root
        # is the oldest member of the family
        pass

    def removeRelation(tx, user):
        s = tx.run(
            "MATCH (p1:Person {name: $user.firstUser})-[r:$user.relationType]->(p2:Person {name: $user.secondUser})" +
            "DELETE r")
        pass

    def printGraph():
        # how to traverse this tree and show to front end?
        # to do later
        # root -> traverse tree -> print
        pass
