import time
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
    time_start = time.time()
    m = Model(n_component)
    subdirs = get_subdir(path)
    n_files = 0
    for dir in subdirs:
        label = dir.name.split('/')[-1]
        wavs = dir.iterdir()
        for wav in wavs:
            if 'wav' not in wav.suffix:
                print("not wav file, skip")
                continue
            try:
                fs, signal = read_wav(wav)
            except Exception as e:
                print(e)
                continue
            print("enroll {}".format(wav))
            m.enroll(label, fs, signal)
            n_files += 1
    m.train()
    m.dump(output_path)
    print('Trained {} wav files.'.format(n_files))
    time_end = time.time()
    print("Used {:.2f}s for training.".format(time_end - time_start))

def predict(model, input_file):
    assert input_file.split('.')[-1] == 'wav'
    fs, signal = read_wav(input_file)
    res = model.predict(fs, signal)
    return res