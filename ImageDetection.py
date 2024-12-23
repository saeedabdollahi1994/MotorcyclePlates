import os
from PlateNumbers import Plate
import cv2
from ultralytics import YOLO


class ImageDetect():
    def __init__(self,image):
       self.image = image
       
    
    def image_detection(self): 
        image = self.image
        image = cv2.imread(image)
        myplate = Plate(image)
        plates,locations = myplate.plate_detection()
        image = cv2.resize(image, (640,640))
        for i in range(len(plates)):
            model_nums = YOLO("YOLO/best_nums_weights.pt")
            confidence = 0.80
            results_num = model_nums(plates[i],conf=confidence)
            if(len(results_num[0].boxes) == 8): 
                result = myplate.numbers_detection(results_num)
                print(result[0]+result[1])
                output = str(result[0])+"//"+str(result[1])
                image = cv2.putText(image, output,(50*i+50,50*i+50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)
                image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                result.clear
            elif(len(results_num[0].boxes) > 8):
                i = i - 1
                confidence = 0.86
                results_num = model_nums(plates[i],conf=confidence)
                result = myplate.numbers_detection(results_num)
                print(result[0]+result[1])
                output = str(result[0])+"//"+str(result[1])
                image = cv2.putText(image, output,(50*i+50,50*i+50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)
                image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                result.clear
            else:
                i = i - 1
                confidence = 0.65
                results_num = model_nums(plates[i],conf=confidence)
                result = myplate.numbers_detection(results_num)
                print(result[0]+result[1])
                output = str(result[0])+"//"+str(result[1])
                image = cv2.putText(image, output,(50*i+50,50*i+50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)
                image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                result.clear

        return image_rgb    