import cv2
import numpy as np
from facenet_pytorch import MTCNN, InceptionResnetV1


class PID:
    def __init__(self, Kp, Ki, Kd, target, min, max):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.target = target
        self.prev_error = 0
        self.integral = 0
        self.min = min
        self.max = max

    def update(self, current):
        error = self.target - current
        self.integral += error
        derivative = error - self.prev_error
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.prev_error = error

        # Map the output to the desired range (min_output to max_output)
        #output = max(self.min, min(self.max , output))
        #print(output)
        return output

