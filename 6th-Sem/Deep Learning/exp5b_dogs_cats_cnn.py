# Simple CNN for binary classification (dogs vs cats). For demo we reuse CIFAR10 classes 3 (cat) and 5 (dog)
import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

if __name__=='__main__':
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
    # keep only classes 3 (cat) and 5 (dog)
    train_mask = (y_train.flatten()==3) | (y_train.flatten()==5)
    test_mask = (y_test.flatten()==3) | (y_test.flatten()==5)
    x_train, y_train = x_train[train_mask], y_train[train_mask]==5
    x_test, y_test = x_test[test_mask], y_test[test_mask]==5
    x_train = x_train.astype('float32')/255.0; x_test = x_test.astype('float32')/255.0

    model = models.Sequential([
        layers.Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3)),
        layers.MaxPooling2D(2,2),
        layers.Conv2D(64,(3,3),activation='relu'),
        layers.MaxPooling2D(2,2),
        layers.Flatten(),
        layers.Dense(64,activation='relu'),
        layers.Dense(1,activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(x_train[:2000], y_train[:2000], epochs=3, batch_size=64)
    loss, acc = model.evaluate(x_test[:1000], y_test[:1000])
    print('Test accuracy (cats vs dogs demo):', acc)
