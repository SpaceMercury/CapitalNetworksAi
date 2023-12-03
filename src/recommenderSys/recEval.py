from sklearn import metrics
import numpy as np
from rec import recommenderSys

def auc_score(predictions, test):
    fpr, tpr, thresholds = metrics.roc_curve(test, predictions)
    return metrics.auc(fpr, tpr)

def calc_mean_auc(train, test, model):
    store_auc = []
    popularity_auc = []
    pop_items = np.array(train.sum(axis=0)).reshape(-1)
    item_vecs = model.item_factors
    for user in range(test.shape[0]):
        training_row = train[user,:].toarray().reshape(-1)
        zero_inds = np.where(training_row == 0)
        user_vec = model.user_factors[user,:]
        pred = user_vec.dot(item_vecs).toarray()[0,zero_inds].reshape(-1)
        actual = test[user,:].toarray()[0,zero_inds].reshape(-1)
        pop = pop_items[zero_inds]
        store_auc.append(auc_score(pred, actual))
        popularity_auc.append(auc_score(pop, actual))

    return float('%.3f'%np.mean(store_auc)), float('%.3f'%np.mean(popularity_auc))

def main():

