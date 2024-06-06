from flask import Flask, jsonify, request
from pid import PID as pd
from multiprocessing import Value
import time
import multiprocessing

app = Flask(__name__)

y = 0
width = 720
x_center = width / 2
max = x_center / 10
range = max * 2

pid_output = Value('d', 0.0)
pid_x = pd(Kp=0.2, Ki=0, Kd=0.01, target=0, min=0, max=0)


def updatePD():
    while True:
        # Model code to get x coordinate
        # Get image
        e_time = time.time() % 40
        if e_time <= 20:
            y = (360 / 20) * e_time
        else:
            y = 360 - (360 / 20) * (e_time - 20)

        #y = 360

        max_x, min_x, _, _ = (y, y, 0, 0)  # Replace with model output
        x = (max_x + min_x) / 2

        pid_error = x_center - x
        pid_output_scaled = pid_x.update(pid_error) / max * 6 + max / 6
        pid_output.value = pid_output_scaled

pid_process = multiprocessing.Process(target=updatePD)
pid_process.start()
# Endpoint to get PID output
@app.route('/get_pid_output', methods=['GET'])
def get_pid_output():
    return jsonify({'output': pid_output.value}), 200


if __name__ == '__main__':
    app.run(port=5000)
