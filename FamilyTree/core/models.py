#from django.db import models
from neo4j import GraphDatabase
from django.conf import settings

# Create your models here.
class NeoDB:
    def __init__(self):
        config = settings.GRAPH_DATABASE
        self.driver = GraphDatabase.driver(
            config.url, auth=(config.user, config.password))

    def close(self):
        self.driver.close()

    def runQuery(self, query):
        return self.driver.session().run(query)

    def createNode(self, nodeName, age):
        query = f"CREATE (p:{nodeName} {{name: \"{nodeName}\", age: {age}}}) RETURN p"
        return self.runQuery(query)

    def deleteNodeQuery(self, nodeName, age):
        query = f"MATCH (p: {nodeName} {{name: \"{nodeName}\", age: {age}}}) DETACH DELETE p RETURN p"
        return self.runQuery(query)

    def createRelationQuery(self, node1, node2, relationType):
        # from front end get the first and second user to set their relation ship
        query = (f"MATCH (p1:{node1} {{name: \"{node1}\"}})"
                 f"MATCH (p2:{node2} {{name: \"{node2}\"}})" +
                 f"CREATE (p1)-[rel:{relationType}]->(p2)) RETURN rel")
        return self.runQuery(query)

    def removeRelationQuery(self, node1, node2, relationType):
        query = f"MATCH (p1:{node1} {{name: \"{node1}\",}})-[rel:{relationType}]->(p2:{node2} {{name: \"{node2}\"}})) DELETE rel"
        return self.runQuery(query)