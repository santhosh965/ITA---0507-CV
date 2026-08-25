import cv2
import numpy as np

# Load the image
image = cv2.imread(
    r"C:\Users\Shivaji V\Downloads\santhosh cv\sample4.png"
)

# Check if image was loaded
if image is None:
    print("Error: Could not load the image!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Apply Top Hat operation
top_hat = cv2.morphologyEx(
    gray,
    cv2.MORPH_TOPHAT,
    kernel
)

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("Top Hat Result", top_hat)

# Save output
cv2.imwrite("top_hat_output.jpg", top_hat)

print("Top Hat operation completed successfully!")
print("Output saved as top_hat_output.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()