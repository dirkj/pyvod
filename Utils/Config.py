import ConfigParser



class Config (object):
 "Liest Konfigurationsdatei für VisualDO"
 
 initialized = False
 config = ConfigParser.SafeConfigParser()
 configfile = ""
 
 def __init__ (self, configfile='Resources/config.ini'):
  if not self.initialized:
   self.initialized = True
   self.configfile = configfile
   self.config.read(configfile)

 def get(self, section, param):
  return self.config.get(section, param)

 def getint(self, section, param):
  return self.config.getint(section, param)

if __name__ == "__main__":
 c1 = Config()
 c2 = Config()
 print "url=", c1.get('camera','url'), "=", c2.get('camera','url')
 print "user=", c1.get('camera','user'), "=", c2.get('camera','user')
 
