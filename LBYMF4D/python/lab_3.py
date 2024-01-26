#importing libraries
import time
import serial
from vpython import *

#declaring variables
mode = 0
tempF = 0
tempC = 0
humidity = 0

#defining the serial port and baud rate of arduino

#arduino = serial.Serial('/dev/cu.usbmodem11101' , 115200) #mac
arduino = serial.Serial('COM3', 115200) #pc

#declaring lists
labels = ("Farenheit", "Celcius", "Humidity")
colors = (color.red, color.yellow, color.blue)
measurements = (tempF, tempC, humidity)
units = ("°F", "°C", "%")

#objects to be used from vpython
cylindersx = cylinder(pos=vector(0,-30,0), axis=vector(0,-5,0), color=colors[mode], size=vector(40, measurements[mode], 40), radius=measurements[mode])
labelsx = label(text=labels[mode], pos=vector(0, 100, 0), height=20)
labelsy = label(text= f"{measurements[mode]}{units[mode]}", pos=vector(0, 80, 0), height=15)

#function of changing the mode
def change_mode():
    global mode
    mode = (mode + 1) % 3
    update()

#function updating the variables accessed from the lists
def update():
    cylindersx.color = colors[mode]
    cylindersx.size.y = measurements[mode]
    cylindersx.radius=measurements[mode]
    labelsx.text = labels[mode]
    labelsy.text = f"{measurements[mode]}{units[mode]}"

#function to read the data from arduino serial
while True:
    data = arduino.readline().decode('utf-8').strip()
    datalist = data.split(',')

#assigning variables to the data gathered from the arduino
    tempF = float(datalist[0])
    tempC = float(datalist[1])
    humidity = float(datalist[2])
    button = float(datalist[3])

#button press
    if button == 1:
        change_mode()

    measurements = (tempF, tempC, humidity)
    print(f"Temperature: {tempF}°F, {tempC}°C | Humidity: {humidity}% | Button State: {button} | Current mode: {mode}")
    update()