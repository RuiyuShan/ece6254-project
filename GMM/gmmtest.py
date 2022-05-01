import pickle

from recognize import *


def task_test(model_path, test_files_dir):
    model = load_model(model_path)
    test_dir = Path(test_files_dir)
    true_num = 0
    err_num = 0
    total_mum = 0
    confusion_table = {}
    label_list = []
    subdirs = get_subdir(test_dir)
    for dir in subdirs:
        label = dir.name.split('/')[-1]
        label_list.append(label)
    for label in label_list:
        confusion_table[label] = {}
        for label1 in label_list:
            confusion_table[label][label1] = 0
    for dir in subdirs:
        true_label = dir.name.split('/')[-1]
        for wav in dir.iterdir():
            if 'wav' not in wav.suffix:
                print('file suffix is not wav, suffix: {}', wav.suffix)
                continue
            try:
                fs, signal = read_wav(wav)
            except Exception as e:
                print(e)
                continue
            label_pred = model.predict(fs, signal)
            print('predict {} --> {}'.format(wav, label_pred))
            try:
                confusion_table[true_label][label_pred] += 1
            except Exception as e:
                print(e)
                print("true: {}, pred: {}".format(true_label, label_pred))
            if true_label == label_pred:
                true_num += 1
            else:
                err_num += 1
            total_mum += 1
    now_time = time.strftime("%m%d%H%M", time.localtime())

    with open('../../data_6273/confusion_table_{}.pickle'.format(now_time), 'wb') as handle:
        pickle.dump(confusion_table, handle, protocol=pickle.HIGHEST_PROTOCOL)
    generate_confusion_table(confusion_table, now_time)
    print("Total test: {}, true num: {}, err num: {}, error rate: {:.2f}%".format(total_mum, true_num, err_num,
                                                                                  (err_num / true_num)))

def generate_confusion_table(dic, now_time):
    import pandas as pd
    import seaborn as sn
    import matplotlib.pyplot as plt
    df_cfm = pd.DataFrame.from_dict(dic)
    plt.figure(figsize=(30, 20))
    cfm_plot = sn.heatmap(df_cfm, cmap='Blues', annot=True, fmt='g')
    cfm_plot.figure.savefig("../../data_6273/cfm_{}.png".format(now_time))
