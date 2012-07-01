import Views.vodView 
import Models.Camera
import time 
# import Utils.log as Log
import logging

class ActionController:
	'''VOD Action Controller
	'''
	
	def __init__(self, root):
		self.log = logging.getLogger(__name__)
		self.root = root
		self.view = None
		self.camera = Models.Camera.Camera()

		self.inPausedState = False
		self.updateInterval = self.camera.config.getint('vod','updateInterval')
		self.log.debug("ActionController started, updateInterval=%d" % self.updateInterval)

	def setView(self, view):
		self.view = view
		self.log.debug('Action Controller initialized with view')

	def pauseAction(self):
		if self.inPausedState:
			self.view.log_add("running")
			self.view.setStatus("running")		
			self.inPausedState = False
			self.root.after(self.updateInterval, self.updateLivePicture)
		else:
			self.view.log_add("paused")
			self.view.setStatus("paused")		
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
		if not self.inPausedState:
			self.view.set_photo_from_image(self.camera.getImage())
			self.view.setStatus("Recent picture take at  %s", now)
		else:
			self.view.setStatus("Paused - no picture taken at %s", now)

		self.root.after(self.updateInterval, self.updateLivePicture)
		self.log.debug('set callback to return after ' + str(self.updateInterval) + 'ms')
		return True               # continue calls if this is a callback of the idle loop

