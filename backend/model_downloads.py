import gdown

classifier = "models/classifier.pkl"
vectorizer = "models/vectorizer.pkl"

classifier_id = "1d2shVZlp8Qnb7P4hqGFtZgxzVNiyNZX9"
vectorizer_id = "1NON2Q6PJ-vQ0qbQRKIHr-89LC-ucttKV"

gdown.download(id=classifier_id, output=classifier, quiet=False)
gdown.download(id=vectorizer_id, output=vectorizer, quiet=False)