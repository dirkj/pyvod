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
		self.addColorDef("__default", "black")
		self.addColorDef("__occupiedColor", "red")
		self.addColorDef("col1", "white")
		self.addColorDef("bgcol", "black")
		self.addColorDef("textcol", "white")
		self.drawingElements = []
		self.addDrawingTestData()	# remove if we can load drawing data from file

	def addDrawingTestData(self):
		self.addLine(10, 100, 600, 100, "col1", 2, "track1")
		self.addCircle(600, 100, 4, "col1", 1)
		self.addText(200, 100, "test track", "textcol")
		self.addLine(20, 100, 40, 120, "col1", 2)
		self.addLine(40, 120, 600, 120, "col1", 2, "track2")
		self.addRectangle(600, 112, 604, 128, "col1", 1)

	def setSchemaController(self, schemaController):
		self.schemaController = schemaController
		self.log.debug('schemaController set')
		
	def addColorDef(self, colorname, definition):
		self.colors[colorname] = definition

	def addLine(self, x1, y1, x2, y2, color, width=5, track=None):
		self.drawingElements.append({"type":"line", "track":track, "currentStateColor":color, "x1":x1, "y1":y1, "x2":x2, "y2":y2, "color":color, "width":width})

	def addCircle(self, x1, y1, r, color, width=5, track=None):
		self.drawingElements.append({"type":"circle", "track":track, "currentStateColor":color, "x1":x1, "y1":y1, "r":r, "color":color, "width":width})

	def addRectangle(self, x1, y1, x2, y2, color, width=5, track=None):
		self.drawingElements.append({"type":"rectangle", "track":track, "currentStateColor":color, "x1":x1, "y1":y1, "x2":x2, "y2":y2, "color":color, "width":width})

	def addText(self, x1, y1, text, text_color):
		self.drawingElements.append({"type":"text", "x1":x1, "y1":y1, "text":text, "text_color":text_color})

	def getColorDef(self,colorName):
		if self.colors[colorName]:
			return self.colors[colorName]
		else:
			return self.colors["__default"]

	def updateTrackStatus(self, track, isOccupied):
		self.log.debug("updateTrackStatus for track=" + track + ", setting isOccupied=" + str(isOccupied))
		for dE in self.drawingElements:
			if "track" in dE and dE["track"] == track:
				if isOccupied:
					dE["currentStateColor"] = "__occupiedColor"
				else:
					dE["currentStateColor"] = dE["color"]
		self.draw()


	def draw(self):
		for dE in self.drawingElements:
			if dE["type"] == "line":
				self.log.debug("draw line from %d,%d to %d,%d, color=%s", dE["x1"], dE["y1"], dE["x2"], dE["y2"], dE["currentStateColor"])
				self.canvas.create_line(dE["x1"], dE["y1"], dE["x2"], dE["y2"], width=dE["width"], fill=self.getColorDef(dE["currentStateColor"])) 
			if dE["type"] == "rectangle":
				self.log.debug("draw rectangle from %d,%d to %d,%d", dE["x1"], dE["y1"], dE["x2"], dE["y2"])
				self.canvas.create_rectangle(dE["x1"], dE["y1"], dE["x2"], dE["y2"], width=dE["width"], fill=self.getColorDef(dE["currentStateColor"]), outline=self.getColorDef(dE["currentStateColor"])) 
			if dE["type"] == "circle":
				self.log.debug("draw circle at %d,%d with radius %d", dE["x1"], dE["y1"], dE["r"])
				self.canvas.create_oval(dE["x1"] - dE["r"], dE["y1"] - dE["r"], dE["r"] + dE["x1"], dE["r"] + dE["y1"], width=dE["width"], fill=self.getColorDef(dE["currentStateColor"]), outline=self.getColorDef(dE["currentStateColor"])) 
			if dE["type"] == "text":
				self.log.debug("draw text at %d,%d with content %s", dE["x1"], dE["y1"], dE["text"])
				self.canvas.create_text(dE["x1"], dE["y1"], anchor="sw", text=dE["text"], fill=self.getColorDef(dE["text_color"])) 
