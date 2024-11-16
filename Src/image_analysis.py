import os
from PIL import Image
import json
import matplotlib.pyplot as plt

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
            image = Image.open(image_path).convert("L")  # Convert RGB images to single-channel grayscale images
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
    print(f"Shape of image 0: {images[0].size}")
    print(f"Mode of the image 0: {images[0].mode}")
    print(f"Shape of mask 0: {masks[0].size}")
    print(f"Mode of the mask 0: {masks[0].mode}")
    # Plot the images
    plot_images(images, masks, metadata)

def plot_images(images, masks, metadata):
    # Extract the titles from the metadata
    titles = [meta.get("Subject disorder status") for meta in metadata]  # Extract the title from the metadata, or use a default value
    # Plot the images with segmentation masks overlaid
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))  # Create a 1x4 subplot grid
    for idx, ax in enumerate(axes):
        if idx < len(images) and idx < len(masks):
            # Blend the image and mask
            blended = Image.blend(images[idx], masks[idx], alpha=0.5)  # 50% transparency
            ax.imshow(blended)  # Display the blended image
            ax.set_title(titles[idx])  # Set the title from the metadata
        else:
            ax.axis("off")  # Hide empty subplots

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    load_data()
