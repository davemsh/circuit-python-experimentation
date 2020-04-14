import board
import pulseio
import adafruit_irremote

# Derived from the tutorial found here: 
# https://learn.adafruit.com/ir-sensor/circuitpython

IR_PIN = board.D2  # Pin connected to IR receiver.

# Expected pulse, pasted in from previous recording REPL session:
# Logitech Z-5500 remote's power button
pulse = [9007, 4489, 572, 561, 575, 560, 576, 556, 549, 1664, 598,
         536, 580, 554, 582, 525, 600, 535, 580, 1658, 604, 1641,
         600, 1663, 579, 556, 580, 1660, 581, 1659, 602, 1638, 603,
         1664, 578, 556, 579, 555, 571, 563, 552, 555, 571, 1668, 574,
         561, 574, 532, 605, 555, 549, 1665, 596, 1650, 602, 1660,
         580, 1659, 603, 558, 547, 1666, 606, 1635, 607, 1660, 580]

print('IR Pulse Reader')

# Fuzzy pulse comparison function:
def fuzzy_pulse_compare(pulse1, pulse2, fuzzyness=0.2):
    if len(pulse1) != len(pulse2):
        return False
    for i in range(len(pulse1)):
        threshold = int(pulse1[i] * fuzzyness)
        if abs(pulse1[i] - pulse2[i]) > threshold:
            return False
    return True

# Create pulse input and IR decoder.
pulses = pulseio.PulseIn(IR_PIN, maxlen=200, idle_state=True)
decoder = adafruit_irremote.GenericDecode()
pulses.clear()
pulses.resume()

# Loop waiting to receive pulses.
while True:
    # Wait for a pulse to be detected.
    detected = decoder.read_pulses(pulses)
    print('got a pulse...')
    print(detected)

    # Got a pulse, now compare.
    if fuzzy_pulse_compare(pulse, detected):
        print('Received correct remote control press!')
