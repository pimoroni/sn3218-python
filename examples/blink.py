import time

import sn3218

lights = sn3218.SN3218()
lights.enable()
lights.enable_leds(0b111111111111111111)

state = True

while True:
    lights.output([state] * 18)
    state = not state
    time.sleep(1.0)


