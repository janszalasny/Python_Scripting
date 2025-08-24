# AdWords Keyword Dynamo

AdWords Keyword Dynamo is a Python-based tool for generating Google Ads keywords from a base set of terms. It's designed to be modular, scalable, and easy to use, leveraging common software design patterns to ensure flexibility and maintainability.

## Features

* **Multiple Match Types**: Generate keywords for Broad, Phrase, and Exact match types.
* **Flexible Output**: Save generated keywords to a CSV file or print them to the console.
* **Extensible**: Easily add new keyword generation strategies or output formats.
* **Containerized**: Includes a Dockerfile for easy setup and deployment in any environment.

## Project Structure

The project is organized into a clear and scalable structure:

```bash
git clone <repository-url>
│
├── src/
│   ├── keyword_generator/
│   │   ├── __init__.py
│   │   ├── generator.py      # Core generator logic
│   │   ├── strategies.py     # Keyword generation strategies
│   │   └── observers.py      # Output savers (observers)
│   │
│   └── main.py               # Main execution script
│
├── data/
│   └── generated_keywords.csv # Output file
│
├── Dockerfile
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

* Python 3.8+
* Docker (for containerized execution)

### Installation

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2.  Navigate to the project directory:
    ```bash
    cd adwords_keyword_dynamo
    ```
3.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

#### Locally

To run the keyword generator locally, execute the `main.py` script:

```bash
python src/main.py
```

## Design Patterns Used
This project utilizes two key design patterns:

- Factory Pattern: The StrategyFactory class is used to create different keyword generation strategy objects (BroadMatchStrategy, PhraseMatchStrategy, etc.) without exposing the creation logic to the client.

- Observer Pattern: The KeywordGenerator acts as the "subject," and the CsvKeywordSaver and ConsoleKeywordSaver act as "observers." When the generator creates new keywords, it notifies all attached observers, which then handle the output accordingly. This decouples the keyword generation logic from the output logic.