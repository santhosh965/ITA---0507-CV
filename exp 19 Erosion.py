import cv2
import numpy as np

# -----------------------------------------
# Erosion Morphological Operation
# -----------------------------------------

# Read the input image
image = cv2.imread("sample2.png")

# Check if image is loaded
if image is None:
    print("Error: Could not load the image!")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert image to binary
# Objects become white and background becomes black
_, binary = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)

# Create a structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded_image = cv2.erode(
    binary,
    kernel,
    iterations=1
)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Binary Image", binary)
cv2.imshow("Eroded Image", eroded_image)

# Save the result
cv2.imwrite("eroded_output.jpg", eroded_image)

print("Erosion operation completed successfully!")
print("Output saved as eroded_output.jpg")

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()