import json
import random

class ResponseGenerator:
    """
    A class to generate responses based on the identified intent.
    """
    def __init__(self):
        """
        Initializes the ResponseGenerator and loads the intents.
        """
        with open('data/intents.json', 'r') as f:
            self.intents = json.load(f)

    def generate_response(self, intent_tag):
        """
        Generates a random response for a given intent tag.

        :param intent_tag: The tag of the intent.
        :return: A response string.
        """
        for intent in self.intents["intents"]:
            if intent["tag"] == intent_tag:
                return random.choice(intent["responses"])
        return "I'm not sure how to respond to that. Can you ask me something else about Python?"
