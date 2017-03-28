import smbus
import time

bus = smbus.SMBus(1)
address = 0x4c

gpio = 6

# select page 0
bus.write_byte_data(address, 0, 0)

# set GPIOX as output
bus.write_byte_data(address, 8, (1 << (gpio - 1)))

# set GPIO6 to register output
bus.write_byte_data(address, 79 + gpio, 0x02)

while True:

    # set GPIOX output high
    bus.write_byte_data(address, 86, (1 << (gpio - 1)))

    time.sleep(0.5)

    # set GPIOs output low
    bus.write_byte_data(address, 86, 0x0)

    time.sleep(0.5)

