# Learn small word embeddings on IMDB using Embedding layer and visualize via PCA (quick demo)
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.decomposition import PCA
import numpy as np

if __name__=='__main__':
    num_words = 5000
    (x_train, y_train), _ = tf.keras.datasets.imdb.load_data(num_words=num_words)
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    x_train = pad_sequences(x_train, maxlen=100)
    model = models.Sequential([
        layers.Embedding(num_words, 64, input_length=100),
        layers.GlobalAveragePooling1D(),
        layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(x_train[:10000], y_train[:10000], epochs=2, batch_size=128)
    emb_layer = model.layers[0]
    embeddings = emb_layer.get_weights()[0]  # shape: (num_words, dim)
    pca = PCA(n_components=2)
    coords = pca.fit_transform(embeddings[:200])
    print('PCA coords shape:', coords.shape)
