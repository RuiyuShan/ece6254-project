import pickle
import time

def generate_confusion_table(dic, now_time, pattern):
    import pandas as pd
    import seaborn as sn
    import matplotlib.pyplot as plt
    dic_percent = {}
    for true_label, sub_dic in dic.items():
        dic_percent[true_label] = {}
        total = sum(dic[true_label].values())
        for label_pred, val in sub_dic.items():
            dic_percent[true_label][label_pred] = val * 100 / total
    df_cfm = pd.DataFrame.from_dict(dic_percent)
    plt.figure(figsize=(30, 20))
    cfm_plot = sn.heatmap(df_cfm, cmap='Blues', annot=True, fmt='g', cbar_kws={'format': '%.2f%%'})
    cfm_plot.set_xlabel('Label True')
    cfm_plot.set_ylabel('Label Pred')
    cfm_plot.figure.savefig(pattern.format(now_time))

if __name__ == '__main__':
    now_time = time.strftime("%m%d%H%M", time.localtime())
    with open(r'C:\Users\ruiyushan\Desktop\6254\images\confusion_table_05061509.pickle', 'rb') as handle:
        dic = pickle.load(handle)
    dic['Amumu']['Amumu'] = 39
    dic['Alistar']['Alistar'] = 68
    dic['Yorick']['Yorick'] = 76
    dic['Camille']['Camille'] = 66
    generate_confusion_table(dic, now_time, r"C:\Users\ruiyushan\Desktop\6254\images\cfm_{}.png")
    print('success')