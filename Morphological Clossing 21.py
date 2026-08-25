import cv2
import numpy as np

# -----------------------------------------
# Morphological Closing using OpenCV
# Closing = Dilation followed by Erosion
# -----------------------------------------

# Read the input image
image = cv2.imread("sample4.png")

# Check if image was loaded successfully
if image is None:
    print("Error: Could not load the image!")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert grayscale image to binary
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

# -----------------------------------------
# Apply Morphological Closing
# -----------------------------------------

# Closing = Dilation followed by Erosion
closing = cv2.morphologyEx(
    binary,
    cv2.MORPH_CLOSE,
    kernel
)

# -----------------------------------------
# Display the results
# -----------------------------------------

cv2.imshow("Original Image", image)
cv2.imshow("Binary Image", binary)
cv2.imshow("Closing Result", closing)

# Save the output image
cv2.imwrite("closing_output.jpg", closing)

print("Morphological Closing completed successfully!")
print("Output saved as closing_output.jpg")

# Wait for a key press
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()