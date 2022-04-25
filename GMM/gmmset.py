import operator

from sklearn.mixture import GaussianMixture
import numpy as np

class GMMSet:
    def __init__(self, n_components=32):
        self.n_components = n_components
        self.gmms = []
        self.labels = []

    def fit_new(self, features, label):
        self.labels.append(label)
        skgmm = GaussianMixture(self.n_components, max_iter=200)
        skgmm.fit(features)
        self.gmms.append(skgmm)

    def predict(self, features):
        scores = [gmm.score(features) for gmm in self.gmms]
        sorted_score_tuple = sorted(enumerate(scores), key=operator.itemgetter(1), reverse=True)
        max_score_item_idx = sorted_score_tuple[0][0]
        return self.labels[max_score_item_idx]



