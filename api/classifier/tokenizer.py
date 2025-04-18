import re

def preprocess_text(text):
     text = text.lower()
     text = re.sub(r'[^a-záéíóúñü\s]', '', text)
     tokens = text.split()
     return tokens