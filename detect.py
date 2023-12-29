import cv2
import torch
from pathlib import Path
import sys
# Set the path to your local YOLOv5 repository
yolov5_path = Path('yolov5')

# Add YOLOv5 directory to the system path
sys.path.append(str(yolov5_path))


# Import YOLOv5 modules
from models.experimental import attempt_load
from utils.general import check_img_size, non_max_suppression, scale_coords
from utils.torch_utils import select_device

# Load YOLOv5 model
weights_path = 'weights/best.pt'
img_size = 640
device = select_device('0')  # Use 'cpu' if you don't have a GPU

model = attempt_load(weights_path, map_location=device)
model.eval()

# Open a video capture object (0 for default camera)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video feed
    ret, frame = cap.read()

    if not ret:
        break

    # Perform inference
    img0 = letterbox(frame, new_shape=img_size)[0]
    img = img0[:, :, ::-1].transpose(2, 0, 1)
    img = torch.from_numpy(img).to(device)
    img /= 255.0

    if img.ndimension() == 3:
        img = img.unsqueeze(0)

    # Inference
    pred = model(img)[0]

    # Apply NMS
    pred = non_max_suppression(pred, 0.4, 0.5)[0]

    # Display results on the frame
    if pred is not None and len(pred):
        pred[:, :4] = scale_coords(img.shape[2:], pred[:, :4], frame.shape).round()

        for det in pred:
            plot_one_box(det, frame, label='Object')

    # Show the frame with results
    cv2.imshow('YOLOv5 Object Detection', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
