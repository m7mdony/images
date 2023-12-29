

import cv2

# Read the original image
image = cv2.imread("pepsi.jpg")

# Resize the image
resized_image = cv2.resize(image, (640, 640))

# Overwrite the original image with the resized image
cv2.imwrite("pepsi.jpg", resized_image)

# Display the overwritten image
cv2.imshow("Resized and Overwritten Image", resized_image)

# Wait for a key event and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()