from recognize import *


def task_test(model_path, test_files_dir):
    model = load_model(model_path)
    test_dir = Path(test_files_dir)
    true_num = 0
    err_num = 0
    total_mum = 0
    subdirs = get_subdir(test_dir)
    for dir in subdirs:
        true_label = dir.name.split('/')[-1]
        for wav in dir.iterdir():
            if 'wav' not in wav.suffix:
                print('file suffix is not wav, suffix: {}', wav.suffix)
                continue
            fs, signal = read_wav(wav)
            label_pred = model.predict(fs, signal)
            if true_label == label_pred:
                true_num += 1
            else:
                err_num += 1
            total_mum += 1
    print("Total test: {}, true num: {}, err num: {}, error rate: %{:.2f}".format(total_mum, true_num, err_num,
                                                                                  (err_num / true_num)))
