import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Define the path to your PNG logo image with a transparent background
input_image_path = "SongBook_logo_basic.png"

# Load the image using matplotlib
image = mpimg.imread(input_image_path)

# Define the color you want to change to (as an RGB tuple)
# Divide the color values by 255 to bring them into the 0..1 range
new_color = (0, 255, 127)  # Change this to your desired color (e.g., blue)

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
output_image_path = "SongBook_logo.png"
plt.imsave(output_image_path, result_image)

print(f"Colorized logo saved as {output_image_path}")

