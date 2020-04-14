import board
import pulseio
import adafruit_irremote

# Derived from the tutorial found here:
# https://learn.adafruit.com/infrared-ir-receive-transmit-circuit-playground-express-circuit-python/ir-test-with-remote

IR_PIN = board.D2 # Pin connected to IR receiver.

# Logitech Z-5500 remote codes
power_code = [239, 16, 247, 8]
vol_up_code = [239, 16, 167, 88]
vol_down_code = [239, 16, 143, 112]
vol_mute_code = [239, 16, 151, 104]

print("IR Bit Decoder")

# Create pulse input and IR decoder.
pulse_in = pulseio.PulseIn(IR_PIN, maxlen=120, idle_state=True)
decoder = adafruit_irremote.GenericDecode()

# Loop waiting to receive pulses.
while True:
    # Receive pulses
    pulses = decoder.read_pulses(pulse_in)
    
    # Decode pulses
    try:
        received_code = decoder.decode_bits(pulses)
    except adafruit_irremote.IRNECRepeatException:
        # Received short code, possible repeat signal
        continue
    except adafruit_irremote.IRDecodeException:
        # Received invalid code
        continue
    
    print("We get signal: ", received_code)

    # Got a code, now compare.
    if received_code == power_code:
        print("Received power button")
    elif received_code == vol_up_code:
        print("Received volume up button")
    elif received_code == vol_down_code:
        print("Received volume down button")
    elif received_code == vol_mute_code:
        print("Received volume mute button")
    else:
        print("Received unknown code")
