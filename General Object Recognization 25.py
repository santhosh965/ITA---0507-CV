import cv2

# -----------------------------------------
# Watch Recognition using OpenCV
# -----------------------------------------

# Load the input image
image = cv2.imread("sample7.png")

# Check if image loaded
if image is None:
    print("Error: Could not load sample7.png")
    print("Make sure sample7.png is in the same folder as this Python file.")
    exit()

print("Image loaded successfully!")

# Make a copy of the original image
display_image = image.copy()

# -----------------------------------------
# Select the watch using mouse
# -----------------------------------------

print("Select the WATCH using your mouse.")
print("Drag a rectangle around the watch.")
print("Press ENTER after selecting.")

roi = cv2.selectROI(
    "Select Watch",
    display_image,
    False,
    False
)

# Get coordinates
x, y, w, h = roi

# Check if selection was made
if w == 0 or h == 0:
    print("No watch selected!")
    cv2.destroyAllWindows()
    exit()

# -----------------------------------------
# Draw rectangle around watch
# -----------------------------------------

cv2.rectangle(
    image,
    (x, y),
    (x + w, y + h),
    (0, 255, 0),
    3
)

# Add label
cv2.putText(
    image,
    "WATCH",
    (x, y - 10),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 255, 0),
    2
)

# -----------------------------------------
# Crop the detected watch
# -----------------------------------------

watch = image[y:y+h, x:x+w]

# Display results
cv2.imshow("Watch Recognition", image)
cv2.imshow("Detected Watch", watch)

# Save results
cv2.imwrite("watch_result.jpg", image)
cv2.imwrite("detected_watch.jpg", watch)

print("Watch recognized successfully!")
print("Result saved as watch_result.jpg")
print("Detected watch saved as detected_watch.jpg")

# Wait for key
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()