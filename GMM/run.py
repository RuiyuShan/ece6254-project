import pickle
from model import Model
import os.path
from pathlib import Path


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



def train_all(path, n_component=32):
    """
    Train all hero audio data in path dir.
    :param n_component: GMM component num.
    :param path: dir which contains hero audio data.
    """
    m = Model(n_component)
    subdirs = get_subdir(path)

if __name__ == '__main__':
    print("")