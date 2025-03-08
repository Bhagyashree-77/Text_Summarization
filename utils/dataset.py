class Vocab:
    def __init__(self):
        self.words = []
    
    def add_word(self, word):
        self.words.append(word)
    
    def size(self):
        return len(self.words)

class Batcher:
    def __init__(self, batch_size):
        self.batch_size = batch_size
    
    def create_batches(self, data):
        return [data[i:i + self.batch_size] for i in range(0, len(data), self.batch_size)]