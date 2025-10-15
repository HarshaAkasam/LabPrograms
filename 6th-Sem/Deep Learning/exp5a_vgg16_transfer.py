# Transfer learning with VGG16 for image classification (example on CIFAR10 features)
import tensorflow as tf
from tensorflow.keras import layers, models, applications
import numpy as np

if __name__=='__main__':
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
    x_train = x_train.astype('float32')/255.0; x_test = x_test.astype('float32')/255.0
    base = applications.VGG16(weights='imagenet', include_top=False, input_shape=(32,32,3))
    base.trainable = False
    model = models.Sequential([
        base,
        layers.Flatten(),
        layers.Dense(256, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(x_train[:5000], y_train[:5000], epochs=3, batch_size=64)
    loss, acc = model.evaluate(x_test[:2000], y_test[:2000])
    print('Test accuracy (transfer):', acc)
