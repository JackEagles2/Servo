import RPi.GPIO as GPIO

def get_used_pins():
    used_pins = []
    GPIO.setmode(GPIO.BCM)  # Set pin numbering scheme to BCM
    for pin in range(2, 28):  # Assuming Raspberry Pi 3 GPIO pins
        try:
            GPIO.setup(pin, GPIO.IN)
            used_pins.append(pin)
        except RuntimeError:
            pass  # Pin already in use
    GPIO.cleanup()  # Clean up GPIO settings
    return used_pins

if __name__ == "__main__":
    used_pins = get_used_pins()
    if used_pins:
        print("The following GPIO pins are being used:")
        print(used_pins)
    else:
        print("No GPIO pins are currently in use.")
