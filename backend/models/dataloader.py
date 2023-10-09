import pandas as pd
import tensorflow as tf
import tensorflow_federated as tff

class Dataloader:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        self.category_vocab = self.data['Category'].unique().tolist()
        self.headlines_vocab = list(set(self.data['Headlines']))

    def create_tf_dataset(self):
        dataset = tf.data.Dataset.from_tensor_slices({
            'news_headline': tf.constant(self.data['Headlines']),
            'news_category': tf.constant(self.data['Category']),
            'likes': tf.constant(self.data['User Likes'])
        })

        return dataset