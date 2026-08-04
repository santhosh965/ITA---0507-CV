import cv2
import numpy as np

# Read the image
image = cv2.imread("sample1.png")

# Check if image is loaded successfully
if image is None:
    print("Error: Image not found!")
    exit()

# Create a kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Dilate the image
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Display original and dilated images
cv2.imshow("Original Image", image)
cv2.imshow("Dilated Image", dilated_image)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()