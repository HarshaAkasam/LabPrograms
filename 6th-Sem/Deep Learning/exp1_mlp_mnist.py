# Multilayer Perceptron for MNIST using Keras (TensorFlow)
import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

def build_mlp(input_shape, num_classes):
    model = models.Sequential([
        layers.Flatten(input_shape=input_shape),
        layers.Dense(512, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(256, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

if __name__=='__main__':
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train = x_train.astype('float32')/255.0
    x_test = x_test.astype('float32')/255.0
    model = build_mlp(input_shape=(28,28), num_classes=10)
    model.fit(x_train[:20000], y_train[:20000], epochs=5, batch_size=128, validation_split=0.1)
    loss, acc = model.evaluate(x_test[:5000], y_test[:5000])
    print('Test accuracy:', acc)
