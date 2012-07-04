# File: vodView.py

from Tkinter import *
import Utils.log as Log

class SchemaView:
	'''Schema view to display schematic drawing of the station's track layout
	'''
	
	def __init__(self, tkparent, width=640, height=240, background="grey", schemaController = None):
		self.log = Log.get_logger(__name__)

		self.log.debug('View initialized')
		self.tkparent = tkparent
		self.width = width
                self.height = height
		self.background = background
		if not schemaController == None:
			self.setSchemaController(schemaController)
                self.canvas = Canvas(tkparent, width=self.width, height=self.height, background="green")
		self.colors = dict()
		self.addColorDef("default", "red")
		self.addColorDef("col1", "white")
		self.drawingElements = []
		self.addLine(10, 100, 600, 120, "col1", 5, "track1")

	def setSchemaController(self, schemaController):
		self.schemaController = schemaController
		self.log.debug('schemaController set')
		
	def addColorDef(self, colorname, definition):
		self.colors[colorname] = definition

	def addLine(self, x1, y1, x2, y2, color, width=5, track=None):
		self.drawingElements.append({"type":"line", "track":track, "x1":x1, "y1":y1, "x2":x2, "y2":y2, "color":color, "width":width})

	def addCircle(self, x1, y1, r, color, width=5, track=None):
		self.drawingElements.append({"type":"circle", "track":track, "x1":x1, "y1":y1, "r":r, "color":color, "width":width})

	def getColorDef(self,colorName):
		if self.colors[colorName]:
			return self.colors[colorName]
		else:
			return self.colors["default"]

	def draw(self):
		for dE in self.drawingElements:
			if dE["type"] == "line":
				self.log.debug("draw line from %d,%d to %d,%d", dE["x1"], dE["y1"], dE["x2"], dE["y2"])
				self.canvas.create_line(dE["x1"], dE["y1"], dE["x2"], dE["y2"], width=dE["width"], fill=self.getColorDef(dE["color"])) 
