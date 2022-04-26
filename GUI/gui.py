from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from playsound import playsound
import os.path
from functools import partial
from GMM import recognize
from GMM import features

global selected_model_path
global model_loaded
global wav_path

IMAGE_DIR = "images"


def browseFiles():
    wav_path = filedialog.askopenfilename(title=u'Choose file')
    label_file_explorer.configure(text="File Opened: " + wav_path)
    return wav_path

def play():
    playsound(wav_path)

def Inference(label_prediction):
    image2 = Image.open(os.path.join(IMAGE_DIR, "LOL.png"))
    image_res2 = image2.resize((150, 150), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(image_res2)
    label_prediction.configure(text="Prediction = ?")
    label_image2 = Label(window,
                        image=photo2, height=200)
    label_image2.image = photo2
    label_image2.grid(column=0, row=2, columnspan=3, rowspan=2, pady=(0.0))

def ModelSelection():
    selected_model_path = filedialog.askopenfilename(title=u'Choose file')
    model_loaded = recognize.load_model(selected_model_path)
    # image2 = Image.open(os.path.join(IMAGE_DIR, "gmm.png"))
    # image_res2 = image2.resize((150, 150), Image.ANTIALIAS)
    # photo4 = ImageTk.PhotoImage(image_res2)
    # label_image2 = Label(window,
    #                      image=photo4, height=200)
    # label_image2.image = photo4
    # label_image2.grid(column=0, row=2, columnspan=2, rowspan=2, pady=(0.0))
    





def PredictFunc(label_prediction, model, path):
    try:
        fs, signal = features.read_wav(path)
    except Exception:
        label_prediction.configure(text="Read {} failed.".format(path))
        return
    pred_res = model.predict(fs, signal)
    image3 = Image.open(os.path.join(IMAGE_DIR, pred_res, ".png"))
    image_res2 = image3.resize((150, 150), Image.ANTIALIAS)
    photo3 = ImageTk.PhotoImage(image_res2)
    label_prediction.configure(text="Prediction = {}".format(pred_res))
    label_image3 = Label(window,
                        image=photo3, height=150)
    label_image3.image = photo3
    label_image3.grid(column=1, row=2, columnspan=2, rowspan=2, pady=(0.0))

def TKWindow():
    global label_file_explorer
    window = Tk()

    window.title('League of Legends Character Audio Recognition Based on Gaussian Mixture Model')
    window.resizable(width=False, height=False)
    window.geometry("750x500")



    image1 = Image.open(os.path.join(IMAGE_DIR, "LOL.png"))
    image_res1 = image1.resize((150, 150), Image.ANTIALIAS)
    photo1 = ImageTk.PhotoImage(image_res1)

    label_file_explorer = Label(window,
                                text="Choose a .wav file to be analyzed!",
                                width=30, height=5,
                                font=('Helvetica', '15')
                                )
    label_file_explorer.config(fg="blue")

    label_prediction = Label(window,
                             text="Prediction:",
                             width=50, height=5,
                             font=('Helvetica', '15')
                             )
    label_prediction .config(fg="blue")

    button_explore = Button(window,
                            text="Browse Files",
                            command=browseFiles,
                            width=18, height=3)


    button_play = Button(window,
                         text="Play",
                         command=play,
                         width=18, height=3)

    # button_test_command = partial(modeltext, label_prediction)
    button_test = Button(window,
                         text="Model selection",
                         command=ModelSelection,
                         width=18, height=3)

    button_test2_command = partial(PredictFunc, label_prediction, model_loaded, wav_path)
    button_test2 = Button(window,
                          text="Prediction",
                          command=button_test2_command,
                          width=18, height=3)

    label_image = Label(window,
                        image=photo1, height=200)
    label_image.image = photo1


    canva=Label(window,
                 text="Hero image",
              font = ('Helvetica', '12')
                                           )
    canva.config(fg="brown")
    label_file_explorer.grid(column=0, row=0, columnspan=3)
    label_prediction.grid(column=0, row=1, columnspan=3)
    label_image.grid(column=0, row=2, columnspan=2, rowspan=2, pady=(0.0))

    button_explore.grid(column=3, row=0, padx=(0, 0))
    button_play.grid(column=3, row=1, padx=(0, 0))
    button_test.grid(column=3, row=2, padx=(0, 0))
    button_test2.grid(column=3, row=3, padx=(0, 0))
    canva.grid(column=1, row=2, columnspan=2, rowspan=2, pady=(0.0))
    return window

if __name__ == '__main__':
    window = TKWindow()
    window.mainloop()
