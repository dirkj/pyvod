import Utils.Config
import logging

class SignalLed (object):
	"Represents a LED that can be turned on/off and which knows it's location"

	config = Utils.Config.Config()

	def __init__ (self, id, switchPort, x=None, y=None):
		self.log = logging.getLogger(__name__)
		self.x = x
		self.y = y
		self.switchPort = switchPort
		self.id = id
		self.switchedOn = False
		

	def isOn(self):
		return self.switchedOn

	def setOn(self, switchOn = True):
		self.switchedOn = switchOn

	def setOff(self):
		self.switchedOn = False

	def getX(self):
		return self.x

	def setX(self, x):
		self.x = x

	def getY(self):
		return self.y

	def setY(self, y):
		self.y = y

    

		

