import sys
import re
import Image
import urllib2
from datetime import datetime,date
import time
import Utils.Config
import Utils.log as Log

class Camera (object):
	"Oeffnet und liest Bilder einer Kamera"

	config = Utils.Config.Config()

	def __init__ (self):
		self.log = Log.get_logger(__name__)
		self.resetCache()
		self.timeout = 3
		self.tmpfilename = self.config.get('camera', 'tmpfile')
		self.baseurl = self.config.get('camera', 'baseurl') + '/'
		command_get = self.config.get('camera', 'command.get')
		user = self.config.get('camera', 'user')
		password = self.config.get('camera', 'password')
		self.userpwd_urlpar = "user="+user+"&pwd="+password

		self.getcmd = self.baseurl + command_get + '?' + self.userpwd_urlpar
		# print "Loading ", self.urlcmd, "to", self.tmpfilename

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
 			img = Image.open(self.tmpfilename)
			self.log.debug('Got image: format=' + img.format + ', size=' + str(img.size[0]) + 'x' + str(img.size[1]) + ', mode=' + img.mode)
 			# print datetime.now().isoformat(), self.getcmd, img.format, "%dx%d" % img.size, img.mode

		except IOError, e:
 			print "IOError:", e.reason, infile
 			pass

		return img

	def resetCache(self):
		self.paramsCached = False

	def getParams(self):
		if not self.paramsCached:
			getparamsurl = self.baseurl + self.config.get('camera','command.getparam') + '&' + self.userpwd_urlpar
			uf = urllib2.urlopen(getparamsurl, timeout=2*self.timeout)
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

	def moveCamera(self, moveCommand):
		uf = urllib2.urlopen(self.baseurl + self.config.get('camera',moveCommand) + '&' + self.userpwd_urlpar, timeout=self.timeout)
		uf.close()

	def moveRight(self):
		self.moveCamera('command.moveright')

	def moveLeft(self):
		self.moveCamera('command.moveleft')

