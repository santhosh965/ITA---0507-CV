import cv2
import numpy as np

# Read the image
image = cv2.imread("sample5.png")

# Check if the image is loaded successfully
if image is None:
    print("Error: Image not found!")
    exit()

# Get image dimensions
rows, cols = image.shape[:2]

# Define four points in the original image
pts1 = np.float32([
    [50, 50],
    [cols - 50, 50],
    [50, rows - 50],
    [cols - 50, rows - 50]
])

# Define four corresponding points in the transformed image
pts2 = np.float32([
    [0, 0],
    [cols, 50],
    [50, rows],
    [cols, rows]
])

# Compute the Perspective Transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply the Perspective Transformation
perspective_image = cv2.warpPerspective(image, matrix, (cols, rows))

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformed Image", perspective_image)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()