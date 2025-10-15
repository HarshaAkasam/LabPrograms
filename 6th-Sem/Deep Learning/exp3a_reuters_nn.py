# Reuters multiclass classification using Keras
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.sequence import pad_sequences

if __name__=='__main__':
    num_words = 10000
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.reuters.load_data(num_words=num_words)
    x_train = pad_sequences(x_train, maxlen=200)
    x_test = pad_sequences(x_test, maxlen=200)
    num_classes = max(y_train)+1

    model = models.Sequential([
        layers.Embedding(num_words, 64, input_length=200),
        layers.GlobalAveragePooling1D(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(x_train[:10000], y_train[:10000], epochs=3, batch_size=128, validation_split=0.1)
    loss, acc = model.evaluate(x_test[:5000], y_test[:5000])
    print('Test accuracy:', acc)
