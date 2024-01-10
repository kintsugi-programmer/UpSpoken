# NOTES WITH CODE
# https://youtu.be/wa2ARoUUdU8?feature=shared
# C:\Users\balie\PycharmProjects\Upspoken
# 3classes a,b,c
# detect>classify
# 1.data collection part>to train
# 2.testing part
# ASL Generally
# problems crop the image to hand size in square
# ad problem is to crop all selectable part and fill bg to make it square
# why ? to send data in classifier its necessary to have same size
# even if error of one pixel => error
# Data/A & B & C
# 2 .py programs dataCollection and test
# install mediapipe and opencv at file>setting>project>python interpreter>add them >ok
# basic code
# we need skeleton to make classifier classify things,so we are not removing it
# fill the gap with white but enlarge the picture as big as possible : 2 cases of height and width FIT AND FILL THE SCREEN
# and it would be more good if image is at centre
# DUE TO CONSTRAINT ENVIRONMENT DON'T GO TOO FAR,NOT COME TOO NEAR
# "s" button to capture images
# ta daaaaaaaa : 300x300 pixels

import cv2  # for using webcam
from cvzone.HandTrackingModule import HandDetector  # for croping
import numpy as np
import math  # ceil is gif func i think
import time

# Initialize the webcam feed
cap = cv2.VideoCapture(0)  # 0 is id no. of webcam

# Initialize the HandDetector object for detecting hands (using a library called cvzone) and we will use to crop it
detector = HandDetector(maxHands=1)  # maxhands is 1

# Define offset and image size constants
offset = 20  # The amount of extra space to include when cropping around the hand
imgSize = 300  # The size of the final captured image

# Folder to save captured images
# TO BE CHANGED AT DIFFERENT SIGNS
folder = "Data/C"

# Counter to keep track of the number of images captured
counter = 0

while True:
    # Read a frame from the webcam feed
    success, img = cap.read()

    # Detect hands in the frame using the HandDetector
    hands, img = detector.findHands(img)

    if hands:
        # Take the first detected hand (assuming only one hand is detected)
        # here 0 is only one hand
        hand = hands[0]

        # Extract the bounding box coordinates of the hand
        # bbox is bounding box
        x, y, w, h = hand['bbox']

        # Create a white canvas of the specified image size
        # here we make first a white background square image for uniform data image size
        # we can make it from matix usng numpy
        # matrix of once np.oce
        # imgSize = 300,so 300x300 square
        # ,3 for coloured image
        # datatype is 8bit values of image colours i.e. 0,255
        # so np.vint8 mens numpy of unsigned integer of 8 bits
        # * 255,because colour range is 0 to 255 and if pixel values are 1 so output will be just black
        # now whatever we do imgwhite is gonna white another window
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

        # Crop the hand region from the frame with an offset
        # starting ht,end,starting witdh,end
        # earlier it was imgCrop = img[y:y + h, x:x + w]
        # but due to it newbox(3rd in my system) made till skeleton tip,not my tip
        # so to perfection this we used offset
        # that's why offset = 20 value is given
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        # Get the shape and aspect ratio of the cropped region
        imgCropShape = imgCrop.shape
        aspectRatio = h / w

        if aspectRatio > 1:
            # If the aspect ratio is greater than 1 (taller than wide)
            # Resize the hand image keeping height constant
            k = imgSize / h
            wCal = math.ceil(k * w)  # Calculate the width after resizing
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)  # Calculate the gap to center the image
            imgWhite[:, wGap:wCal + wGap] = imgResize  # Place the resized image on the canvas
        else:
            # If the aspect ratio is less than or equal to 1 (wider than tall)
            # Resize the hand image keeping width constant
            k = imgSize / w
            hCal = math.ceil(k * h)  # Calculate the height after resizing
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)  # Calculate the gap to center the image
            imgWhite[hGap:hCal + hGap, :] = imgResize  # Place the resized image on the canvas

        # Display the cropped hand image and the combined image with white canvas
        # display used variables and methods
        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    # Display the original frame with detected hands
    cv2.imshow("Image", img)

    # Wait for user input (press 's' key) to capture and save the image
    # BURST SHOT or single
    key = cv2.waitKey(1)
    if key == ord("s"):
        counter += 1
        # Save the image with a timestamp as the filename in the specified folder
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgWhite)
        print(counter)