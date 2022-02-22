# load the train and test
# train algorithm
# save the metrices, parameters
import os
import warnings
import sys
import pandas as pd
import numpy as np
#from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import precision_recall_curve, auc
from sklearn.metrics import confusion_matrix
from get_data import read_params
import argparse
import joblib
import json


"""def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2"""

def train_and_evaluate(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    random_state = config["base"]["random_state"]
    model_dir = config["model_dir"]

    alpha = config["train_and_evaluate"]["alpha"]
    #l1_ratio = config["estimators"]["ElasticNet"]["params"]["l1_ratio"]

    target = [config["base"]["target_col"]]

    train = pd.read_csv(train_data_path, sep=",")
    test = pd.read_csv(test_data_path, sep=",")

    train_y = train[target]
    test_y = test[target]

    train_x = train.drop(target, axis=1)
    test_x = test.drop(target, axis=1)

    sc = StandardScaler()
    train_x = sc.fit_transform(train_x)
    test_x = sc.fit_transform(test_x)

    classifier = GaussianNB()
    classifier.fit(train_x , train_y)

    predicted_qualities = classifier.predict(test_x)
    predictions = predicted_qualities[:,-1]
    cm = confusion_matrix(test_y , predicted_qualities)

    # generate scores
    precision, recall, thresholds = precision_recall_curve(test_y, predictions)
    auc = auc(recall, precision)

#####################################################
    scores_file = config["reports"]["scores"]
    params_file = config["reports"]["params"]

    with open(scores_file, "w") as f:
        json.dump({'auc': auc}, f)

    with open(params_file, "w") as f:
        proc_dict = {'proc': [{
        'precision': p,
        'recall': r,
        'threshold': t
        } for p, r, t in zip(precision, recall, thresholds)
    ]}
    json.dump(proc_dict, f)


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)