import numpy as np
import cv2
from mss import mss
# from PIL import Image

bounding_box = {'top': 400, 'left': 800, 'width': 400, 'height': 300}
sct = mss()
average_intensities = [] # Initialize the list of average intensity values
frame_count = 0 # Set the frame count to 0

while True:
    sct_img = sct.grab(bounding_box)
    cv2.imshow('screen', np.array(sct_img))

    frame_count += 1 # Increment the frame count

    if frame_count % 60 == 0: # If this is the 60th frame, take a screenshot
        image_array = np.array(sct_img)  # Convert the image to a numpy array
        average_intensity = np.mean(image_array)  # Calculate the average intensity value for the image
        average_intensities.append(average_intensity)  # Add the average intensity value to the list

        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            cv2.destroyAllWindows()
            folder_path = "/Users/User/Desktop/Lab17/Git_Projects" # Output the average intensity
            file_name = "signal.dat" # Define the folder path and file name
            file_path = folder_path + "/" + file_name
            np.savetxt(file_path, average_intensities) # Save the array to a .dat file

            break
