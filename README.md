# Boy-Or-Girl-Name-ML
This script uses NLP and an LSTM recurrent neural network to determine if a name is a boys name or a girls name.


The getNames.py file is used to gather a data set of names from Google Cloud. If you want to recreate this code you will need to sign up for a Google Cloud Platform account to utilize this data set.

The preprocess.py file uses Natural Language Processing (NLP) techniques to normalize the data set.

The model.py file uses a Long Short Term Memory (LSTM) Recurrent Neural Network to train our model. It is defaulted to train the model with 50 epochs, this can be altered but you will in return receive a less accurate model. Once the model is trained you will see a pop up with the results of accuracy throughout the training by epic. The model will also be saved to the local folder.

The test.py file uses the saved model to test names. You can alter this file to your liking to test names in the way you see fit.


Thank you for checking out this repository!
