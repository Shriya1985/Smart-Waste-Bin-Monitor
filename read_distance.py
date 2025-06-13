# read_distance.py
import serial # type: ignore
import time

ser = serial.Serial('COM3', 9600, timeout=1)  # Capital 'S'

while True:
    line = ser.readline().decode().strip()
    if line.isdigit():
        print(f"Distance: {line} cm")
        with open("data3.txt", "w") as f:
            f.write(line)
    time.sleep(0.5)
