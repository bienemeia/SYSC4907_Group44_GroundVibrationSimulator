#  Raspberry Pi Master for Arduino Slave
#  i2c_master_pi.py
#  Connects to Arduino via I2C

import sys
import smbus
import time

addr = 0x8 # bus address of Arduino
bus = smbus.SMBus(1) # indicates /dev/ic2-1

def getTemperature():
    try:
        return((bus.read_word_data(addr, 1)))
    except OSError:
        print("Failed to read I2C")
    
def getHumidity():
    try:
        return((bus.read_word_data(addr, 2)))
    except OSError:
        print("Failed to read I2C")

def ConvertStringToBytes(src):
    converted = []
    for b in src:
        converted.append(ord(b))
    return converted



