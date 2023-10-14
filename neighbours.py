import pandas as pd
import numpy as np
import pickle
from sklearn import preprocessing
def neigh(ls):
    with open('dictionary.txt','rb') as handle:
        data = handle.read()
    d = pickle.loads(data)
    
    df = pd.read_csv('parsed_without_normal.csv')
    point = ls
    n =7
    df.drop(columns=df.columns[0], axis=1,  inplace=True)
    tf = df.drop('Default',axis = 1)
    scaler = preprocessing.MinMaxScaler()
    d = scaler.fit_transform(tf)
    n_closest_points = tf.loc[(tf - point).pow(2).sum(axis=1).nsmallest(n).index]
    index = n_closest_points.index
    z = pd.DataFrame()
    for i in index:
        z = pd.concat([z,df.iloc[[i]]])
    
    
    edu = {1:"Bachelor's",
           2:"Master's",
           3:"High School",
           4:"PhD"}
    emp = {1:"Full-Time",
           2:"Unemployed",
           3:"Self-Employed",
           4:"Part-Time"}
    mari = {1:"Divorced",
            2:"Married",
            3:"Single"}
    typ = {1:"Other",
           2:"Auto",
           3:"Business",
           4:"Home",
           5:"Education"}
    yn = {0:"No",
          1:"Yes"}
    
    tst = []
    for i in z['education']:
        tst.append(edu[i])
    z['education'] = tst
    tst = []
    for i in z['has_cosigner']:
        tst.append(yn[i])
    z['has_cosigner'] = tst
    tst = []
    for i in z['employment_type']:
        tst.append(emp[i])
    z['employment_type'] = tst
    tst = []
    for i in z['marital_status']:
        tst.append(mari[i])
    z['marital_status'] = tst
    tst = []
    for i in z['has_mortgage']:
        tst.append(yn[i])
    z['has_mortgage'] = tst
    tst = []
    for i in z['has_dependents']:
        tst.append(yn[i])
    z['has_dependents'] = tst
    tst = []
    for i in z['loan_purpose']:
        tst.append(typ[i])
    z['loan_purpose'] = tst
    tst = []
    for i in z['Default']:
        tst.append(yn[i])
    z['Default'] = tst
    return(z)