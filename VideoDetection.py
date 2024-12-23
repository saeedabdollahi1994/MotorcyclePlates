import os
from PlateNumbers import Plate
import cv2
from ultralytics import YOLO
from ImageDetection import ImageDetect
from PIL import Image, ImageTk

class VideoDetect():
    def __init__(self,frame):
        self.frame = frame
        

    def frame_detection(self): 
        frame = self.frame
        myplate = Plate(frame)
        plates,locations = myplate.plate_detection()
        frame = cv2.resize(frame, (640,640))
        if frame is None:
            print("Error: Frame is empty or invalid.")
            return None, None  # Handle the error gracefully
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        for i in range(len(plates)):
            model_nums = YOLO("YOLO/best_nums_weights.pt")
            confidence = 0.80
            results_num = model_nums(plates[i],conf=confidence)
            if(len(results_num[0].boxes) == 8): 
                result = myplate.numbers_detection(results_num)
                print(result[0]+result[1])
                output = str(result[0])+"//"+str(result[1])
                frame = cv2.putText(frame, output,(50*i+50,50*i+50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)
                image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                result.clear
            elif(len(results_num[0].boxes) > 8):
                i = i - 1
                confidence = 0.86
                results_num = model_nums(plates[i],conf=confidence)
                result = myplate.numbers_detection(results_num)
                print(result[0]+result[1])
                output = str(result[0])+"//"+str(result[1])
                frame = cv2.putText(frame, output,(50*i+50,50*i+50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)
                image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                result.clear
            else:
                i = i - 1
                confidence = 0.74
                results_num = model_nums(plates[i],conf=confidence)
                result = myplate.numbers_detection(results_num)
                print(result[0]+result[1])
                output = str(result[0])+"//"+str(result[1])
                frame = cv2.putText(frame, output,(50*i+50,50*i+50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)
                image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                result.clear    
        return  frame
        
            



    
                    