import cv2
import numpy as np

# -----------------------------------------
# Dilation Morphological Operation
# -----------------------------------------

# Read the input image
image = cv2.imread("sample2.png")

# Check if image is loaded successfully
if image is None:
    print("Error: Could not load the image!")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert grayscale image to binary image
# Foreground = white (255)
# Background = black (0)
_, binary = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)

# Create a structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated_image = cv2.dilate(
    binary,
    kernel,
    iterations=1
)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Binary Image", binary)
cv2.imshow("Dilated Image", dilated_image)

# Save the output image
cv2.imwrite("dilated_output.jpg", dilated_image)

print("Dilation operation completed successfully!")
print("Output saved as dilated_output.jpg")

# Wait for a key press
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()