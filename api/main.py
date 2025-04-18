from pathlib import Path
from classifier.load_data import load_dataset
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from classifier.classifier import NaiveBayesClassifier

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class text(BaseModel):
    texto: str

@app.post("/get-text-news")
def get_text_news(data: text):
    classifier = NaiveBayesClassifier()
    path = Path("classifier") / "TRAINING-DATA" / "BBC News Summary" / "News Articles"
    data_art = load_dataset(path)

    path = Path("classifier") / "TRAINING-DATA" / "BBC News Summary" / "Summaries"
    data_sum = load_dataset(path)
    
    dataset = data_art + data_sum

    classifier.train(data=dataset)

    category = classifier.predict(text=data.texto)

    return {
        "text": data.texto,
        "category": category,
    }
