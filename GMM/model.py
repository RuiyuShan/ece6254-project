import pickle
from gmmset import *
from collections import defaultdict
from features import *


class Model:
    def __init__(self, n_component=32):
        self.gmmset = GMMSet(n_component)
        self.features = defaultdict(list)

    def enroll(self, label, fs, signal):
        feat = get_feature(fs, signal)
        self.features[label].extend(feat)

    def train(self):
        self.gmmset = GMMSet()
        for label, feats in self.features.items():
            try:
                self.gmmset.fit_new(feats, label)
                print('feat new: {}'.format(label))
            except Exception as e:
                print("training {} failed".format(label))
                print(e)

    def predict(self, fs, signal):
        try:
            feat = get_feature(fs, signal)
        except Exception as e:
            print(e)
        return self.gmmset.predict(feat)

    def dump(self, model_name):
        self.features.clear()
        print('Saving model...')
        with open(model_name, 'wb') as f:
            pickle.dump(self, f, -1)

