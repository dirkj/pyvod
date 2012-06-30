#!/usr/bin/env python

# vod = Visual Occupancy Detector

from Tkinter import *
import time
import Utils.log as Log
import Utils.Config
import Views.vodView
import Controller.actionController

class VOD(object):       
	def __init__(self):
	    self.log = Log.get_logger(__name__)
	    self.log.debug("starting application ...")
	    self.config = Utils.Config.Config();
	    self.updateInterval = self.config.getint('vod','updateInterval')

	    self.root = Tk()
	    self.actionController = Controller.actionController.ActionController(self.root)
	    self.view = Views.vodView.VODView(self.root, self.actionController)
	    self.actionController.setView(self.view)
	    self.view.setStatus("Application started %s", "now")
	    self.updateLivePicture()
	    self.root.mainloop()
	    self.log.debug("stopping application ...")
            
	def updateLivePicture(self):
	    self.log.debug('updateLivePicture')
	    self.actionController.updateLivePicture()
	    self.log.debug('set callback to return after ' + str(self.updateInterval) + 'ms')
	    self.root.after(self.updateInterval, self.updateLivePicture)
	    return True		# continue calls if this is a callback of the idle loop
	
	def getCamera(self):
		return self.camera

	def cameraMoveRight(self, target):
		print 'Camera move right called'
		self.camera.moveRight()

if __name__ == "__main__":
	app = VOD()

