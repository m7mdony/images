import os 
import shutil
import cv2
def separate(labels_path, images_path, new_images, new_labels):
    for filename in os.listdir(labels_path):
        label_path = os.path.join(labels_path, filename)
        image_path = os.path.join(images_path, filename[:-4] + ".jpg")

        with open(label_path, "r") as file:
            for line in file:
                if line.startswith("1"):
                    # Ensure the destination directories exist
                    if not os.path.exists(new_labels):
                        os.makedirs(new_labels)
                    if not os.path.exists(new_images):
                        os.makedirs(new_images)

                    # Construct new file paths
                    new_label_path = os.path.join(new_labels, filename)
                    new_image_path = os.path.join(new_images, filename[:-4] + ".jpg")

                    # Copy files
                    shutil.copyfile(label_path, new_label_path)
                    shutil.copyfile(image_path, new_image_path)

                    break
    # for filename in os.listdir(images_path):
        
    #     image_path = os.path.join(images_path,filename)
    #     labels_path=os.path.join(labels_path,filename[:-4]+".txt")
    #     image=cv2.imread(images_path)
    #     image=cv2.resize(image,display_size=(500,500))
    #     annotations=[]
    #     with open(labels_path,"r") as file:
    #         for line in file:
    #             annotations.append(line)
        
    #     for annotation in annotations:
            
                
        

labels_path = "valid/labels"
images_path = "valid/images"
new_images="images"
new_labels="labels"

separate(labels_path,images_path,new_images,new_labels)