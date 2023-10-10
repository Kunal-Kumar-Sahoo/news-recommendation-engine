import os
import tensorflow as tf
# import tensorflow_federated as tff
from dataloader import Dataloader
from model import NewsRecommendationModel
from trainer import FederatedTrainer
from server import FederatedServer


num_epochs = 10
embedding_dim = 64
lstm_units = 64

client_datasets = os.listdir('backend/dataset')
num_clients = len(client_datasets)

for i in range(num_clients):
    data_loader = Dataloader(os.path.join('backend/dataset', client_datasets[i]))
    client_dataset = data_loader.create_tf_dataset()
    client_datasets.append(client_dataset)

num_headline_vocab = len(data_loader.headlines_vocab)
model = NewsRecommendationModel(num_headline_vocab, embedding_dim, lstm_units)

client_optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)
server_optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)
trainer = FederatedTrainer(model, client_optimizer, server_optimizer)

initial_weights = model.get_weights()
federated_server = FederatedServer(model, trainer, initial_weights)

federated_server.federated_training(client_datasets, num_epochs)
