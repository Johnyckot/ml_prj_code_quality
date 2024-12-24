import pickle

import pandas as pd
import numpy as np
from scipy.io import arff
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier

data_file_path = 'data/kc1.arff'
output_file_path = 'model.bin'

model_params = {
    'n_estimators':140,
    'max_depth':30
}

def load_df(data_file_path):

    # Load your ARFF file
    data, meta = arff.loadarff(data_file_path)

    # Convert to a pandas DataFrame
    df = pd.DataFrame(data)

    # To decode byte strings into ordinary strings 
    df = df.applymap(lambda x: x.decode() if isinstance(x, bytes) else x)

    df['target'] = df['defects'].map({'true': 1, 'false': 0})
    del df['defects']

    numerical_columns = list(df.columns)
    numerical_columns.remove('target')

    return df , numerical_columns

def train(df, model_params, numerical_columns):
    # split dataset into Train(80%) and Test(20%)   
    df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)

    y_train = df_full_train.target.values

    df_full_train = df_full_train.reset_index(drop=True)

    del df_full_train['target']

    # Vectorize dataset
    dv = DictVectorizer(sparse=False)    

    train_dict = df_full_train[numerical_columns].to_dict(orient='records')
    X_train = dv.fit_transform(train_dict)

    model = RandomForestClassifier(n_estimators=model_params['n_estimators'] , max_depth=model_params['max_depth'] ,random_state=1)
    model.fit(X_train, y_train)

    return dv, model

df, numerical_columns = load_df(data_file_path)
dv, model = train(df,model_params, numerical_columns)

with open(output_file_path, 'wb') as f_out:
        pickle.dump((dv, model), f_out)

print(f'the model is saved to {output_file_path}')