import os 
import shutil
import cv2

def check(images_path, labels_path):
    image_list = os.listdir(images_path)
    current_index = 0
    
    while current_index < len(image_list):
        filename = image_list[current_index]
        image_path = os.path.join(images_path, filename)
        labels_path_file = os.path.join(labels_path, filename[:-4] + ".txt")
        
        # Read the image
        image = cv2.imread(image_path)
        image = cv2.resize(image, (500, 500))
        height, width, _ = image.shape  # Get the image dimensions
        
        # Read annotations from the label file
        annotations = []
        with open(labels_path_file, "r") as file:
            for line in file:
                annotations.append(list(map(float, line.strip().split())))
        
            # Draw rectangles for each annotation
            for annotation in annotations:
                x, y, w, h = annotation[1:]
                xmin = int(x * width - w * width / 2)
                ymin = int(y * height - h * height / 2)
                xmax = int(x * width + w * width / 2)
                ymax = int(y * height + h * height / 2)
                
                cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

        # Show the image with rectangles
        cv2.imshow("Annotated Image", image)
        
        key = cv2.waitKey(0)
        if key == ord("q"):
            cv2.destroyAllWindows()
            break
        elif key == ord("b") and current_index > 0:
            current_index -= 1
        else:
            current_index += 1
        
       
        
            
            
    
images_path="images"
labes_path="labels"

check(images_path,labes_path)