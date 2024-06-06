from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
import requests
import time

# Use pigpio pin factory
factory = PiGPIOFactory()

print("Setup")

# Initialize the servo with the pigpio factory on GPIO pin 17 (physical pin 11)
servo = AngularServo(17, min_pulse_width=0.0006, max_pulse_width=0.0023, pin_factory=factory)

print("Starting")

# Function to get PID controller output from endpoint
def get_pid_output():
    endpoint_url = "http://127.0.0.1:5000/get_pid_output"
    try:
        response = requests.get(endpoint_url, timeout=5)
        if response.status_code == 200:
            pid_output = float(response.json().get('output', 0.0))  # Default to 0.0 if 'output' is not found
            return pid_output
        else:
            print(f"Error: Unable to fetch PID output - Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

while True:
    pid_output = get_pid_output()
    print(f"PID Output: {pid_output}")
    if pid_output is not None:
        # Scale the PID output to match servo angle range (-50 to 50 degrees)
        scaled_output = (pid_output + 6) / 12 * 100 - 50  # Adjust scaling factor as needed

        # Ensure scaled output is within valid range
        scaled_output = int(max(-50, min(50, scaled_output)))
        print(f"Angle = {scaled_output}")
        servo.angle = int(scaled_output)
        time.sleep(0.5)
    else:
        # Move the servo to the middle position if there is no response
        servo.angle = 0  # Middle position for standard servo

    time.sleep(0.5)  # Adjust sleep time as needed for responsiveness

