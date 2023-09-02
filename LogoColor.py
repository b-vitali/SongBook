import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys

def change_logo_color(input_image_path, output_image_path, new_color):
    # Load the image using matplotlib
    image = mpimg.imread(input_image_path)

    # Extract the alpha channel (transparency) from the image
    alpha_channel = image[:, :, 3]

    # Create a mask for the logo's transparency
    logo_mask = (alpha_channel > 0)

    # Create a new color image with the desired color
    colorized_image = np.zeros_like(image)
    colorized_image[:, :, :3] = np.array(new_color) / 255.0  # Normalize color values

    # Combine the colorized image with the original alpha channel
    result_image = np.copy(image)
    result_image[:, :, :3][logo_mask] = colorized_image[:, :, :3][logo_mask]

    # Save the result to a new PNG file
    plt.imsave(output_image_path, result_image)

    print(f"Colorized logo saved as {output_image_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 LogoColor.py rgb(x y z)")
        sys.exit(1)

    try:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        z = int(sys.argv[3])
    except ValueError:
        print("Invalid RGB values. Please provide integers for x, y, and z.")
        sys.exit(1)

    new_color = (x, y, z)
    input_image_path = "SongBook_logo_basic.png"  # Change to your image path
    output_image_path = "SongBook_logo.png"  # Change to your output image path

    change_logo_color(input_image_path, output_image_path, new_color)

