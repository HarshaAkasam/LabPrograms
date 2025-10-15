# Boston Housing price prediction using Keras (regression)
import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

if __name__=='__main__':
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.boston_housing.load_data()
    mean = x_train.mean(axis=0)
    std = x_train.std(axis=0)
    x_train = (x_train - mean)/std
    x_test = (x_test - mean)/std

    model = models.Sequential([
        layers.Dense(64, activation='relu', input_shape=(x_train.shape[1],)),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    model.fit(x_train, y_train, epochs=50, batch_size=32, validation_split=0.1, verbose=0)
    loss, mae = model.evaluate(x_test, y_test, verbose=0)
    print('Test MAE:', mae)
