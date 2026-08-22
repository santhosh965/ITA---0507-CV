import cv2
import numpy as np
# Read the image
image = cv2.imread("sample1.png")
# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load image.")
else:
    # Create a 5x5 kernel
    kernel = np.ones((5, 5), np.uint8)
    # Apply erosion
    eroded_image = cv2.erode(image, kernel, iterations=1)
    # Display the original and eroded images
    cv2.imshow("Original Image", image)
    cv2.imshow("Eroded Image", eroded_image)
    # Wait until a key is pressed
    cv2.waitKey(0)
    # Close all windows
    cv2.destroyAllWindows()
