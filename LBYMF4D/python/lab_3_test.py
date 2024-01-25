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

arduino = serial.Serial('/dev/cu.usbmodem11101', 115200)

modes = [
    {"label": "Cylinder Measurement 1", "color": color.red},
    {"label": "Cylinder Measurement 2", "color": color.green},
    {"label": "Cylinder Measurement 3", "color": color.blue}
]

current_measurement_index = 0

scene = canvas(width=900, height=600)

cylinder = cylinder(pos=vec(0,-1,0), axis=vec(0,1,0), radius=0.2, length=1, color=cylinders[current_measurement_index]["color"])

label(text=cylinders[current_measurement_index]["label"], align='center', pos=vector(0, 1, 0), height=30)

def update_display(evt):
    global current_measurement_index
    current_measurement_index = (current_measurement_index + 1) % len(cylinders)
    
    cylinder.color = cylinders[current_measurement_index]["color"]
    label.text = cylinders[current_measurement_index]["label"]

scene.bind('keydown', update_display)

while True:
    button_state = int(arduino.readline().decode().strip())
    
    if button_state == 1:
        update_display(None)

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