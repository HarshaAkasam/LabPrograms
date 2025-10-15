# RNN (LSTM) for IMDB classification
import tensorflow as tf
from tensorflow.keras import layers, models

if __name__=='__main__':
    num_words = 10000
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.imdb.load_data(num_words=num_words)
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    x_train = pad_sequences(x_train, maxlen=200)
    x_test = pad_sequences(x_test, maxlen=200)

    model = models.Sequential([
        layers.Embedding(num_words, 64, input_length=200),
        layers.LSTM(64),
        layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(x_train[:10000], y_train[:10000], epochs=2, batch_size=128)
    loss, acc = model.evaluate(x_test[:2000], y_test[:2000])
    print('Test accuracy (LSTM):', acc)
