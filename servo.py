#import RPi.GPIO as GPIO
from time import sleep
import requests  # Import the requests library to make HTTP requests

print("Setup")
<<<<<<< HEAD
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
p = GPIO.PWM(11, 50)
p.start(0)
=======
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(11, GPIO.OUT)
#p = GPIO.PWM(11, 50)
#p.start(0)
print("Starting")
>>>>>>> 1f1b6d85251b8826e3123376b6cb4164253a6afd

# Function to get PID controller output from endpoint
def get_pid_output():
    # Replace "PID_ENDPOINT_URL" with the actual endpoint URL
    endpoint_url = "http://192.168.0.91:5000/get_pid_output"
    try:
        response = requests.get(endpoint_url, timeout=5)
        if response.status_code == 200:
            pid_output = float(response.json()['output'])  # Assuming the output is in JSON format
            return pid_output
        else:
            print("Error: Unable to fetch PID output - Status code:", response.status_code)
            return None
    except Exception as e:
        print("Error:", e)
        return None

try:
    while True:
        pid_output = get_pid_output()
        print(pid_output)
        if pid_output is not None:
            # Scale the PID output to match servo PWM duty cycle range (0-100)
<<<<<<< HEAD
            p.ChangeDutyCycle(pid_output)
=======
            scaled_output = pid_output * 10  # Adjust scaling factor as needed

            # Ensure scaled output is within valid range
            scaled_output = max(0, min(100, scaled_output))

            #p.ChangeDutyCycle(scaled_output)
>>>>>>> 1f1b6d85251b8826e3123376b6cb4164253a6afd
            sleep(0.1)  # Adjust sleep time as needed for responsiveness
        else:
            # If PID output is not available, stop the servo
            #p.ChangeDutyCycle(0)
            sleep(1)  # Wait before retrying
except KeyboardInterrupt:
    #p.stop()
    GPIO.cleanup()
#Resets the GPIO pins back to defaults
