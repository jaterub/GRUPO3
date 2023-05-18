import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Codigo 2

import pandas
import numpy
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
st.set_option('deprecation.showPyplotGlobalUse', False)

train_df = pd.read_csv('data/train.csv')
test_df = pd.read_csv('data/test.csv')

train_df['Sex'] = train_df['Sex'].map({'male': 0, 'female': 1})
test_df['Sex'] = test_df['Sex'].map({'male': 0, 'female': 1})
train_df['Sex'].fillna(train_df['Age'].mean(), inplace=True)
test_df['Sex'].fillna(test_df['Age'].mean(), inplace=True)