import Views.schemaView 
import logging

class SchemaController:
	'''Schema Action Controller
	'''
	
	def __init__(self, view=None):
		self.log = logging.getLogger(__name__)
		self.view = view

		self.log.debug("SchemaController started")


	def setView(self, view):
		self.view = view
		self.view.setSchemaController(self)
		self.log.debug('view defined')

	def drawSchema(self):
		self.log.debug('drawSchema called')
		self.view.draw()


