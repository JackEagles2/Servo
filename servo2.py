from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# Use pigpio pin factory
factory = PiGPIOFactory()

# Initialize the servo with the pigpio factory
s = AngularServo(17, min_pulse_width=0.0006, max_pulse_width=0.0023, pin_factory=factory)

while True:
    s.angle = 90
    sleep(2)
    s.angle = 0
    sleep(2)
    s.angle = -90
    sleep(2)
