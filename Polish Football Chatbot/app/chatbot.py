from app.nlp.spacy_processor import SpacyProcessor
from app.responses.generator import ResponseGenerator

class ChatBot:
    """
    The main ChatBot class that orchestrates the conversation.
    """
    def __init__(self):
        """
        Initializes the ChatBot with an NLP processor and a response generator.
        """
        self.nlp_processor = SpacyProcessor()
        self.response_generator = ResponseGenerator()

    def get_response(self, user_input):
        """
        Gets a response from the chatbot for a given user input.

        :param user_input: The user's message.
        :return: The chatbot's response.
        """
        intent = self.nlp_processor.process(user_input)
        return self.response_generator.generate_response(intent)
