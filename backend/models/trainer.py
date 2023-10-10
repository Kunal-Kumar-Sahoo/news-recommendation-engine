import tensorflow as tf
import tensorflow_federated as tff


class FederatedTrainer:
    def __init__(self, model, client_optimizer, server_optimizer):
        self.model = model
        self.client_optimizer = client_optimizer
        self.server_optimizer = server_optimizer

    @tf.function
    def federated_train_step(self, server_weights, client_dataset):
        @tff.tf_computation
        def client_update(weights, batch):
            with tf.GradientTape() as tape:
                output = self.model(batch)
                loss = tf.reduce_mean(
                    tf.keras.losses.binary_crossentropy(
                        batch['likes'], output
                ))
            grads = tape.gradient(loss, weights)
            return grads
        
        
        client_grads = tff.federated_map(client_update, (server_weights, client_dataset))

        averaged_grads = tff.federated_mean(client_grads)
        server_weights = self.server_optimizer.apply_gradients(
            zip(averaged_grads, server_weights))
        return server_weights