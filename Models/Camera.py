import sys
import re
import Image
import urllib2
from datetime import datetime,date
import time
import Utils.Config
import logging
import socket

class Camera (object):
	"Oeffnet und liest Bilder einer Kamera"

	config = Utils.Config.Config()

	def __init__ (self):
		self.log = logging.getLogger(__name__)
		self.resetCaches()
		self.timeout = 3
		self.tmpfilename = self.config.get('camera', 'tmpfile')
		self.baseurl = self.config.get('camera', 'baseurl') + '/'
		command_get = self.config.get('camera', 'command.get')
		user = self.config.get('camera', 'user')
		password = self.config.get('camera', 'password')
		self.userpwd_urlpar = "user="+user+"&pwd="+password

		self.getcmd = self.baseurl + command_get + '?' + self.userpwd_urlpar
		self.log.debug("Loading " + self.getcmd + " to " + self.tmpfilename)

	def getImage(self):
		img = None
		try:
			# loadresult = urllib.urlretrieve(self.getcmd, self.tmpfilename)
			self.log.debug('Getting camera picture using: ' + self.getcmd)
			self.log.debug('Requesting image ....')
			f = urllib2.urlopen(self.getcmd, timeout=self.timeout)
			image = f.read()
			self.log.debug('Writing temp file: ' + self.tmpfilename)
			of = open(self.tmpfilename, "wb")
			of.write(image)
			of.close()
			f.close()

		except urllib2.URLError, e:
			self.log.warn('Timeout occured while trying to grab a new image from the camera')

		except urllib2.URLError, e:
			if isinstance(e.reason, socket.timeout):
				self.log.warn('Timeout occured while trying to grab a new image from the camera')
			else:
				raise

		except IOError, e:
			if isinstance(e, socket.timeout):
				self.log.warn('Timeout occured while trying to grab a new image from the camera')
			else:
	 			self.log.error("IOError: " + e.reason + " (" + infile + ")")
 			pass

		img = Image.open(self.tmpfilename)
		self.log.debug('Got image: format=' + img.format + ', size=' + str(img.size[0]) + 'x' + str(img.size[1]) + ', mode=' + img.mode)
		return img

	def resetCaches(self):
		self.paramsCached = False
		self.configsCached = False

	def getParams(self):
		if not self.paramsCached:
			getparamsurl = self.baseurl + self.config.get('camera','command.getparam') + '?' + self.userpwd_urlpar
			uf = urllib2.urlopen(getparamsurl, timeout=self.timeout)
			self.params = re.findall(r'var\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*=\s*(.*);', uf.read())
			uf.close()
			# --> result ist ein array mit key/value pairs
			self.log.info('Got fresh params from camera')
		return self.params

	def getParam(self, param):
		self.getParams()
		for tuple in self.params:
			if tuple[0] == param:
				self.log.debug('Camera.getParam(' + param + ')=' + tuple[1])
				return tuple[1]
		return 0

	def getConfigs(self):
		if not self.configsCached:
			getparamsurl = self.baseurl + self.config.get('camera','command.getconfig') + '?' + self.userpwd_urlpar
			uf = urllib2.urlopen(getparamsurl, timeout=self.timeout)
			self.configs = re.findall(r'var\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*=\s*(.*);', uf.read())
			uf.close()
			# --> result ist ein array mit key/value pairs
			self.log.info('Got fresh configs from camera')
		return self.configs

	def getConfig(self, param):
		self.getConfigs()
		for tuple in self.configs:
			if tuple[0] == param:
				self.log.debug('Camera.getConfig(' + param + ')=' + tuple[1])
				return tuple[1]
		return 0

	def getBrightness(self):
		if not self.configsCached:
			self.getConfigs()
		brightness = int(self.getConfig('brightness')) >> self.config.getint('command.setbrightness_bitshift')
		return brightness

	def getContrast(self):
		if not self.configsCached:
			self.getConfigs()
		contrast = int(self.getConfig('contrast'))
		return contrast

	def moveCamera(self, moveCommand):
		uf = urllib2.urlopen(self.baseurl + self.config.get('camera',moveCommand) + '&' + self.userpwd_urlpar, timeout=self.timeout)
		uf.close()
		self.log.debug("moveCamera - moveCommand=%s" % moveCommand)

	def moveRight(self):
		self.moveCamera('command.moveright')

	def moveLeft(self):
		self.moveCamera('command.moveleft')

	def moveUp(self):
		self.moveCamera('command.moveup')

	def moveDown(self):
		self.moveCamera('command.movedown')

	def moveCenter(self):
		self.moveCamera('command.movecenter')

	def moveToPosition1(self):
		self.moveCamera('command.movetopos1')

	def setPositionAsPos1(self):
		self.moveCamera('command.setpos1')

	def moveToPosition2(self):
		self.moveCamera('command.movetopos2')

	def setPositionAsPos2(self):
		self.moveCamera('command.setpos2')

	def moveToPosition3(self):
		self.moveCamera('command.movetopos3')

	def setPositionAsPos3(self):
		self.moveCamera('command.setpos3')

	def setBrightness(self, newBrightness):
		self.moveCamera('command.setbrightness' % (newBrightness << self.config.getint('command.setbrightness_bitshift')))

	def setContrast(self, newContrast):
		self.moveCamera('command.setcontrast' % newContrast)

