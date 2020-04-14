import board
import time
import pulseio
import adafruit_irremote
from digitalio import DigitalInOut, Direction

# Basic test of IR transmitter. Every five seconds, send the power toggle code I learned from using main_ir_receiver_bits.py

IR_PIN = board.D2 # Pin connected to IR transmitter.
CARRIER_FREQ = 38000 # 38 kHz
DUTY_CYCLE = 2 ** 15 # 50% (range is 0-65536, 32768 (2^15) is 50% on/off, approximating a sine wave)

# Logitech Z-5500 remote codes
power_code = [239, 16, 247, 8]

# Onboard red LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# Create pulse output and IR encoder.
# See here for description of NEC protocol: https://techdocs.altium.com/display/FPGA/NEC+Infrared+Transmission+Protocol
pwm = pulseio.PWMOut(IR_PIN, frequency=CARRIER_FREQ, duty_cycle=DUTY_CYCLE)
pulse_out = pulseio.PulseOut(pwm)
encoder = adafruit_irremote.GenericTransmit(header=[9500, 4500], one=[550, 550], zero=[550, 1700], trail=0)

# Send power code once every five seconds
while True:
    led.value = True
    encoder.transmit(pulse_out, power_code)
    led.value = False
    time.sleep(5)
