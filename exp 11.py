import cv2

# Read the image
image = cv2.imread("sample3.png")

# Check if the image is loaded successfully
if image is None:
    print("Error: Image not found!")
    exit()

# Rotate the image 180 degrees
rotated_image = cv2.rotate(image, cv2.ROTATE_180)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("180 Degree Rotated Image", rotated_image)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()