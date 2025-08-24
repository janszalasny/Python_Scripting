"""
AdWords Keyword Dynamo: Main execution script.

This script demonstrates the use of the keyword generator by:
1. Defining a base set of keywords and modifiers.
2. Creating a KeywordGenerator instance.
3. Creating a factory for keyword generation strategies.
4. Attaching observers to save the generated keywords.
5. Generating keywords using different strategies.
"""

import pandas as pd
from keyword_generator.generator import KeywordGenerator, StrategyFactory
from keyword_generator.observers import CsvKeywordSaver, ConsoleKeywordSaver


def main():
    """
    Main function to run the AdWords Keyword Dynamo.
    """
    # Base keywords and modifiers
    products = ['digital camera', 'dslr camera', 'mirrorless camera']
    modifiers = ['buy', 'best', 'cheap', 'for sale', 'review']

    # Create a KeywordGenerator instance
    keyword_generator = KeywordGenerator(products, modifiers)

    # Create a factory for keyword generation strategies
    strategy_factory = StrategyFactory()

    # Create observers to save the generated keywords
    csv_saver = CsvKeywordSaver('data/generated_keywords.csv')
    console_saver = ConsoleKeywordSaver()

    # Attach observers to the keyword generator
    keyword_generator.attach(csv_saver)
    keyword_generator.attach(console_saver)

    # Generate keywords using different strategies
    print("--- Generating Broad Match Keywords ---")
    broad_match_strategy = strategy_factory.create_strategy('broad')
    keyword_generator.set_strategy(broad_match_strategy)
    keyword_generator.generate_keywords()

    print("\n--- Generating Phrase Match Keywords ---")
    phrase_match_strategy = strategy_factory.create_strategy('phrase')
    keyword_generator.set_strategy(phrase_match_strategy)
    keyword_generator.generate_keywords()

    print("\n--- Generating Exact Match Keywords ---")
    exact_match_strategy = strategy_factory.create_strategy('exact')
    keyword_generator.set_strategy(exact_match_strategy)
    keyword_generator.generate_keywords()

    # You can also generate keywords for a new set of products and modifiers
    print("\n--- Generating Keywords for a New Product Set ---")
    new_products = ['4k tv', 'led tv', 'smart tv']
    new_modifiers = ['deals', 'offers', 'discount']
    keyword_generator.products = new_products
    keyword_generator.modifiers = new_modifiers
    keyword_generator.set_strategy(broad_match_strategy)
    keyword_generator.generate_keywords()


if __name__ == "__main__":
    main()
