import smbus
import sys
import os


bus = smbus.SMBus(1)
address = 0x4c

#os.putenv("PY_SMBUS","1")
os.environ["PY_SMBUS"] = "1"

if len(sys.argv) < 2:
    print("Call with cfg file as argument")
    exit()

filename = sys.argv[1]

cfg = []

for line in open(filename):
    l = line.strip()
    if not l.startswith("#"):
        cfg.append(l.split())


for config in cfg:
    if config[0] == "w":
        register = int(config[2], 16)
        value = int(config[3], 16)
        print("Setting register %x to %x" % (register, value))
        bus.write_byte_data(address, register, value)

