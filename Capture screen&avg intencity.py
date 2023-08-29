import numpy as np
import cv2
from mss import mss
# from PIL import Image

bounding_box = {'top': 400, 'left': 800, 'width': 400, 'height': 300}

sct = mss()

# Initialize the list of average intensity values
average_intensities = []

while True:
    sct_img = sct.grab(bounding_box)

    # Convert the image to a numpy array
    image_array = np.array(sct_img)

    # Calculate the average intensity value for the image
    average_intensity = np.mean(image_array)

    # Add the average intensity value to the list
    average_intensities.append(average_intensity)

    cv2.imshow('screen', np.array(sct_img))

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()

        # Output the average intensity
        # Define the folder path and file name
        folder_path = "/Users/User/Desktop/Lab17/Git_Projects"
        file_name = "signal.dat"

        # Save the array to a .dat file
        file_path = folder_path + "/" + file_name
        np.savetxt(file_path, average_intensities)

        break