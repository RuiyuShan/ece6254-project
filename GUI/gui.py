from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from playsound import playsound
import os.path
from functools import partial
from GMM import recognize
from GMM import features

wav_path = ''
model_list = []

IMAGE_DIR = "images"


def BrowseFile():
    global wav_path
    wav_path = filedialog.askopenfilename(title=u'Choose file')
    print(wav_path)
    label_file_explorer.configure(text="File Opened: " + str.join('/', wav_path.split('/')[-2:]))
    print(os.path.join(IMAGE_DIR, wav_path.split('/')[-2] + '.png'))
    image = Image.open(os.path.join(IMAGE_DIR, wav_path.split('/')[-2] + '.png'))
    image_resize = image.resize((150, 200), Image.ANTIALIAS)
    photo1 = ImageTk.PhotoImage(image_resize)
    label_image_left = Label(window,
                        image=photo1, height=200)
    # label_image_left.configure(image=photo1)
    label_image_left.image = photo1
    label_image_left.grid(column=0, row=3, columnspan=2, rowspan=2, pady=(0.0))

    return wav_path

def Play():
    playsound(wav_path)

def ModelSelection(label_model):
    global model_list
    selected_model_path = filedialog.askopenfilename(title=u'Choose file')
    model_loaded = recognize.load_model(selected_model_path)
    model_list.clear()
    model_list.append(model_loaded)
    label_model.configure(text="Selected model: {}".format(os.path.basename(selected_model_path)))
    print(wav_path)
    print(selected_model_path)
    





def PredictFunc(label_prediction):
    print(wav_path)
    try:
        fs, signal = features.read_wav(wav_path)
    except Exception as e:
        print(e)
        label_prediction.configure(text="Read {} failed.".format(wav_path))
        return
    if len(model_list) == 0:
        return
    model_loaded = model_list[0]
    pred_res = model_loaded.predict(fs, signal)
    image3 = Image.open(os.path.join(IMAGE_DIR, pred_res + ".png"))
    image_res2 = image3.resize((150, 200), Image.ANTIALIAS)
    photo3 = ImageTk.PhotoImage(image_res2)
    label_prediction.configure(text="Prediction = {}".format(pred_res))
    label_image3 = Label(window,
                        image=photo3, height=200)
    label_image3.image = photo3
    label_image3.grid(column=1, row=3, columnspan=2, rowspan=2, pady=(0.0))

def TKWindow():
    global label_file_explorer
    window = Tk()

    window.title('League of Legends Character Audio Recognition Based on Gaussian Mixture Model')
    window.resizable(width=False, height=False)
    window.geometry("750x600")



    image_left = Image.open(os.path.join(IMAGE_DIR, "LOL.png"))
    image_left_resized = image_left.resize((150, 200), Image.ANTIALIAS)
    photo_left = ImageTk.PhotoImage(image_left_resized)
    label_image_left = Label(window,
                        image=photo_left, height=200)
    label_image_left.image = photo_left

    image_right = Image.open(os.path.join(IMAGE_DIR, "LOL.png"))
    image_right_resized = image_right.resize((150, 200), Image.ANTIALIAS)
    photo_right = ImageTk.PhotoImage(image_right_resized)
    label_image_right = Label(window,
                             image=photo_right, height=200)
    label_image_right.image = photo_right

    canva=Label(window,
                 text="Prediction",
              font = ('Helvetica', '12')
                                           )
    canva.config(fg="brown")
    canva_left=Label(window,
                 text="Hero selected",
              font = ('Helvetica', '12')
                                           )
    canva_left.config(fg="brown")

    label_file_explorer = Label(window,
                                text="Choose a .wav file to be analyzed!",
                                width=30, height=5,
                                font=('Helvetica', '15')
                                )
    label_file_explorer.config(fg="blue")

    label_model = Label(window,
                             text="Please choose a model.",
                             width=50, height=5,
                             font=('Helvetica', '15')
                             )
    label_model.config(fg='blue')

    label_prediction = Label(window,
                             text="Prediction:",
                             width=50, height=5,
                             font=('Helvetica', '15')
                             )
    label_prediction .config(fg="blue")

    button_explore = Button(window,
                            text="Browse Files",
                            command=BrowseFile,
                            width=18, height=3)


    button_play = Button(window,
                         text="Play",
                         command=Play,
                         width=18, height=3)

    button_test_command = partial(ModelSelection, label_model)
    button_test = Button(window,
                         text="Model selection",
                         command=button_test_command,
                         width=18, height=3)

    button_test2_command = partial(PredictFunc, label_prediction)
    button_test2 = Button(window,
                          text="Prediction",
                          command=button_test2_command,
                          width=18, height=3)

    label_text_true = Label(
        window,
        text="Hero selected",
        width=20, height=5,
        font=('Helvetica', '15')
    )

    label_text_pred = Label(
        window,
        text="Hero predicted",
        width=20, height=5,
        font=('Helvetica', '15')
    )




    label_file_explorer.grid(column=0, row=0, columnspan=3)
    label_prediction.grid(column=0, row=2, columnspan=3)
    label_model.grid(column=0, row=1, columnspan=3)
    label_image_left.grid(column=0, row=3, columnspan=2, rowspan=2, pady=(0.0))
    label_image_right.grid(column=1, row=3, columnspan=2, rowspan=2, pady=(0.0))

    button_explore.grid(column=3, row=0, padx=(0, 0))
    button_play.grid(column=3, row=2, padx=(0, 0))
    button_test.grid(column=3, row=1, padx=(0, 0))
    button_test2.grid(column=3, row=3, padx=(0, 0))
    canva.grid(column=1, row=2, columnspan=2, rowspan=5, pady=(0.0))
    canva_left.grid(column=0, row=2, columnspan=2, rowspan=5, pady=(0.0))
    label_text_true.grid(column=0, row=5, columnspan=2)
    label_text_pred.grid(column=1, row=5, columnspan=2)
    return window

if __name__ == '__main__':
    window = TKWindow()
    window.mainloop()
