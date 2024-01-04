import cv2

image = cv2.imread("f.jpeg")
print(image.shape)
image =cv2.resize(image,(4000,4000))
cv2.imwrite("f.jpeg",image)