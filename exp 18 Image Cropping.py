import cv2

# Load the image
image = cv2.imread("sample3.png")

# Check if image is loaded
if image is None:
    print("Error: Could not load the image.")
    exit()

# Get image dimensions
height, width = image.shape[:2]

print("Image size:", width, "x", height)

# --------------------------------
# Define ROI coordinates
# --------------------------------

# Change these values according to your image
x1 = 50
y1 = 50
x2 = 200
y2 = 200

# Make sure coordinates are inside the image
if x2 > width or y2 > height:
    print("Error: ROI coordinates are larger than the image.")
    print("Image size:", width, "x", height)
    exit()

# --------------------------------
# Crop the ROI
# --------------------------------

roi = image[y1:y2, x1:x2]

# Display cropped ROI
cv2.imshow("Cropped ROI", roi)

# --------------------------------
# Copy the ROI
# --------------------------------

roi_copy = roi.copy()

# --------------------------------
# Paste the ROI
# --------------------------------

# Paste at top-left corner
paste_x = 10
paste_y = 10

roi_height, roi_width = roi_copy.shape[:2]

# Check whether ROI fits
if (paste_x + roi_width <= width and
        paste_y + roi_height <= height):

    image[
        paste_y:paste_y + roi_height,
        paste_x:paste_x + roi_width
    ] = roi_copy

    print("ROI copied and pasted successfully!")

else:
    print("Error: ROI cannot fit at the paste position.")
    exit()

# --------------------------------
# Show final result
# --------------------------------

cv2.imshow("Original Image", cv2.imread("sample3.png"))
cv2.imshow("ROI Copy Paste Result", image)

# Save result
cv2.imwrite("roi_result.jpg", image)

print("Result saved as roi_result.jpg")

# Wait for key
cv2.waitKey(0)
cv2.destroyAllWindows()