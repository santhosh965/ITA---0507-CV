import cv2
import numpy as np

# -----------------------------------------
# Morphological Opening using OpenCV
# Opening = Erosion followed by Dilation
# -----------------------------------------

# Read the input image
image = cv2.imread("sample4.png")

# Check if image was loaded
if image is None:
    print("Error: Could not load the image!")
    exit()

# Convert image to grayscale
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

# Create structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# -----------------------------------------
# Apply Morphological Opening
# -----------------------------------------

# Opening = Erosion + Dilation
opening = cv2.morphologyEx(
    binary,
    cv2.MORPH_OPEN,
    kernel
)

# -----------------------------------------
# Display the results
# -----------------------------------------

cv2.imshow("Original Image", image)
cv2.imshow("Binary Image", binary)
cv2.imshow("Opening Result", opening)

# Save the output
cv2.imwrite("opening_output.jpg", opening)

print("Morphological Opening completed successfully!")
print("Output saved as opening_output.jpg")

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()