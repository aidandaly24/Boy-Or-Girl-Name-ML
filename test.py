from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np


def preprocess(names):
    names['name'] = names['name'].str.lower()
    names['name'] = [list(name)
                     for name in names['name']]
    nameLength = 50
    names['name'] = [(name + [' ']*nameLength)[:nameLength]
                     for name in names['name']]
    names['name'] = [[max(0, ord(char)-96)for char in name]
                     for name in names['name']]
    return names


pred_model = load_model('boyorgirl.h5')

# Input names
namesInput = input("Enter names you want tested with a \",\" between each: ")
namesTest = namesInput.split(",")
for i in range(len(namesTest)):
    namesTest[i] = namesTest[i].strip()


# Convert to dataframe
predDF = pd.DataFrame({'name': namesTest})

# Preprocess
predDF = preprocess(predDF)

# Predictions
result = pred_model.predict(np.asarray(
    predDF['name'].values.tolist())).squeeze(axis=1)

predDF['Boy or Girl?'] = [
    'Boy' if logit > 0.5 else 'Girl' for logit in result
]

predDF['Probability'] = [
    logit if logit > 0.5 else 1.0 - logit for logit in result
]

# Format the output
predDF['name'] = namesTest
predDF.rename(columns={'name': 'Name'}, inplace=True)
predDF['Probability'] = predDF['Probability'].round(2)
predDF.drop_duplicates(inplace=True)

predDF.head()
print(predDF)
