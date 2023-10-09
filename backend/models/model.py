import tensorflow as tf
import tensorflow_federated as tff
from collections import OrderedDict


class NewsRecommendationModel(tf.Module):
    def __init__(self, num_headline_vocab, embedding_dim, lstm_units):
        self.embedding_layer = tf.keras.layers.Embedding(
            input_dim=num_headline_vocab,
            output_dim=embedding_dim,
        )
        self.lstm_layer = tf.keras.layers.LSTM(lstm_units)
        self.fc_layer = tf.keras.layers.Dense(1, activation='sigmoid')

    def __call__(self, batch):
        headline_embeddings = self.embedding_layer(batch['news_headlines'])
        lstm_output = self.lstm_layer(headline_embeddings)
        predictions = self.fc_layer(lstm_output)
        return predictions
    
    def get_weights(self):
        weights = OrderedDict()  
        weights['embedding_layer'] = self.embedding_layer.get_weights()
        weights['lstm_layer'] = self.lstm_layer.get_weights()
        weights['fc_layer'] = self.fc_layer.get_weights()
        return weights