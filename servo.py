import RPi.GPIO as GPIO
import time

def setup_servo(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    return GPIO.PWM(pin, 50)  # PWM frequency: 50Hz

def move_servo(servo, angle):
    duty = angle / 18 + 2
    servo.start(duty)
    time.sleep(1)
    servo.stop()

if __name__ == "__main__":
    try:
        servo_pin = 6  # Assuming servo is connected to GPIO pin 6
        servo = setup_servo(servo_pin)

        while True:
            # Move servo to left (0 degrees)
            move_servo(servo, 0)
            time.sleep(1)

            # Move servo to right (180 degrees)
            move_servo(servo, 180)
            time.sleep(1)

    except KeyboardInterrupt:
        servo.stop()
        GPIO.cleanup()
    except Exception as e:
        print("Error:", e)
        GPIO.cleanup()
