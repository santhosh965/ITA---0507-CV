import cv2
import numpy as np

# Read the image
image = cv2.imread("sample4.png")

# Check if the image is loaded successfully
if image is None:
    print("Error: Image not found!")
    exit()

# Get image dimensions
rows, cols = image.shape[:2]

# Select three points from the original image
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

# Select corresponding points in the transformed image
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Compute the Affine Transformation matrix
matrix = cv2.getAffineTransform(pts1, pts2)

# Apply the Affine Transformation
affine_image = cv2.warpAffine(image, matrix, (cols, rows))

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformed Image", affine_image)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()