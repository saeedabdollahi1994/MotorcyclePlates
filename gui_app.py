import tkinter as tk
from tkinter import filedialog, Label, Button, Text,Scrollbar, Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from VideoDetection import VideoDetect
from ImageDetection import ImageDetect
from PIL import Image, ImageTk


class MyGUI():
    def __init__(self,root):
        self.root = root
        self.root.title("My Tkinter App")
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
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.MOV;*.MP4")])
        if file_path:
            imgclass = ImageDetect(file_path)
            image = imgclass.image_detection()
            pil_image = Image.fromarray(image)
            tk_image = ImageTk.PhotoImage(pil_image)
            self.image_frame.config(image=tk_image)
            self.image_frame.image = tk_image

        else:
            pass    
'''
    def show_image(self,image_frame):
    # Clear previous plot
       # for widget in image_frame.winfo_children():
        #    widget.destroy()

    # Display image
        fig, ax = plt.subplots(figsize=(20, 15))
        ax.imshow(image_frame)
        ax.set_title("Uploaded Image")
        ax.axis("off")

    # Embed plot into Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=image_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

'''