# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# ADS1100
# This code is designed to work with the ADS1100_I2CADC I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Analog-Digital-Converters?sku=ADS1100_I2CADC#tabs-0-product_tabset-2

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# ADS1100 address, 0x48(72)
# Select configuration register
#		0x0C(12)	Continuous conversion mode, 8 SPS, 1 PGA
bus.write_byte(0x48, 0x0C)

time.sleep(0.5)

# ADS1100 address, 0x48(72)
# Read data back from 0x00(00), 2 bytes
# raw_adc MSB, raw_adc LSB
data = bus.read_i2c_block_data(0x48, 0x00, 2)

# Convert the data
raw_adc = data[0] * 256 + data[1]
if raw_adc > 32767 :
	raw_adc -= 65536

# Output data to screen
print "Digital Value of Analog Input : %d " %raw_adc
