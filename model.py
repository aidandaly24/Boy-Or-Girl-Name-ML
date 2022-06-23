import numpy as np
from matplotlib import pyplot as plt
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Embedding, Bidirectional, LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from preprocess import processedNamesDF


def lstmModel(nameLength=50, dim=256, alphabets=27):
    model = Sequential([
        Embedding(alphabets, dim, input_length=nameLength),
        Bidirectional(LSTM(units=128, recurrent_dropout=0.2, dropout=0.2)),
        Dense(1, activation="sigmoid")
    ])
    model.compile(loss='binary_crossentropy',
                  optimizer=Adam(learning_rate=0.001),
                  metrics=['accuracy'])
    return model


model = lstmModel(nameLength=50, dim=256, alphabets=27)

# split train and test data
xArray = np.asarray(processedNamesDF['name'].values.tolist())
yArray = np.asarray(processedNamesDF['gender'].values.tolist())

xTrain, xTest, yTrain, yTest = train_test_split(
    xArray, yArray, test_size=0.2, random_state=0)

# trains model
callbacksOfModel = [EarlyStopping(monitor='val_accuracy', min_delta=1e-3,
                                  patience=5, mode='max', restore_best_weights=True, verbose=1), ]

historyData = model.fit(x=xTrain, y=yTrain, batch_size=64, epochs=50,
                        validation_data=(xTest, yTest), callbacks=callbacksOfModel)

model.save('boyorgirl.h5')

# plottiong accuracy of the model so I can see
plt.plot(historyData.history['accuracy'], label='train')
plt.plot(historyData.history['val_accuracy'], label='val')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
