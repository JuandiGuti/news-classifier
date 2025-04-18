import os
import pandas as pd
import re

STOPWORDS = {
    'a', 'an', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'was', 'were',
    'will', 'with', 'you', 'your', 'i', 'we', 'they', 'but', 'and', 'or',
    'not', 'do', 'does', 'did', 'this', 'these', 'those'
}

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)  # keep only letters and spaces
    words = text.split()
    filtered = [w for w in words if w not in STOPWORDS]
    return ' '.join(filtered)

def load_dataset(path):
    data = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.txt'):
                category = os.path.basename(root)
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                    text = f.read()
                    cleaned_text = clean_text(text)
                    data.append((cleaned_text, category))
    return data