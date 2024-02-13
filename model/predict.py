import torch
import cv2
import torch
from torchvision.transforms.functional import to_pil_image
from PIL import Image, ImageDraw
import numpy as np

# Define the function to make predictions
import torch

# Define the function to make predictions

model = torch.hub.load('ultralytics/yolov5', 'custom','/servo/model/best.pt')

frame = cv2.imread(
    '/football-recorder/code/model/data/test/images/img1.jpg')  # Replace 'image.jpg' with the path to your image file

# Convert the image from BGR to RGB (OpenCV loads images as BGR by default)
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

print(model(frame))
frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# Convert the frame to PIL Image for drawing
#frame_pil = to_pil_image(frame_rgb)

results = model(frame_rgb)
# Create a drawing object
#draw = ImageDraw.Draw(frame_pil)

# Extract bounding boxes and class predictions
for pred in results.xyxy[0]:
    print(pred)
    box = pred[0:4]  # Extract bounding box coordinates (x_min, y_min, x_max, y_max)
    cls = int(pred[5])  # Extract predicted class
    score = float(pred[4])  # Extract confidence score
    # Convert bounding box coordinates to integers
    box_int = [int(coord) for coord in box]

    # Draw bounding box and class label
    #draw.rectangle(box_int, outline="red", width=3)

    #draw.text((box[0], box[1] - 10), f"Class: {cls}, Score: {score:.2f}", fill="red")

# Convert PIL Image back to OpenCV format for display
#frame_with_predictions = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)

# Display the frame with predictions
#cv2.imshow('Frame with Predictions', frame_with_predictions)
#cv2.waitKey(0)
#cv2.destroyAllWindows()