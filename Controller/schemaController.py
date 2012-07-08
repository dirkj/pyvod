import Views.schemaView 
import Models.Station
import logging

class SchemaController:
	'''Schema Action Controller
	'''
	
	def __init__(self, view=None):
		self.log = logging.getLogger(__name__)
		self.view = view

		self.log.debug("SchemaController started")
		self.station = Models.Station.Station()
		for color in self.station.getColors():
			self.view.addColorDef(color["id"], color["color"])
		tracks = self.station.getTracks()	# list of xml elements
		for dE in self.station.getDrawingElements():
			if dE.tag == "line":
				self.view.addLine(x1=dE.attrib["x1"], y1=dE.attrib["y1"], x2=dE.attrib["x2"], y2=dE.attrib["y2"], color=dE.attrib["color"], width=2, track=None if not "track" in dE.attrib else dE.attrib["track"])  
			elif dE.tag == "rectangle":
				self.view.addRectangle(x1=dE.attrib["x1"], y1=dE.attrib["y1"], x2=dE.attrib["x2"], y2=dE.attrib["y2"], color=dE.attrib["color"], width=2, track=None if not "track" in dE.attrib else dE.attrib["track"])  
			elif dE.tag == "circle":
				self.view.addCircle(x1=dE.attrib["x1"], y1=dE.attrib["y1"], r=dE.attrib["r"], color=dE.attrib["color"], track=None if not "track" in dE.attrib else dE.attrib["track"])  


	def setView(self, view):
		self.view = view
		self.view.setSchemaController(self)
		self.log.debug('view defined')

	def drawSchema(self):
		self.log.debug('drawSchema called')
		self.view.draw()


