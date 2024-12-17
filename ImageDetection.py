import os
from PlateNumbers import Plate
import cv2
from ultralytics import YOLO
from tkinter import filedialog, Label, Button, Text,Scrollbar, Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

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
            results_num = model_nums(plates[i],conf=0.75)
            result = myplate.numbers_detection(results_num)
            print(result[0]+result[1])
            output = str(result[0])+"//"+str(result[1])
            image = cv2.putText(image, output,(50*i+50,50*i+50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            result.clear

        return image_rgb    