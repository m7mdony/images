import onnxruntime
import cv2
import numpy as np

# Load the ONNX model
sess = onnxruntime.InferenceSession('weights/best.onnx')

# Print the names of the model inputs
input_names = [input.name for input in sess.get_inputs()]
print("Model Input Names:", input_names)

# Assuming there is only one input, use its name in the sess.run() call
if len(input_names) == 1:
    input_name = input_names[0]
else:
    raise ValueError("Multiple model inputs found. Update the code to handle multiple inputs.")

# Load the image
image = cv2.imread('test/images/12.jpg')
height, width, _ = image.shape

# Preprocess the image
input_image = cv2.resize(image, (416, 416))
input_image = input_image.astype(np.float32) / 255.0
input_image = np.transpose(input_image, (2, 0, 1))
input_image = np.expand_dims(input_image, axis=0)

# Perform inference
detections = sess.run(None, {input_name: input_image})

# Process the detections and draw bounding boxes
for det in detections:
    # Extract relevant information from the detection results
    class_ids = det[0][:, -1]
    confidences = det[0][:, -2]
    boxes = det[0][:, :-2]

    # Iterate through the detected objects
    for class_id, confidence, box in zip(class_ids, confidences, boxes):
        if confidence > 0.5:  # Adjust confidence threshold as needed
            x, y, w, h = box
            x = int(x * width)
            y = int(y * height)
            w = int(w * width)
            h = int(h * height)

            # Draw bounding box and label
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            label = f"Class {int(class_id)}: {confidence:.2f}"
            cv2.putText(image, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the result
cv2.imshow('Object Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
