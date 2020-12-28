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
        s = tx.run("MATCH (p1:Person {name: $user.firstUser}" +
                   "MATCH (p2:Person {name: $user.secondUser})" +
                   "CREATE (p1)-[rel:$user.relationType]->($p2))")
        pass

    def removeRelation(tx, user):
        # to do later
        pass


    def printGraph():
        # to do later
        # root -> traverse tree -> print
        pass
