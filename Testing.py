# make new directory named "Model"
# paste the 2 files downloaded
# testing file is modified file of data collection file
# remove key part of saving
# install pakage tensorflow
# (machine learning framework by google,pretty big like mediapipe )
# 2.9.1 version did by sir
# little delay first time run
# in output : [3 confident values,last one maybe responsible for final prediction] prediction
# now we dont want to show backend remove skeleton by removing draw
# or draw=False at detector.findHands(),it will remove for all
# but we also need drawings for other 2 boxes
# use img.copy() and use it as output
# predictions will be wrong if we give image not image white
# then play with customizations
# ;0 DONE



# Import necessary libraries

import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier  # send images to model and it will classify it
import numpy as np
import math

# Initialize the camera capture
cap = cv2.VideoCapture(0)

# Initialize hand detector to track one hand
detector = HandDetector(maxHands=1)

# Initialize the classifier model for hand gesture recognition
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

# Define some constants
offset = 20           # Offset for cropping the hand region
imgSize = 300          # Size of the image for classification
folder = "Data/C"      # Folder where data is stored
counter = 0            # Counter for something (not used in the code)
labels = ["A", "B", "C"]  # Labels for gesture classification

# Main loop for capturing and processing frames
while True:
    # Read a frame from the camera
    success, img = cap.read()

    # Create a copy of the image for displaying the output
    imgOutput = img.copy()

    # Detect hands in the frame
    hands, img = detector.findHands(img)

    # If hands are detected
    if hands:
        hand = hands[0]  # Consider only the first detected hand

        # Extract the bounding box coordinates of the hand
        x, y, w, h = hand['bbox']

        # Create a white image of a fixed size (imgSize x imgSize)
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

        # Crop the hand region with an offset
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        # Get the shape of the cropped hand image
        imgCropShape = imgCrop.shape

        # Calculate the aspect ratio of the hand
        aspectRatio = h / w

        # If the aspect ratio is greater than 1, it means the hand is tall
        if aspectRatio > 1:
            k = imgSize / h  # Calculate the scaling factor

            # Calculate the width of the resized image while maintaining the aspect ratio
            wCal = math.ceil(k * w)

            # Resize the cropped hand image to the calculated width
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))

            # Get the shape of the resized image
            imgResizeShape = imgResize.shape

            # Calculate the gap to center the resized image horizontally
            wGap = math.ceil((imgSize - wCal) / 2)

            # Place the resized image onto the white canvas
            imgWhite[:, wGap:wCal + wGap] = imgResize

            # Get a prediction for the hand gesture and index
            prediction, index = classifier.getPrediction(imgWhite, draw=False)

            # Print the prediction and its index
            print(prediction, index)
        else:
            k = imgSize / w  # Calculate the scaling factor

            # Calculate the height of the resized image while maintaining the aspect ratio
            hCal = math.ceil(k * h)

            # Resize the cropped hand image to the calculated height
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))

            # Get the shape of the resized image
            imgResizeShape = imgResize.shape

            # Calculate the gap to center the resized image vertically
            hGap = math.ceil((imgSize - hCal) / 2)

            # Place the resized image onto the white canvas
            imgWhite[hGap:hCal + hGap, :] = imgResize

            # Get a prediction for the hand gesture
            prediction, index = classifier.getPrediction(imgWhite, draw=False)

        # Draw rectangles
        # and Draw labels on the output image
        # and its ABOVE OUR HAND !!!!!
        # offsets and other properties swaad anusaar
        cv2.rectangle(imgOutput, (x - offset, y - offset - 50), (x - offset + 90, y - offset - 50 + 50), (255, 0, 255),
                      cv2.FILLED)
        cv2.putText(imgOutput, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
        cv2.rectangle(imgOutput, (x - offset, y - offset), (x + w + offset, y + h + offset), (255, 0, 255), 4)

    # Display the cropped hand image, the white canvas, and the output image
    cv2.imshow("ImageCrop", imgCrop)
    cv2.imshow("ImageWhite", imgWhite)
    cv2.imshow("Image", imgOutput)

    # Wait for a key press and exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()