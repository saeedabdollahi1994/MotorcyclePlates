import tkinter as tk
from gui_app import MyGUI

def main():
    root = tk.Tk()
    app = MyGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()