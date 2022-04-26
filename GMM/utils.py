from pathlib import Path
import shutil
import os


def make_test_data(wavs_dir, test_data_dir, n_file):
    for dir in Path(wavs_dir).iterdir():
        if not dir.is_dir():
            continue
        label = dir.name.split('/')[-1]
        new_subdir = os.path.join(test_data_dir, label)
        os.mkdir(new_subdir)
        n = 0
        for wav in dir.iterdir():
            if n >= n_file:
                break
            if 'wav' not in wav.suffix:
                print('file suffix is not wav, suffix: {}', wav.suffix)
                continue
            shutil.copy(wav, os.path.join(new_subdir, os.path.basename(wav)))
            print('copied {} to {}'.format(wav, os.path.join(new_subdir, os.path.basename(wav))))
            n += 1

if __name__ == '__main__':
    make_test_data("/Users/shanruiyu/Desktop/ECE6254/ece6254-project/data/wavs",
                   "/Users/shanruiyu/Desktop/ECE6254/ece6254-project/data/test",
                   n_file=3)
