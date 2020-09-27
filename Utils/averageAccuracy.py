import numpy as np
from operator import truediv

def AA_andEachClassAccuracy(confusion_matrix):
    list_diag = np.diag(confusion_matrix)
    list_raw_sum = np.sum(confusion_matrix, axis=1)
    each_acc = np.nan_to_num(truediv(list_diag, list_raw_sum))
    average_acc = np.mean(each_acc)
    precision = np.diag(confusion_matrix)/np.sum(confusion_matrix, axis=0)
    average_precision = np.sum(precision)/confusion_matrix.shape[0]
    return each_acc, average_acc,precision,average_precision