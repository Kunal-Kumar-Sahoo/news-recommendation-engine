import tensorflow as tf
import tensorflow_federated as tff


class FederatedServer:
    def __init__(self, model, trainer, initial_weights):
        self.model = model
        self.trainer = trainer
        self.server_state = initial_weights

    def federated_training(self, client_datasets, num_epochs):
        for _ in range(num_epochs):
            for client_dataset in client_datasets:
                self.server_state = self.trainer.federated_train_step(
                    self.server_state, client_dataset
                )
    
    def evaluate(self, test_dataset):
        test_losses = tf.keras.metrics.Mean()
        test_accuracy = tf.keras.metrics.BinaryAccuracy()

        for batch in test_dataset:
            batch_loss = self.compute_loss(batch)
            batch_accuracy = self.compute_accuracy(batch)
            test_losses(batch_loss)
            test_accuracy(batch['likes'], self.model(batch))

        print(f'Test Loss: {test_losses.result().numpy()}')
        print(f'Test Accuracy: {test_accuracy.result().numpy()}')

    def compute_loss(self, batch):
        output = self.model(batch)
        loss = tf.reduce_mean(tf.keras.losses.binary_crossentropy(
            batch['likes'], output))
        return loss

    def compute_accuracy(self, batch):
        output = self.model(batch)
        accuracy = tf.keras.metrics.binary_accuracy(batch['likes'], output)
        return accuracy
    
        