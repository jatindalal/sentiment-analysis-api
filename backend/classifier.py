import pickle
from process_text import Preprocessor

class Classifier:
    def __init__(self) -> None:
        # load model and vectorizer
        self.model = pickle.load(open("models/classifier.pkl", "rb"))
        self.vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

    def classify(self, text):
        # Preprocess given string
        sentences = [text]
        preprocessor = Preprocessor()
        processed_text = preprocessor.preprocess(sentences)

        # Vectorize the text and infer the output
        vectorized_text = self.vectorizer.transform(processed_text)
        prediction = self.model.predict(vectorized_text)

        return prediction[0]

