import os
import random
import shutil

def move_images(input_folder, output_folders, percentages,input_folder2,output_folders2):
    print("hi")
    # Validate input
    if not os.path.exists(input_folder) or not os.path.isdir(input_folder):
        print("Invalid input folder path.")
        return

    if len(output_folders) != len(percentages):
        print("Number of output folders and percentages should be the same.")
        return

    total_percentage = sum(percentages)
    if total_percentage> 1 or total_percentage<0:
        print("Percentages should add up to 1.0.")
        return
    print("hey")
    # Get a list of all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Loop through each image and move it to one of the output folders based on percentages
    for image_file in image_files:
        rand_num = random.random()  # Generate a random number between 0 and 1
        cumulative_percentage = 0

        for i, percentage in enumerate(percentages):
            cumulative_percentage += percentage
            if rand_num <= cumulative_percentage:
                
                output_folder = output_folders[i]
                output_path = os.path.join(output_folder, image_file)
                input_path = os.path.join(input_folder, image_file)

                txtname=image_file[:-4]+".txt"
                output_folder2 = output_folders2[i]
                output_path2 = os.path.join(output_folder2, txtname)
                input_path2 = os.path.join(input_folder2, txtname)
                # Move the image to the selected output folder
                shutil.move(input_path, output_path)
                shutil.move(input_path2, output_path2)
                break

if __name__ == "__main__":
    input_folder_path = "images"
    input_folder_path2 = "labels"
    output_folder_paths = ["train/images","valid/images", "test/images" ]
    output_folder_paths2 = ["train/labels","valid/labels", "test/labels" ]
    percentages = [0.8, 0.13, 0.07]

    move_images(input_folder_path, output_folder_paths, percentages,input_folder_path2,output_folder_paths2)
