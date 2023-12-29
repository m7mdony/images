import cv2
import numpy as np
import os
def check(path):
    counter1=0
    counter2=0
    for filename in os.listdir(path):
        file_path= os.path.join(path,filename)
        
        with open(file_path,"r") as file:
            for line in file:
                if line[0]=="0":
                    counter1+=1
                elif line[0]=="1":
                    counter2+=1
    print(f' the annotations for the label 0 is {counter1}')
    print(f' the annotations for the label 1 is {counter2}')
# Example usage
images_path="images"
labels_path="labels"

check(labels_path)
