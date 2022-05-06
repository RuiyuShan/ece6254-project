import pickle

from gmmtest import generate_confusion_table


if __name__ == '__main__':
    with open('/home/ruiyushan/proj/data_6254/confusion_table_05020551.pickle', 'rb') as handle:
        dic = pickle.load(handle)

    generate_confusion_table(dic, "05020551")
    print('success')