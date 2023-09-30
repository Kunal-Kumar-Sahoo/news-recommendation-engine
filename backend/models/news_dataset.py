import pandas as pd
import tensorflow as tf
import tensorflow_federated as tff

class NewsDataset:
    def __init__(self, csv_file):
        self.dataset = pd.read_csv(csv_file)
        # Preprocessing techniques

    def to_tff_dataset(self):
        tff_dataset_type = tff.SequenceType(tf.float32, self.dataset.shape)
        client_data = [dict(zip(self.dataset.columns, row)) for row in self.dataset.to_dict(orient='records')]
        return tff.simulation.datasets.from_clients_input(client_data, tff_dataset_type)
    