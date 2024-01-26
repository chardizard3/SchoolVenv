'''import serial
import time
from vpython import *

cylinders = [cylinder1 = cylinder(pos=vec(0,-2,0), axis=vec(0,1,0), color=color.blue, radius=1, size=vec(1,1,1)), 
cylinder2 = cylinder(pos=vec(0,-2,0), axis=vec(0,1,0), color=color.yellow, radius=2, size=vec(2,2,2)),
cylinder3 = cylinder(pos=vec(0,-2,0), axis=vec(0,1,0), color=color.white, radius=3, size=vec(3,3,3))]

# Replace 'COMx' with the appropriate serial port where your Arduino is connected
arduinoData = serial.Serial('/dev/cu.usbmodem11101', 115200)

def read_button_state():
    ser.write(b'R')  # Send a character 'R' to request the button state
    time.sleep(0.1)  # Wait for the response
    return int(ser.readline().decode().strip())

while True:
        button_state = read_button_state()
        print("Button State:", button_state)
        time.sleep(1)
'''
from vpython import *
import serial
import time

#arduino = serial.Serial('/dev/cu.usbmodem11101', 115200) #for mac
arduino = serial.Serial('COM3', 115200) #for pc

#dictionary for the 3 mode measurements
modes = [{"label": "Cylinder Measurement 1", "color": color.red}, 
        {"label": "Cylinder Measurement 2", "color": color.green}, 
        {"label": "Cylinder Measurement 3", "color": color.blue}]


#reading sensor data
def read_sensor_data():   
    arduino.write(b"READ_SENSOR_DATA\n")
    arduino_data = ser.readline().decode('utf-8').rstrip()
    if arduino_data:
        return arduino_data.split(',')
    return None

current_measurement_index = 0

scene = canvas(width=900, height=600)

cylinder = cylinder(pos=vec(0,-1,0), axis=vec(0,1,0), radius=0.2, length=1, color=modes[current_measurement_index]["color"])

label(text=modes[current_measurement_index]["label"], align='center', pos=vector(0, 1, 0), height=30)

def change_mode(evt):
    global current_measurement_index
    current_measurement_index = (current_measurement_index + 1) % len(modes)
    
    cylinder.color = modes[current_measurement_index]["color"]
    label.text = modes[current_measurement_index]["label"]

scene.bind('keydown', change_mode)

while True:
    button_state = int(arduino.readline().decode().strip())
    dhtsensor = arduino.readline().decode('utf-8').rstrip()

    if button_state == 1:
        change_mode(None)

"""
def change_mode(current_mode):
    modes = ["Mode 1", "Mode 2", "Mode 3"]
    
    # Find the index of the current mode
    current_index = modes.index(current_mode)
    
    # Increment the index to move to the next mode
    next_index = (current_index + 1) % len(modes)
    
    # Get the next mode
    next_mode = modes[next_index]
    
    return next_mode

# Example usage:
current_mode = "Mode 1"
new_mode = change_mode(current_mode)
print(f"Current Mode: {current_mode}, New Mode: {new_mode}")
"""



"""

# Replace 'COMx' with your Arduino's serial port
arduino_port = 'COM3'
baud_rate = 115200

ser = serial.Serial(arduino_port, baud_rate, timeout=5)

def read_sensor_data():
    ser.write(b"READ_SENSOR_DATA\n")
    arduino_data = ser.readline().decode('utf-8').rstrip()
    if arduino_data:
        return arduino_data.split(',')
    return None

def read_button_state():
    ser.write(b"READ_BUTTON_STATE\n")
    return int(ser.readline().decode('utf-8').rstrip())

while True:
    sensor_data = read_sensor_data()
    button_state = read_button_state()

    if sensor_data:
        tempC, tempF, humidity = map(float, sensor_data)
        print(f"Temperature: {tempC}°C, {tempF}°F | Humidity: {humidity}%")
    
    print(f"Button State: {button_state}")

    time.sleep(2)  # Adjust the delay as needed

"""