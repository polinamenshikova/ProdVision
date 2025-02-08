"""

This script is designed for object tracking and counting in a production line setting.
It utilizes computer vision techniques to detect and monitor items without the need
for a pre-trained dataset, thereby saving time and computational resources.

Key Features:
- Utilizes OpenCV for image processing
- Tracks objects using bounding boxes
- Eliminates the need for dataset training

"""

import cv2
import numpy as np

# Initialize video capture
cap = cv2.VideoCapture('production_line.mp4')

# Parameters for object detection
min_contour_area = 500  # Minimum contour area to consider
line_position = 400     # Position of the counting line

# Variables for counting
object_count = 0
previous_centers = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale and apply Gaussian blur
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform background subtraction
    fg_mask = cv2.createBackgroundSubtractorMOG2().apply(blurred)

    # Apply threshold to get binary image
    _, thresh = cv2.threshold(fg_mask, 127, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    current_centers = []

    for contour in contours:
        if cv2.contourArea(contour) > min_contour_area:
            # Get bounding box from contour
            x, y, w, h = cv2.boundingRect(contour)
            center = (int(x + w / 2), int(y + h / 2))
            current_centers.append(center)

            # Draw bounding box and center point
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

            # Check if object has crossed the counting line
            if center[1] > line_position and center not in previous_centers:
                object_count += 1

    # Draw counting line
    cv2.line(frame, (0, line_position), (frame.shape[1], line_position), (255, 0, 0), 2)

    # Display count on frame
    cv2.putText(frame, f'Count: {object_count}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Show the frame
    cv2.imshow('Frame', frame)

    # Update previous centers
    previous_centers = current_centers.copy()

    # Exit on 'q' key press
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
