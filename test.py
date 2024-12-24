import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model.bin'
threshold = 0.65

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

program = {"loc":1.0
            ,"v(g)":1.0
            ,"ev(g)":1.0
            ,"iv(g)":1.0
            ,"n":1.0
            ,"v":1.0
            ,"l":1.0
            ,"d":1.0
            ,"i":1.0
            ,"e":1.0
            ,"b":1.0
            ,"t":1.0
            ,"lOCode":1.0
            ,"lOComment":1.0
            ,"lOBlank":1.0
            ,"locCodeAndComment":1.0
            ,"uniq_Op":1.0
            ,"uniq_Opnd":1.0
            ,"total_Op":1.0
            ,"total_Opnd":1.0
            ,"branchCount":1.0
            ,"target":1.0}

X = dv.transform([program])
y_pred = model.predict_proba(X)[0, 1]
subscribe = y_pred >= threshold


result = {
    'bugs_probability': float(y_pred),
    'defects_decision': bool(subscribe)
}

print(result)


