import os
import json
import cv2
from background_segmentation import background_segmentation


if __name__ == '__main__':
    #setting up parameters
    #choose learning rate and threshold values manually.
    testFile = "C:/Users/priyanka/Downloads/26_02_2022_group10_assignment1/param.json"
    video_path = cv2.VideoCapture(r"C:\Users\priyanka\Downloads\26_02_2022_group10_assignment1\umcp.mpg")

    if os.path.exists(testFile):
        with open(testFile, 'r') as f:
            jsonObj = json.load(f)
        alpha= jsonObj["learning_rate"]
        T = jsonObj["threshold"]

    object1=background_segmentation(video_path,alpha,T)
    object1.update_parameter()

