# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 15:59:10 2026

@author: rogue_system


"""
####Import libraries####
import serial
import serial.tools.list_ports
import time
import pandas as pd
from matplotlib import pyplot as plt
####################################

####Find Arduino Microcontroler####
def find_arduino():
    for port in serial.tools.list_ports.comports():
        if 'Arduino' in port.description or 'CH340' in port.description:
            return port.device
    return None

port = find_arduino()

if port:
    print(f"Found Arduino on {port}")
else:
    print("Arduino not found")
###################################


####Define Serial Port connection####
arduino = serial.Serial(port, 9600, timeout=2)
time.sleep(2)  # Wait for Arduino reset
###################################

#####Define command transmission function####
def send_command(cmd):
    arduino.write((cmd + '\n').encode())
    return arduino.readline().decode().strip()
####################################

####Send commands defined on the Arduino board####
for i in range(10):
    print(send_command("TEMP"))
    time.sleep(1)
    print(send_command("BARO")) 
    time.sleep(1)
    print(send_command("HUMIDITY"))
    time.sleep(1)
##################################################

####Properly terminate serial connection####
arduino.close()
##################################################