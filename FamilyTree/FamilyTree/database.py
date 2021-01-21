"""
Django Settings for Neo4j
This file will contain the configurations
for connecting to the an existing neo4j
instance. This maybe used to setup neo4j
clusters
"""
import os
from neomodel import db, util, remove_all_labels, install_all_labels
from neo4j.exceptions import AuthError, ServiceUnavailable
from importlib import import_module

class Neo4j:
	'''
	Define a class to interact with Neomodels
	'''
	def __init__(self):
		'''
		The base config comes from the following url.
		https://neomodel.readthedocs.io/en/latest/getting_started.html
		'''
		self.user = os.environ.get('DB_USERNAME', 'neo4j')
		self.password = os.environ.get('DB_PASSWORD', 'user_pass')
		self.hostname = os.environ.get('DB_HOSTNAME', 'db')
		self.port = os.environ.get('DB_PORT', 7687)

	def connect(self):
		self.conf = f"bolt://{self.user}:{self.password}@{self.hostname}:{self.port}"
		try:
			db.set_connection(self.conf)
		except AuthError:
			raise ValueError(f"The following user_name: {self.user} and password: {self.password.__hash__()} is invalid")
		except ServiceUnavailable:
			raise ValueError(f"The following host or port could not be resolved. Please retry after verifying")

	def clear_database(self, clear_constraints=False, clear_indexes=False):
		'''
		This is going to be removed after the mvp
		'''
		util.clear_neo4j_database(db,clear_constraints,clear_indexes)

	def change_password(self, new_password):
		if not new_password:
			raise ValueError(f"new_password must not be null. Given: {new_password.__hash__}")
		util.change_neo4j_password(db, new_password)

	def install_labels(self, modules):
		if isinstance(modules, str):
			import_module(modules)
		elif isinstance(modules, list):
			(import_module(module) for module in modules)
		else:
			raise ValueError("Make sure modules is either of type str or list")
		install_all_labels()

	def remove_labels(self, modules):
		if isinstance(modules, str):
			import_module(modules)
		elif isinstance(modules, list):
			(import_module(module) for module in modules)
		else:
			raise ValueError("Make sure modules is either of type str or list")
		remove_all_labels()

def startup():
	database = Neo4j()
	database.connect()
	return database