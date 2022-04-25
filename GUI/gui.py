from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from playsound import playsound
import os.path
from functools import partial


openedfile = 0

IMAGE_DIR = "images"

def browseFiles(label_file_explorer):
    global openedfile
    global file_text
    file_path = filedialog.askopenfilename(title=u'Choose file')
    label_file_explorer.configure(text="File Opened: "+file_path)
    return file_path

def play(file_path):
    playsound(file_path)

def Inference(label_prediction):

    image2 = Image.open(os.path.join(IMAGE_DIR, "AATROX.png"))
    image_res2 = image2.resize((400, 300), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(image_res2)
    label_prediction.configure(text="Prediction=AATROX")
    label_image2 = Label(window,
                        image=photo2, height=200)
    label_image2.image = photo2
    label_image2.grid(column=0, row=2, columnspan=3, rowspan=2, pady=(0.0))

def Inference2(label_prediction):
    image3 = Image.open(os.path.join(IMAGE_DIR, "AATROX.png"))
    image_res2 = image3.resize((400, 300), Image.ANTIALIAS)
    photo3 = ImageTk.PhotoImage(image_res2)
    label_prediction.configure(text="Prediction=LUCIAN")
    label_image3 = Label(window,
                        image=photo3, height=200)
    label_image3.image = photo3
    label_image3.grid(column=0, row=2, columnspan=3, rowspan=2, pady=(0.0))

def TKWindow():
    window = Tk()

    window.title('League of Legends Character Audio Recognition Based on Gaussian Mixture Model')

    window.geometry("700x500")

    window.config(background="white")
    window.resizable(False, False)

    image1 = Image.open(os.path.join(IMAGE_DIR, "AATROX.png"))
    image_res1 = image1.resize((400, 300), Image.ANTIALIAS)
    photo1 = ImageTk.PhotoImage(image_res1)

    label_file_explorer = Label(window,
                                text="Choose a .wav file to be analyzed!",
                                width=75, height=6,
                                fg="blue")

    label_prediction = Label(window,
                             text="Prediction:",
                             width=75, height=6,
                             fg="blue")

    button_explore_command = partial(browseFiles, label_file_explorer)
    file_path = browseFiles(label_file_explorer)

    button_explore = Button(window,
                            text="Browse Files",
                            command=button_explore_command,
                            width=25, height=6)

    button_play_command = partial(play, file_path)
    button_play = Button(window,
                         text="Play",
                         command=button_play_command,
                         width=25, height=6)

    button_test_command = partial(Inference, label_prediction)
    button_test = Button(window,
                         text="Prediction",
                         command=button_test_command,
                         width=25, height=6)

    button_test2_command = partial(Inference2, label_prediction)
    button_test2 = Button(window,
                          text="Prediction",
                          command=button_test2_command,
                          width=25, height=6)

    label_image = Label(window,
                        image=photo1, height=200)
    label_image.image = photo1

    label_file_explorer.grid(column=0, row=0, columnspan=3)
    label_prediction.grid(column=0, row=1, columnspan=3)
    label_image.grid(column=0, row=2, columnspan=3, rowspan=2, pady=(0.0))
    button_explore.grid(column=3, row=0, padx=(0, 0))
    button_play.grid(column=3, row=1, padx=(0, 0))
    button_test.grid(column=3, row=2, padx=(0, 0))
    button_test2.grid(column=3, row=3, padx=(0, 0))
    return window

if __name__ == '__main__':
    window = TKWindow()
    window.mainloop()
