import serial
import time

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