import Utils.Config
import logging
import SignalLed

class CalibrationLed (SignalLed):
	"Represents the calibration LED"

	config = Utils.Config.Config()

	def __init__ (self, id, switchPort, x=None, y=None):
		SignalLed.__init__(id, switchPort, x, y)
		self.log = logging.getLogger(__name__)
		self.pixelX = None
		self.pixelY = None
		
	def setPixelPosition(self, x, y):
		self.pixelX = x
		self.pixelY = y
		
	def getRealXFromPixel(self, x, y):
		realX = (x - self.pixelX) * self.x + (y - self.pixelY) * self.y
		return realX
	
    

		

