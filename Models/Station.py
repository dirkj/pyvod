import Utils.Config
import logging
import xml.etree.ElementTree as ET

class Station (object):
	"Represents the station track layout as a schematic"

	config = Utils.Config.Config()

	def __init__ (self):
		self.log = logging.getLogger(__name__)
		self.schemaFile = 'Resources/' + self.config.get('stationscheme', 'file')
		tree = ET.parse(self.schemaFile)
		rootStation = ET.Element("station")
		# print "root=" + rootStation.tag

		colorsEL = tree.findall("colors/")
		tracksEL = tree.findall("tracks/")
		self.colors = list()
		
		for element in colorsEL:
			self.colors.append({"id":element.attrib["id"], "color": element.attrib["color"]})
			
		self.tracks = list()
		for element in tracksEL:
			self.tracks.append(element)
			
		self.drawingElements = tree.findall("schema/")

	def getColors(self):
		return self.colors

	def getTracks(self):
		return self.tracks

	def getDrawingElements(self):
		return self.drawingElements

if __name__ == "__main__":
    station = Station()
    

		

