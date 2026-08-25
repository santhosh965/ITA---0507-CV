import cv2
import numpy as np

# -----------------------------------------
# Morphological Black Hat Operation
# Black Hat = Closing - Original Image
# -----------------------------------------

# Load the image
image = cv2.imread(
    r"C:\Users\Shivaji V\Downloads\santhosh cv\sample4.png"
)

# Check if image was loaded successfully
if image is None:
    print("Error: Could not load the image!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# -----------------------------------------
# Apply Morphological Black Hat
# -----------------------------------------

black_hat = cv2.morphologyEx(
    gray,
    cv2.MORPH_BLACKHAT,
    kernel
)

# -----------------------------------------
# Display the results
# -----------------------------------------

cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Black Hat Result", black_hat)

# Save the output
cv2.imwrite("black_hat_output.jpg", black_hat)

print("Black Hat operation completed successfully!")
print("Output saved as black_hat_output.jpg")

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()