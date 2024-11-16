import os
from PIL import Image
import json
import matplotlib.pyplot as plt
import numpy as np

def load_BAGLS_data():
    # Specify the directory where the files are located
    directory = "C://Users//DANIE//OneDrive//FAU//5. Semester//Data Science Survival Skills//Homework//Homework 03//Src//Mini_BAGLS_dataset"
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

    # Plot the images
    plot_images(images, masks, metadata)

def plot_images(images, masks, metadata):
    # Extract the titles from the metadata
    titles = [meta.get("Subject disorder status") for meta in metadata]  
    # Plot the images with segmentation masks overlaid
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))  # Create a 1x4 subplot grid
    for idx, ax in enumerate(axes):
        # Check if we have an image and mask to display
        if idx < len(images) and idx < len(masks):
            # Blend the image and mask
            blended = Image.blend(images[idx], masks[idx], alpha=0.5)  # 50% transparency
            ax.imshow(blended)  # Display the blended image
            ax.set_title(titles[idx])  # Set the title from the metadata
        else:
            ax.axis("off")  # Hide empty subplots

    plt.tight_layout()
    plt.show()

def load_leave_data():
    # Load the image (replace with the path to your .jpg file)
    image_path = "C://Users//DANIE//OneDrive//FAU//5. Semester//Data Science Survival Skills//Homework//Homework 03//Src//leaves.jpg"
    img = Image.open(image_path) # Load the leave image

    # Convert to NumPy array for pixel manipulation
    img_array = np.array(img)

    # Extract R, G, B channels
    R, G, B = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2]

    # Lightness method
    lightness = (np.maximum(R, np.maximum(G, B)) + np.minimum(R, np.minimum(G, B))) / 2

    # Average method
    average = (R + G + B) / 3

    # Luminosity method
    luminosity = 0.2989 * R + 0.5870 * G + 0.1140 * B

    # Create images for each grayscale converted image
    lightness_img = Image.fromarray(lightness.astype('uint8'))
    average_img = Image.fromarray(average.astype('uint8'))
    luminosity_img = Image.fromarray(luminosity.astype('uint8'))

    # Plot the results
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))

    # Set the overall title
    fig.suptitle("Different Grayscale Conversion Methods", fontsize=16)

    axes[0].imshow(img)
    axes[0].set_title("Original Image")
    axes[0].axis("off")

    axes[1].imshow(lightness_img, cmap="gray")
    axes[1].set_title("Lightness Method")
    axes[1].axis("off")

    axes[2].imshow(average_img, cmap="gray")
    axes[2].set_title("Average Method")
    axes[2].axis("off")

    axes[3].imshow(luminosity_img, cmap="gray")
    axes[3].set_title("Luminosity Method")
    axes[3].axis("off")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    load_BAGLS_data()
    load_leave_data()
