import Views.vodView 
import Models.Camera
import time 
# import Utils.log as Log
import logging

class ActionController:
	'''VOD Action Controller
	'''
	
	def __init__(self, tkroot):
		self.log = logging.getLogger(__name__)
		self.tkroot = tkroot
		self.view = None
		self.camera = Models.Camera.Camera()

		self.inPausedState = False
		self.updateInterval = self.camera.config.getint('vod','updateInterval')
		self.log.debug("ActionController started, updateInterval=%d" % self.updateInterval)

		# TODO: create instance of schemaController and pass to vodView and schemaView
		# self.schemaController = schemaController.SchemaController()
		

	def setView(self, view):
		self.view = view
		self.log.debug('Action Controller initialized with view')

	def pauseAction(self):
		if self.inPausedState:
			self.view.log_add("running")
			self.view.setStatus("running")		
			self.inPausedState = False
			# self.tkroot.after(self.updateInterval, self.updateLivePicture)
		else:
			self.view.log_add("paused")
			self.view.setStatus("paused")		
			self.inPausedState = True
		return not self.inPausedState
		
	def showCameraParamAction(self):
		self.camera.resetCaches()
		params = self.camera.getParams()
		for tuple in params:
			self.view.log_add('- ' + tuple[0] + ': ' + tuple[1])

	def showCameraExtParamAction(self):
		self.camera.resetCaches()
		params = self.camera.getExtParams()
		for tuple in params:
			self.view.log_add('- ' + tuple[0] + ': ' + tuple[1])

	def showCameraConfigAction(self):
		self.camera.resetCaches()
		params = self.camera.getConfigs()
		for tuple in params:
			self.view.log_add('- ' + tuple[0] + ': ' + tuple[1])

	def cameraTurnLeft(self):
		self.view.log_add("camera turn left")
		self.camera.moveLeft()

	def cameraTurnRight(self):
		self.view.log_add("camera turn right")
		self.camera.moveRight()

	def cameraTurnUp(self):
		self.view.log_add("camera turn up")
		self.camera.moveUp()

	def cameraTurnDown(self):
		self.view.log_add("camera turn down")
		self.camera.moveDown()

	def cameraMoveCenter(self):
		self.view.log_add("camera move to center position")
		self.camera.moveCenter()

	def cameraMoveToPosition1(self):
		self.view.log_add("camera move to stored position 1")
		self.camera.moveToPosition1()

	def cameraMoveToPosition2(self):
		self.view.log_add("camera move to stored position 2")
		self.camera.moveToPosition2()

	def cameraMoveToPosition3(self):
		self.view.log_add("camera move to stored position 3")
		self.camera.moveToPosition3()

	def saveCurrentPositionAsPos1(self):
		self.view.log_add("save current position as position #1")
		self.camera.setPositionAsPos1()

	def saveCurrentPositionAsPos2(self):
		self.view.log_add("save current position as position #2")
		self.camera.setPositionAsPos2()

	def saveCurrentPositionAsPos3(self):
		self.view.log_add("save current position as position #3")
		self.camera.setPositionAsPos3()

	def updateLivePicture(self):
		now = time.strftime("%H:%M:%S")
		if not self.inPausedState:
			self.view.set_photo_from_image(self.camera.getImage())
			self.view.setStatus("Recent picture take at  %s", now)
		else:
			self.view.setStatus("Paused - no picture taken at %s", now)

		self.tkroot.after(self.updateInterval, self.updateLivePicture)
		self.log.debug('set callback to return after ' + str(self.updateInterval) + 'ms')
		return True               # continue calls if this is a callback of the idle loop

	def changeBrightness(self, newBrightness):
		self.camera.setBrightness(newBrightness)

	def changeContrast(self, newContrast):
		self.camera.setContrast(newContrast)

	def startTest(self):
		self.log.debug("Test action called")
		self.view.schemaView.updateTrackStatus("track1", True)


