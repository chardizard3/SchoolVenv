import time
import serial

arduinoData = serial.Serial('/dev/cu.usbmodem11101' , 115200)

time.sleep(1)

while True:
    while (arduinoData.inWaiting()==0):
        pass
    dataPacket = arduinoData.readline()
    dataPacket = str(dataPacket, 'utf-8')
    dataPacket = dataPacket.strip('\r\n')
    splitPacket = dataPacket.split(',')
    x = float(splitPacket[0])
    y = float(splitPacket[1])
    z = float(splitPacket[2])
    print('X = ',x,'Y = ',y,'Z = ',z)