import tensorflow_federated as tff
import tensorflow as tf
from news_dataset import NewsDataset
from recommendation_model import create_compiled_keras_model


class FederatedLearning:
    def __init__(self, train_data, n_epochs, input_size, hidden_size, output_size):
        self.train_data = train_data
        self.n_epochs = n_epochs
        self.model = create_compiled_keras_model(input_size, hidden_size, output_size)
        self.tff_model = self._create_tff_model()

    def _create_tff_model(self):
        @tff.tf_computation
        def model_fn():
            return tff.learning.from_keras_model(self.model, input_spec=self.train_data.element_type_structure)
        
        iterative_process = tff.learning.build_federated_averaging_process(
            model_fn, 
            client_optimizer_fn=lambda: tf.keras.optimizers.Adam(learning_rate=0.1)
        )

        return iterative_process
    
    def train(self):
        state = self.tff_model.initialize()
        for epoch in range(self.n_epochs):
            state, metrics = self.tff_model.next(state, self.train_data)
            print(f'Epoch {epoch+1}, Metrics: {metrics}')