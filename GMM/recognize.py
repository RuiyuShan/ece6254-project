from pathlib import Path
from features import *
import pickle
from model import Model

def load_model(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
        return model

def get_subdir(path):
    subdirs = []
    for subdir in Path(path).iterdir():
        if subdir.is_dir():
            subdirs.append(subdir)
            print(subdir)
    return subdirs



def train_all(path, output_path, n_component=32):
    """
    Train all hero audio data in path dir.
    :param n_component: GMM component num.
    :param path: dir which contains hero audio data.
    """
    m = Model(n_component)
    subdirs = get_subdir(path)
    for dir in subdirs:
        label = dir.name.split('/')[-1]
        wavs = dir.iterdir()
        for wav in wavs:
            if 'wav' not in wav.suffix:
                print("not wav file, skip")
                continue
            print("enroll {}".format(wav))
            fs, signal = read_wav(wav)
            m.enroll(label, fs, signal)
    m.train()
    m.dump(output_path)

def predict(model, input_file):
    assert input_file.split('.')[-1] == 'wav'
    fs, signal = read_wav(input_file)
    res = model.predict(fs, signal)
    return res