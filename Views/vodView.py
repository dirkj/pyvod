# File: vodView.py

from Tkinter import *
from Views.tkSimpleStatusBar import *
from PIL import Image, ImageTk
import Utils.log as Log
import schemaView

class VODView:
	'''VOD view componenten managing all visual elements of the VOD main window.
	Methods:
	* VODView(parent) creates the window content incl. menu+statusbar, where parent is the toplevel window
	* set_photo(photo) to change the display of the camera view
	* log_add(message) to add an entry to the logviewer
	* set_status(format, args) sets the status bar using formatted print
	'''
	
	def __init__(self, master, actionController = None, schemaController = None):
		self.log = Log.get_logger(__name__)
		self.setActionController(actionController)
		self.setSchemaController(schemaController)
		self.menubar = self.create_menubar(master)
		self.toolbar = self.create_toolbar(master)

		self.content = self.create_content(master)
		self.content.pack(fill=X)

		# STATUS LINE
		self.status = StatusBar(master)
		self.status.pack(side=BOTTOM, fill=X)
		
		# Other initializations
		self.log_add("VOD")
		self.log_add("-- App start --")

	def setActionController(self, actionController):
		self.actionController = actionController
		self.log.debug('View initialized with actionController')
		
	def setSchemaController(self, schemaController):
		self.schemaController = schemaController
		
	def set_photo_from_image(self, image):
		self.set_photo(ImageTk.PhotoImage(image))
		self.log_add('Updated image from image')

	def set_photo_from_file(self, photofile):
		image = Image.open(photofile)
		self.set_photo_from_image(image)
		self.log_add('Updated image from file ' + photofile)

	def set_photo(self, photo):
		self.livepicture_photo = photo
		self.livepicture_canvas.photo = self.livepicture_photo # keep reference, otherwise garbage collection destroys photo data
		self.livepicture_canvas.itemconfigure(self.photo_item, image=photo)
		
	def create_content(self, master):
		# CONTENT
		# 2 columns: right column = log, left column = live pic + cam_toolbar + schema
		# Live Picture

		frame = Frame(master, padx=5, pady=5, background="red")
		# start with logview to be able to start logging
		self.logview = self.create_logview(frame)

		self.livepicture_canvas = livepicture_canvas = Canvas(frame, width=640, height=480, background="cyan")
		self.photo_item = livepicture_canvas.create_image(0, 0, anchor=NW) #, image=self.livepicture_photo)
		self.set_photo_from_file("Resources/testbild.jpg")
		livepicture_canvas.grid(row=0, column=0, sticky=W)
		
		# CAM Toolbar
		cam_toolbar = self.create_camera_toolbar(frame) # Frame(frame)
		# b = Button(cam_toolbar, text="Pause", command=self.actionController.pauseAction)
		# b = Button(cam_toolbar, text="Pause", command=self.actionController.pauseAction)
		# b.pack(side=LEFT, padx=2, pady=2)

		# b = Button(cam_toolbar, text="Camera Param", command=self.actionController.showCameraParamAction)
		# b.pack(side=LEFT, padx=2, pady=2)

		cam_toolbar.grid(row=1, column=0, sticky=W)
		
		# Schema
		self.schemaView = schemaView.SchemaView(frame, width=640, height=240, background="green", schemaController=self.schemaController)

		self.schemaView.canvas.grid(row=2, column=0, sticky=W)
		
		# Logview
		self.logview.grid(row=0, column=1, rowspan=3, sticky=W+E+N+S)

		# button = Button(frame, text="QUIT", fg="red", command=frame.quit).pack(side=LEFT)
		# hi_there = Button(frame, text="Hello", command=self.say_hi).pack(side=LEFT)
		return frame
	
	def create_menubar(self, master):
		# MENU
		menubar = Menu(master)
		# menubar.add_command(label="Pause", command=self.pause_callback)
		# menubar.add_command(label="Camera Param", command=self.getparam_callback)
		#
		# create a pulldown menus, and add it to the menu bar
		vodmenu = Menu(menubar, tearoff=0)
		vodmenu.add_command(label="Options", command=self.say_hi)
		vodmenu.add_command(label="Save", command=self.say_hi)
		vodmenu.add_separator()
		vodmenu.add_command(label="Exit", command=master.quit)
		menubar.add_cascade(label="VOD", menu=vodmenu)
		#
		cameramenu = Menu(menubar, tearoff=0)
		cameramenu.add_command(label="Pause/Run", command=self.togglePauseRun)
		cameramenu.add_command(label="Parameter", command=self.actionController.showCameraParamAction)
		cameramenu.add_command(label="Turn left", command=self.actionController.cameraTurnLeft)
		cameramenu.add_command(label="Turn right", command=self.actionController.cameraTurnRight)
		cameramenu.add_command(label="Turn up", command=self.actionController.cameraTurnUp)
		cameramenu.add_command(label="Turn down", command=self.actionController.cameraTurnDown)
		menubar.add_cascade(label="Camera", menu=cameramenu)
		#
		helpmenu = Menu(menubar, tearoff=0)
		helpmenu.add_command(label="About", command=self.say_hi)
		menubar.add_cascade(label="Help", menu=helpmenu)
		#
		master.config(menu=menubar)
		return menubar

	def create_logview(self, master):
		logview = Text(master)
		logview.config(state=DISABLED)
		return logview

	def log_add(self, message):
		self.logview.config(state=NORMAL)
		self.logview.insert(END, message + "\n")
		self.logview.config(state=DISABLED)
		self.logview.see(END)
		self.log.debug("Logview: " + message)
		
	def create_camera_toolbar(self, master):
		camera_toolbar = Frame(master, background="GREY")

		# Postions Toolbar
		toolbar = Frame(camera_toolbar, background="GREY")
		b = Button(toolbar, text="Move to #1", command=self.actionController.cameraMoveToPosition1)
		b.pack(side=LEFT, padx=2, pady=2)

		b = Button(toolbar, text="Move to #2", command=self.actionController.cameraMoveToPosition2)
		b.pack(side=LEFT, padx=2, pady=2)

		b = Button(toolbar, text="Move to #3", command=self.actionController.cameraMoveToPosition3)
		b.pack(side=LEFT, padx=2, pady=2)

		b = Button(toolbar, text="Store #1", command=self.actionController.saveCurrentPositionAsPos1)
		b.pack(side=LEFT, padx=2, pady=2)

		b = Button(toolbar, text="Store #2", command=self.actionController.saveCurrentPositionAsPos2)
		b.pack(side=LEFT, padx=2, pady=2)

		b = Button(toolbar, text="Store #3", command=self.actionController.saveCurrentPositionAsPos3)
		b.pack(side=LEFT, padx=2, pady=2)

		toolbar.pack(side=TOP, fill=X)

		# Config Toolbar
		toolbar = Frame(camera_toolbar, background="GREY")
		l = Label(toolbar, text="Brightness")
		l.pack(side=LEFT, padx=2, pady=2)
		w = Scale(toolbar, from_=0, to=15, orient=HORIZONTAL, command=self.changeBrightness)
		w.pack(side=LEFT, padx=2, pady=2)
		self.brightnessScale = w

		l = Label(toolbar, text="Contrast")
		l.pack(side=LEFT, padx=2, pady=2)
		w = Scale(toolbar, from_=0, to=6, orient=HORIZONTAL, command=self.changeContrast)
		w.pack(side=LEFT, padx=2, pady=2)
		self.contrastScale = w

		toolbar.pack(side=TOP, fill=X)

		camera_toolbar.pack(side=TOP, fill=X)
		return camera_toolbar

	def create_toolbar(self, master):
		# TOOLBAR
		toolbar = Frame(master, background="WHITE")
		b = Button(toolbar, text="Pause", command=self.togglePauseRun)
		b.pack(side=LEFT, padx=2, pady=2)
		self.pauseRunButton = b

		b = Button(toolbar, text="Camera Param", command=self.actionController.showCameraParamAction)
		b.pack(side=LEFT, padx=2, pady=2)

		b = Button(toolbar, text="Camera Config", command=self.actionController.showCameraConfigAction)
		b.pack(side=LEFT, padx=2, pady=2)

		b = Button(toolbar, text="Camera Ext-Params", command=self.actionController.showCameraExtParamAction)
		b.pack(side=LEFT, padx=2, pady=2)

		b = Button(toolbar, text="Turn left", command=self.actionController.cameraTurnLeft)
		b.pack(side=LEFT, padx=2, pady=2)

		b = Button(toolbar, text="Turn right", command=self.actionController.cameraTurnRight)
		b.pack(side=LEFT, padx=2, pady=2)

		b = Button(toolbar, text="Turn Up", command=self.actionController.cameraTurnUp)
		b.pack(side=LEFT, padx=2, pady=2)

		b = Button(toolbar, text="Turn Down", command=self.actionController.cameraTurnDown)
		b.pack(side=LEFT, padx=2, pady=2)

		b = Button(toolbar, text="Move to Center", command=self.actionController.cameraMoveCenter)
		b.pack(side=LEFT, padx=2, pady=2)

		toolbar.pack(side=TOP, fill=X)
		return toolbar

	def togglePauseRun(self):
		self.actionController.pauseAction()
		if self.actionController.inPausedState:
			self.pauseRunButton["text"]="Run"
		else:
			self.pauseRunButton["text"]="Pause"

	def changeBrightness(self, par2):
		self.actionController.changeBrightness(self.brightnessScale.get())

	def changeContrast(self, par2):
		self.actionController.changeContrast(self.contrastScale.get())


	def say_hi(self):
		self.log_add("hi")

	def setStatus(self, format, *args):
		self.status.set(format % args)
		self.log.debug(("setStatus to " + format) % args)

	def getSchemaView(self):
		return self.schemaView

