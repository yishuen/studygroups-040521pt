import pandas as pd
import numpy as np
import pickle

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

def make_prediction(var, skew, kurt, entropy):
    
    model = pickle.load(open("model.pkl", "rb"))
    pred = model.predict([[var, skew, kurt, entropy]])
    
    if pred[0] == 0:
        return 'Authentic'
    else:
        return 'Forged'
