import sys

from python_speech_features import mfcc
from scipy.io import wavfile


def read_wav(path):
    fs, signal = wavfile.read(path)
    if len(signal.shape) != 1:
        signal = signal[:, 0]
    return fs, signal

def get_feature(fs, signal):
    feature = mfcc(signal, fs, nfft=1200)
    if len(feature) == 0:
        print("ERR: extract mfcc failed. ", file=sys.stderr)
    return feature

