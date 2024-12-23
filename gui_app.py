import tkinter as tk
from tkinter import filedialog, Label, Button, Text,Scrollbar, Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from VideoDetection import VideoDetect
from ImageDetection import ImageDetect
from PIL import Image, ImageTk
import imageio.v3 as iio
import cv2

class MyGUI():
    def __init__(self,root):
        self.root = root
        self.root.title("تشخیص پلاک موتورسیکلت")
        self.root.geometry("1200x950")
        self.root.configure(bg="lightgrey")
        self.upload_button = Button(root, text="Upload Image", command=self.upload_file, bg="lightblue", fg="black")
        self.upload_button.pack(pady=10)
        self.image_frame = Label(root, bg="white", width=640, height=640)
        self.image_frame.pack(pady=10)
        self.plates_label = Label(root, text="Plates:", font=("Arial", 12), bg="lightgrey")
        self.plates_label.pack(pady=5)
        self.text_box = Text(root, height=2, width=60)
        self.text_box.pack(pady=5)
       
        



    def upload_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Image or Video File",
            filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp"),
                       ("Video files", "*.mp4;*.avi;*.mov;*.mkv")])
           
        if file_path:
            if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                imgobject = ImageDetect(file_path)
                image = imgobject.image_detection()
                cv2.imshow("پلاک", image)
                pil_image = Image.fromarray(image)
                tk_image = ImageTk.PhotoImage(pil_image)
                self.image_frame.config(image=tk_image)
                self.image_frame.image = tk_image
            elif file_path.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
                cap = cv2.VideoCapture(file_path)
                if not cap.isOpened():
                    print("Error: Cannot open video file.")
                    exit()
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    vid_object = VideoDetect(frame)
                    frame = vid_object.frame_detection()
                    cv2.imshow("Video with Text", frame)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                            break
        
                cap.release()
                cv2.destroyAllWindows()   
        else:
            Text.showerror("Error", "Unsupported file format!")

