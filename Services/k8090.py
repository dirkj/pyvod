import serial

ser = serial.Serial()
ser.port = 8
if ser.isOpen():
	ser.close()
	
def ser_test():
	ser = serial.Serial(8, 2400, timeout=60)

	while True:
		x = ser.read()          # read one byte
		print x