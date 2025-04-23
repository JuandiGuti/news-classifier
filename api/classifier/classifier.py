from collections import defaultdict
import math
from .tokenizer import preprocess_text

class NaiveBayesClassifier:
    def __init__(self):
        self.class_frecuency = defaultdict(int)
        self.word_frecuency = defaultdict(lambda: defaultdict(int))
        self.total_documents = 0
        self.vocabulary = set()

    def train(self, data):
        for text, category in data:
            tokens = preprocess_text(text)
            self.class_frecuency[category] += 1
            self.total_documents += 1
            for word in tokens:
                self.word_frecuency[category][word] += 1
                self.vocabulary.add(word)

    def predict(self, text):
        tokens = preprocess_text(text)
        max_prob = float('-inf')
        better_class = None

        for category in self.class_frecuency:
            log_prob = math.log(self.class_frecuency[category] / self.total_documents)
            total_words_in_class = sum(self.word_frecuency[category].values())
            for token in tokens:
                token_count = self.word_frecuency[category].get(token, 0)
                prob = (token_count + 1) / (total_words_in_class + len(self.vocabulary))
                log_prob += math.log(prob)
            if log_prob > max_prob:
                max_prob = log_prob
                better_class = category

        return better_class
