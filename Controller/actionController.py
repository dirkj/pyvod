from Views.vodView import *
from Models.Camera import *
import time 
import Utils.log as Log

class ActionController:
	'''VOD Action Controller
	'''
	
	def __init__(self, root):
		self.log = Log.get_logger(__name__)
		self.root = root
		self.view = None
		self.camera = Camera()
		self.inPausedState = False
		self.updateInterval = self.camera.config.getint('vod','updateInterval')

	def setView(self, view):
		self.view = view
		self.log.debug('Action Controller initialized with view')

	def pauseAction(self):
		if self.inPausedState:
			self.view.log_add("running")
			self.view.status.set("running")		
			self.inPausedState = False
			self.root.after(self.updateInterval, self.updateLivePicture)
		else:
			self.view.log_add("paused")
			self.view.status.set("paused")		
			self.inPausedState = True
		return not self.inPausedState
		
	def showCameraParamAction(self):
		params = self.camera.getParams()
		for tuple in params:
			self.view.log_add('- ' + tuple[0] + ': ' + tuple[1])

	def cameraTurnLeft(self):
		self.view.log_add("camera turn left - nyi")

	def cameraTurnRight(self):
		self.view.log_add("camera turn right - nyi")

	def updateLivePicture(self):
		now = time.strftime("%H:%M:%S")
		self.view.set_photo_from_image(self.camera.getImage())
		self.view.setStatus("Recent picture take at  %s", now)
		self.root.after(1000, self.updateLivePicture)
		return True               # continue calls if this is a callback of the idle loop

