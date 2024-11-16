import os
from PIL import Image
import json


def load_data():
    # Specify the directory where the files are located
    directory = "C://Users//DANIE//OneDrive//FAU//5. Semester//Data Science Survival Skills//Homework//Homework 03//Mini_BAGLS_dataset"
    # Initialize data structures to hold loaded data
    images = []
    masks = []
    metadata = []
    # Iterate through the files in the directory
    for i in range(4):  # Load the first 4 sets of files
        # Build file paths
        image_path = os.path.join(directory, f"{i}.png")
        mask_path = os.path.join(directory, f"{i}_seg.png")
        meta_path = os.path.join(directory, f"{i}.meta")
        # Load the image
        try:
            image = Image.open(image_path)
            images.append(image)
        except FileNotFoundError:
            print(f"Image file {image_path} not found.")
        # Load the segmentation mask
        try:
            mask = Image.open(mask_path)
            masks.append(mask)
        except FileNotFoundError:
            print(f"Segmentation mask file {mask_path} not found.")
        # Load the metadata which is saved in JSON format
        try:
            with open(meta_path, "r") as meta_file:
                meta_data = json.load(meta_file)  
                metadata.append(meta_data)
        except FileNotFoundError:
            print(f"Metadata file {meta_path} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON for file {meta_path}.")
    # Output the loaded data to check if everything is loaded correctly
    print("Loaded images:", len(images))
    print("Loaded masks:", len(masks))
    print("Loaded metadata:", len(metadata))
    if metadata:
        print("Metadata of first file:", metadata[0])


if __name__ == "__main__":
    load_data()
