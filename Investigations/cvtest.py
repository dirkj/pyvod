#!/usr/bin/env python

# vod = Visual Occupancy Detector

from Tkinter import *
import time
#import Utils.Config
#import Views.vodView
#import Views.schemaView
#import Controller.actionController
#import Controller.schemaController
#import logging, logging.config

import cv2.cv as cv #Import functions from OpenCV

class VOD(object):       
	def __init__(self):
		#logging.config.fileConfig('Resources/vodlog.conf')
		#self.log = logging.getLogger(__name__)
		#self.log.info("starting application ...")
		#self.config = Utils.Config.Config();

		#self.root = Tk()

		#self.actionController = Controller.actionController.ActionController(self.root)
		#self.view = Views.vodView.VODView(self.root, self.actionController)
		#self.actionController.setView(self.view)
		#self.view.setStatus("Application started %s", time.strftime("%Y-%m-%d %H:%M:%S"))

		#self.schemaController = Controller.schemaController.SchemaController(self.view.getSchemaView())

		#self.actionController.updateLivePicture()
		#self.schemaController.drawSchema()
		#self.root.mainloop()
		
		cv.NamedWindow('a_window', cv.CV_WINDOW_AUTOSIZE)
		image=cv.LoadImage('picture.png', cv.CV_LOAD_IMAGE_COLOR) #Load the image
		font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8) #Creates a font
		x = 50 # x position of text
		y = 50 # y position of text
		cv.PutText(frame,"Hello World!!!", (x,y),font, 255) #Draw the text
		cv.ShowImage('a_window', image) #Show the image
		cv.Waitkey(10000)
		cv.SaveImage('image.png', image) #Saves the image

		self.log.debug("stopping application ...")

if __name__ == "__main__":
	app = VOD()

