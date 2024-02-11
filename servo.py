import RPi.GPIO as GPIO
import time

def setup_servo(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    return GPIO.PWM(pin, 50)  # PWM frequency: 50Hz

def move_servo(servo, angle):
    duty = angle / 18 + 2
    servo.ChangeDutyCycle(duty)
    time.sleep(1)

if __name__ == "__main__":
    try:
        servo_pin = 6  # Assuming servo is connected to GPIO pin 6
        servo = setup_servo(servo_pin)
        if servo is None:
            print("Error: Unable to setup servo.")
            exit()

        servo.start(0)  # Start at 0 degrees

        while True:
            print("Moving servo to left (0 degrees)...")
            move_servo(servo, 0)
            time.sleep(1)

            print("Moving servo to right (180 degrees)...")
            move_servo(servo, 180)
            time.sleep(1)

    except KeyboardInterrupt:
        servo.stop()
        GPIO.cleanup()
    except Exception as e:
        print("Error:", e)
        GPIO.cleanup()
