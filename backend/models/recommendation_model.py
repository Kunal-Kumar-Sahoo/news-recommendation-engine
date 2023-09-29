import tensorflow as tf
from transformers import TFBertModel, BertTokenizer
from transformers import TFT5ForConditionalGeneration, T5Tokenizer

class RecommendationModel(tf.keras.Model):
    def __init__(self, bert_model_name, transformer_model_name, max_sequence_length):
        super(RecommendationModel, self).__init__()

        self.bert = TFBertModel.from_pretrained(bert_model_name)
        self.tokenizer = BertTokenizer.from_pretrained(bert_model_name)
        self.transformer = TFT5ForConditionalGeneration.from_pretrained(transformer_model_name)

        self.max_sequence_length = max_sequence_length
    
    def call(self, inputs):
        input_ids = self.tokenizer(
            inputs, padding='max_length', truncation=True, max_length=self.max_sequence_length, return_tensors='tf'
        )['input_ids']
        
        bert_outputs = self.bert(input_ids)
        transformer_input = bert_outputs['last_hidden_state']

        recommendations = self.transformer.generate(transformer_input)
        return recommendations
    
bert_model_name = 'bert-base-uncased'
transformer_model_name = 't5-small'
max_sequence_length = 128

model = RecommendationModel(bert_model_name, transformer_model_name, max_sequence_length)