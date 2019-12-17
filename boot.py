# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal
import machine
import epy
from machine import *
from epy import *
protect=WRITEPROTECT()
status=protect.get_status()
if status == 0:
    protect.write_protect(0x00000000,4096 * 1024)
