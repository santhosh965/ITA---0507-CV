import cv2

# Read the image
image = cv2.imread("sample2.png")

# Check if the image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Resize the image to a bigger size (2 times)
bigger_image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Resize the image to a smaller size (0.5 times)
smaller_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Bigger Image", bigger_image)
cv2.imshow("Smaller Image", smaller_image)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()