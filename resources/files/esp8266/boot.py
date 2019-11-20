# This file is executed on every boot (including wake-boot from deepsleep)

try:
  import usocket as socket
except:
  import socket
import network
import esp
import uos
import machine
uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl
from machine import UART


esp.osdebug(None)
webrepl.start()
gc.collect()

led = machine.Pin(2, machine.Pin.OUT)

# SSID and Password configuration
########################################################
# ssid = 'BBG-Display'
# password = 'bbgdisplay'
#
# ap = network.WLAN(network.AP_IF)
# ap.active(True)
# ap.config(essid=ssid, password=password)
#
# while ap.active() == False:
#     pass
#
# print('Connection successful')
# print(ap.ifconfig())
########################################################
