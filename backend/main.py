from typing import Union
from fastapi import FastAPI
from classifier import Classifier
import uvicorn

app = FastAPI(title="Sentiment Analysis API",
              description="API to predict sentiment of given text",
              version="1.0")

@app.on_event('startup')
def load_classifier():
    global clf
    clf = Classifier()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment Analysis API"}

@app.get("/api")
def root(text: Union[str, None] = None):
    prediction = clf.classify(text)
    
    return {"sentiment": prediction}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)