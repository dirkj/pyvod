import serial
import Utils.Config
import Queue
import threading
import logging

class K8090 (object):
	"Schnittstelle zum Velleman Board K8090 zum schalten von Relais per USB"
	
	config = Utils.Config.Config()
	cmdQueue = Queue.Queue()
	
	# Command constants:
	SWITCH_RELAY_ON = '\x11'
	SWITCH_RELAY_OFF = '\x12'
	TOGGLE_RELAY = '\x14'
	SET_BUTTON_MODE = '\x21'
	START_RELAY_TIMER = '\x41'
	SET_RELAY_TIMER_DELAY = '\x42'
	QUERY_RELAY_STATUS = '\x18'
	QUERY_TIMER_DELAY = '\x44'
	QUERY_BUTTON_MODE = '\x22'
	QUERY_JUMPER_STATUS = '\x70'
	QUERY_FIRMWARE_VERSION = '\x71'
	RESET_FACTORY_DEFAULT = '\x66'
	
	# Event constants:
	BUTTON_MODE = '\x22'
	TIMER_DELAY = '\x44' # works with relay # (0..7) as well: TIMER_DELAY_0 for relay #0
	BUTTON_STATUS = '\x50'
	RELAY_STATUS = '\x51'
	JUMPER_STATUS = '\x70'
	FIRMWARE_VERSION = '\x71'
	
	RelayMappingMaskToNumber = { 1: 1, 2: 2, 4: 3, 8: 4, 16: 5, 32: 6, 64: 7, 128: 8} 
	RelayMappingNumberToMask = { 1: 1, 2: 2, 3: 4, 4: 8, 5: 16, 6: 32, 7: 64, 8: 128}
	
	def __init__ (self):
		self.log = logging.getLogger(__name__)
		self.port = self.config.get('k8090', 'port', 'COM8')
		self.baudrate = self.config.getint('k8090', 'baudrate',19200)
		self.timeout = self.config.getint('k8090', 'timeout',10)
		paritySupported = {
			"PARITY_NONE": serial.PARITY_NONE,
			"PARITY_EVEN": serial.PARITY_EVEN,
			"PARITY_ODD": serial.PARITY_ODD,
			"PARITY_MARK": serial.PARITY_MARK,
			"PARITY_SPACE": serial.PARITY_SPACE }
		self.parity = paritySupported[self.config.get('k8090', 'parity', 'PARITY_NONE')]
		# self.stopbits = self.config.get('k8090', 'stopbits')
		self.serial = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=self.timeout, parity=self.parity)

		t1 = K8090CommandThread(self, self.cmdQueue, self.serial)
		t1.setDaemon(True)
		t1.start()
		
		t2 = K8090EventThread(self, self.serial)
		t2.setDaemon(True)
		t2.start()
	
	def addCommand(self, command, mask=0, param1=0, param2=0):
		self.log.debug('addCommand(command=%d, mask=%d, param1=%d, param2=%d' % (command, mask, param1, param2))
		cmd = {"command" : command, "mask" : mask, "param1" : param1, "param2" : param2}
		self.queue.add(cmd)

	def resetToFactoryDefault(self):
		"""Reset board to factory default settings; no parameters"""
		this.addCommand(this.RESET_FACTORY_DEFAULT)
		
	def queryRelayStatus(self):
		"""Query the current relay status and initiate a RELAY_STATUS event"""
		this.addCommand(this.QUERY_RELAY_STATUS)

		
			
class K8090CommandThread(threading.Thread):
	"""Threaded command execution for K8090 board"""

	def __init__(self, k8090, queue, serial):
		threading.Thread.__init__(self)
		this.k8090 = k8090
		self.queue = queue
		self.serial = serial

	def twosComplement(self, stringToBuildComplements):
		twosComplement = 0
		for c in stringToBuildComplements:
			twosComplement += ord(c)
		return ~twosComplement + 1
		
	def run(self):
		while True:
			#grabs command from queue
			command = self.queue.get()
			serialCommand = "\x04" + chr(command["command"]) + chr(command["mask"]) + chr(command["param1"]) + chr(command["param2"])
			serialCommand = serialCommand + chr(this.twosComplement(serialCommand)) + "\x0F"
			self.serial.write(serialCommand)
			self.queue.task_done()

			
class K8090EventThread():
	"""Threaded event receiver for K8090 board"""

	eventSubscriptions = []

	def __init__(self, k8090, serial):
		threading.Thread.__init__(self)
		this.k8090 = k8090
		self.serial = serial
	
	def run(self):
		while True:
			receivedEvent = ''
			charReceived = self.serial.read()
			while charReceived != '\x04': # wait for STX
				this.log.debug("ignoring character (%d) from K8090 while waiting for STX" % charReceived)
				charReceived = self.serial.read()
			checksum = 4 # STX	
			charReceived = self.serial.read()
			while charReceived != '\x0F': # wait for ETX
				receivedEvent = receivedEvent + chr(charReceived)
				checksum += ord(charReceived)
			
			# event interpretation
			if len(receivedEvent) != 5:
				this.log.error("corrupt event received from K8090: %s" % receivedEvent)
			else:
				event = receivedEvent[0]
				mask = receivedEvent[1]
				param1 = receivedEvent[2]
				param2 = receivedEvent[3]
				# senderChecksum = receivedEvent[4]
				
				if checksum != 0:
					log.error("Received message with invalid checksum! (event=%d, mask=%d, p1=%d, p2=%d)" % (event, mask, param1, param2))

				if event == this.k8090.BUTTON_MODE:
					for subscriber in self.eventSubscriptions:
						if subscriber["event"] == event:
							subscriber["queue"].add({"event" : event, "inMomentaryMode" : mask, "inToggleMode" : param1, "inTimedMode" : param2})
							
				if event == this.k8090.TIMER_DELAY:
					relay = RelayMappingMaskToNumber[mask]
					delay = (param1 << 8) + param2
					for subscriber in self.eventSubscriptions:
						relayEvent = event + '_' + chr(ord('0') + relay)
						if subscriber["event"] == event or subscriber["event"] == relayEvent:
							subscriber["queue"].add({"event" : subscriber["event"], "relay" : relay, "delay" : delay})
							
				if event == this.k8090.BUTTON_STATUS:
					for subscriber in self.eventSubscriptions:
						if subscriber["event"] == event:
							subscriber["queue"].add({"event" : event, "currentState" : mask, "pressedEvent" : param1, "releasedEvent" : param2})
					allEvents = pressedEvent | releasedEvent
					for relay in range(1,8):
						relayEvent = event + '_' + chr(ord('0') + relay)
						relayMask = RelayMappingNumberToMask[relay]
						if (allEvents & relayMask != 0) and subscriber["event"] == relayEvent:
							subscriber["queue"].add({"event" : relayEvent, "currentState" : mask & relayMask, "pressedEvent" : param1 & relayMask, "releasedEvent" : param2 & relayMask})
							
				elif event == this.k8090.RELAY_STATUS:
					for subscriber in self.eventSubscriptions:
						if subscriber["event"] == event:
							subscriber["queue"].add({"event" : event, "previousState" : mask, "currentState" : param1, "relayTimerState" : param2})
							
				elif event == this.k8090.JUMPER_STATUS:
					for subscriber in self.eventSubscriptions:
						if subscriber["event"] == event:
							subscriber["queue"].add({"event" : event, "set" : True if param1 > 1 else False})
							
				elif event == this.k8090.FIRMWARE_VERSION:
					for subscriber in self.eventSubscriptions:
						if subscriber["event"] == event:
							subscriber["queue"].add({"event" : event, "version" :  "%d.%02d" % (param1, param2)})
							
				else:
					this.log.error("Unknown event received: %d (mask=%d, p1=%d, p2=%d)" % (event, mask, param1, param2))
					
	def subscribeEvent(self, event, queue, relay = None):
		"""register a queue to be filled with given event types; if relay parameter is given, only events for given relay (1..8) are reported"""
		if relay != None:
			event = event + "_" + str(ord('0') + relay)
		this.eventSubscriptions.add({"event" : event, "queue" : queue})
