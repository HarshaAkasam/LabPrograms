# CNN for MNIST using Keras
import tensorflow as tf
from tensorflow.keras import layers, models

if __name__=='__main__':
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train = x_train.reshape(-1,28,28,1).astype('float32')/255.0
    x_test = x_test.reshape(-1,28,28,1).astype('float32')/255.0

    model = models.Sequential([
        layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
        layers.MaxPooling2D((2,2)),
        layers.Conv2D(64, (3,3), activation='relu'),
        layers.MaxPooling2D((2,2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(x_train[:20000], y_train[:20000], epochs=3, batch_size=128, validation_split=0.1)
    loss, acc = model.evaluate(x_test[:5000], y_test[:5000])
    print('Test accuracy:', acc)
