import Utils.Config
import logging
import xml.etree.ElementTree as ET

class Station (object):
	"Represents the station track layout as a schematic"

	config = Utils.Config.Config()

	def __init__ (self):
		self.log = logging.getLogger(__name__)
		self.schemaFile = config.get('stationscheme', 'file')
		self.schemaFile = '../Resources/weitingen-tracks.xml'
		tree = ET.parse(self.schemaFile)
		rootStation = ET.Element("station")
		# print "root=" + rootStation.tag

		self.colors = tree.findall("colors/")
		self.tracks = tree.findall("tracks/")
		
		# for a in colors:
		#	print "color="+a.attrib["id"]
			
		self.schemaElements = tree.findall("schema/")
		# for a in schemaElements:
		#	print a.tag + ": x1="  + a.attrib["x1"] + ", y1=" + a.attrib["y1"]
			
		#for subject in rootStation.findall("color"):
		#	print "subject=" + subject
		#	if subject.tag == "colors":
		#		print "color=" + color
		#		for colorET in subject:
		#			color[colorET.attrib["id"]] = colorET.attrib["color"]
		#			print "color " + colorET.attrib["id"] + "=" + colorET.attrib["color"]

if __name__ == "__main__":
    station = Station()
    

		

