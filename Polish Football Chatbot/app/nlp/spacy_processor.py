import spacy
import json
from app.nlp.processor import NLPProcessor

class SpacyProcessor(NLPProcessor):
    """
    An NLP processor that uses the spaCy library.
    """
    def __init__(self, model="en_core_web_sm"):
        """
        Initializes the SpacyProcessor.

        :param model: The spaCy model to use.
        """
        self.nlp = spacy.load(model)
        with open('data/intents.json', 'r') as f:
            self.intents = json.load(f)

    def process(self, text):
        """
        Processes the user input to find the best matching intent.

        :param text: The user's input text.
        :return: The tag of the best matching intent.
        """
        doc = self.nlp(text.lower())
        best_match = {"tag": "default", "score": 0.0}

        for intent in self.intents["intents"]:
            for pattern in intent["patterns"]:
                pattern_doc = self.nlp(pattern.lower())
                similarity = doc.similarity(pattern_doc)
                if similarity > best_match["score"]:
                    best_match["score"] = similarity
                    best_match["tag"] = intent["tag"]

        if best_match["score"] > 0.7:  # Confidence threshold
            return best_match["tag"]
        else:
            return "default"
