from pathlib import Path
import shutil
import os


def make_test_data(wavs_dir, test_data_dir, test_percent):
    for dir in Path(wavs_dir).iterdir():
        if not dir.is_dir():
            continue
        label = dir.name.split('/')[-1]
        new_subdir = os.path.join(test_data_dir, label)
        os.mkdir(new_subdir)
        wav_num = 0
        for _ in dir.iterdir():
            wav_num += 1
        n_file = round(wav_num * test_percent)
        n = 0
        for wav in dir.iterdir():
            if n >= n_file:
                break
            if 'wav' not in wav.suffix:
                print('file suffix is not wav, suffix: {}', wav.suffix)
                continue
            shutil.move(wav, os.path.join(new_subdir, os.path.basename(wav)))
            print('move {} to {}'.format(wav, os.path.join(new_subdir, os.path.basename(wav))))
            n += 1

if __name__ == '__main__':
    make_test_data("/home/ruiyushan/proj/data_6273/wavs",
                   "/home/ruiyushan/proj/data_6273/test",
                   test_percent=0.2)
