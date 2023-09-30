from news_dataset import NewsDataset
from federated_learning import FederatedLearning

if __name__ == '__main__':
    dataset = NewsDataset('dataset/data.csv')
    federated_data = dataset.to_tff_dataset()

    input_size = None # to be filled
    hidden_size = None
    output_size = 1
    n_epochs = 50

    federated_learning = FederatedLearning(federated_data, n_epochs, input_size, hidden_size, output_size)
    federated_learning.train()