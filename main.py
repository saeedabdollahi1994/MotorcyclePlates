import os
from PlateNumbers import Plate
import cv2
from ultralytics import YOLO


path = "E:/Datasets/Iran_motorcycle_plate.v1i.yolov8/test/images/"
for item in os.listdir(path):
    myplate = Plate(path+item)
    plates,locations = myplate.plate_detection()
    image = cv2.imread(path+item)
    image = cv2.resize(image, (640,640))
    for i in range(len(plates)):
        model_nums = YOLO("YOLO/best_nums_weights.pt")
        results_num = model_nums(plates[i],conf=0.75)
        result = myplate.numbers_detection(results_num)
        print(item,"Plate Numbers:",result[0],"\n",result[1])
        image = cv2.putText(image, str(result[0]+result[1]),(50*i+50,50*i+50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)
        result.clear
    file_name = f'test_result_{item}'
    full_path = os.path.join("testres", file_name)
    cv2.imwrite(full_path, image)
    
        

