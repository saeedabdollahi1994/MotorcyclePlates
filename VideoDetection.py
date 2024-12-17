import os
from PlateNumbers import Plate
import cv2
from ultralytics import YOLO

class VideoDetect():
    def __init__(self,video):
        self.video = video

    def video_detection(path):
    
        cap = cv2.VideoCapture(path)
        if not cap.isOpened():
            print("Error: Cannot open video file.")
            exit()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break    
            myplate = Plate(frame)
            if myplate:
                plates,locations = myplate.plate_detection()
                #image = cv2.resize(image, (640,640))
                for i in range(len(plates)):
                    model_nums = YOLO("YOLO/best_nums_weights.pt")
                    results_num = model_nums(plates[i],conf=0.75)
                    result = myplate.numbers_detection(results_num)
                    print(result[0]+result[1])
                    frame = cv2.putText(frame, str(result[0]+result[1]),(50*i+50,50*i+50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)
                    show_image(frame)
                    result.clear
            if myplate is None:
                show_image(frame)
