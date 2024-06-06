import random

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


pid_output = Value('d', 0.0)
pid_x = pd(Kp=0.2, Ki=0, Kd=0.01, target=0, min=0, max=0)


def updatePD():
    previous_number = 200
    while True:
        x = random.randint(100, 300)
        #print("hi" + str(x))
        for number in range(previous_number, x):
            pid_error = 200 - number
            #print(pid_error)
            pid_output_scaled = pid_x.update(pid_error)
            pid_output.value = pid_output_scaled
            

            time.sleep(0.1)  # Small delay to observe changes
        previous_number = x


pid_process = multiprocessing.Process(target=updatePD)
pid_process.start()


# Endpoint to get PID output
@app.route('/get_pid_output', methods=['GET'])
def get_pid_output():
    return jsonify({'output': pid_output.value}), 200


if __name__ == '__main__':
    app.run(port=5000)
