import RPi.GPIO as GPIO

def check_pin(pin_number):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_number, GPIO.IN)
    pin_value = GPIO.input(pin_number)
    GPIO.cleanup()
    return pin_value

if __name__ == "__main__":
    pin_number = 6  # Replace with the GPIO pin you want to check
    try:
        pin_value = check_pin(pin_number)
        print(f"Pin {pin_number} is {'connected' if pin_value else 'not connected'}.")
    except Exception as e:
        print(f"Error: {e}")
