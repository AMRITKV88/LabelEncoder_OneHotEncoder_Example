# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer


# %%
# Sample 2D matricx data
x = [['Germany','Male'],['France','Female'],['Spain', 'Female'],[ 'Germany', 'Female']]
x = np.asarray(x)


# %%
# LabelEncoder on first column
labelEncoder_X_1 = LabelEncoder()
x[:, 0] = labelEncoder_X_1.fit_transform(x[:, 0])
print(x)


# %%
# LabelEncoder on second column
x[:, 1] = labelEncoder_X_1.fit_transform(x[:, 1])
print(x)


# %%
x = x.reshape(len(x),2)
print(x)


# %%
# OneHotEncoder on entire x In output - First 3 columns are country columns and last two are gender columns.
oneHotEncoder = OneHotEncoder(sparse = False)
x = np.asarray(oneHotEncoder.fit_transform(x))
print(x) 


