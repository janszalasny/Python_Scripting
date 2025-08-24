Polish Football Chatbot
======================
--------------------------------

This project is  chatbot built with pure Python. It has been customized to act as a "Polish Football FanBot," capable of answering questions about Polish football clubs, history, and players. The core goal of this project is to showcase a strong understanding of Object-Oriented Programming (OOP), design patterns, and modern software development practices.

### Key Features

-   **Specialized Knowledge:** The chatbot is an expert on Polish football, with its knowledge base easily editable in a simple JSON file.

-   **OOP Architecture:** The codebase is highly modular and follows OOP principles, with a clear separation of concerns between the GUI, NLP processing, and response generation.

-   **Strategy Design Pattern:** The project uses the Strategy design pattern, allowing for interchangeable NLP (Natural Language Processing) backends. The current implementation uses the powerful spaCy library.

-   **Tkinter GUI:** A clean and simple graphical user interface is provided using Python's built-in Tkinter library for a native desktop experience.

-   **Containerized with Docker:** A `Dockerfile` is included to demonstrate the ability to containerize the application for easy deployment and portability across any environment.

-   **Extensible Knowledge Base:** The chatbot's knowledge is stored in `data/intents.json`. This file can be easily updated to expand the bot's expertise without changing a single line of Python code.

### Project Structure

The project is organized into a clean and scalable structure:

```
PolishFootballFanBot/
├── app/
│   ├── chatbot.py         # Core chatbot logic
│   ├── gui.py             # Tkinter GUI implementation
│   └── nlp/
│       ├── processor.py     # Abstract base class for NLP (Strategy Pattern)
│       └── spacy_processor.py # Concrete spaCy implementation
│   └── responses/
│       └── generator.py     # Handles response generation
├── data/
│   └── intents.json       # The chatbot's knowledge base
├── main.py                # Main entry point for the application
├── requirements.txt       # Python dependencies
└── Dockerfile             # Docker configuration

```

### How to Run

You can run this application either locally on your machine or within a Docker container.

#### 1\. Local Development

1.  **Clone the repository:**

    ```
    git clone <repository-url>
    cd PolishFootballFanBot

    ```

2.  **Create and activate a virtual environment:**

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    ```

3.  **Install dependencies:**

    ```
    pip install -r requirements.txt

    ```

4.  **Download the spaCy language model:**

    ```
    python -m spacy download en_core_web_sm

    ```

5.  **Run the application:**

    ```
    python main.py

    ```

#### 2\. Using Docker

1.  **Build the Docker image:**

    ```
    docker build -t football-fanbot .

    ```

2.  **Run the Docker container:**  *Note: Running a GUI application in Docker requires sharing your host's display with the container.*

    -   **On Linux:**

        ```
        docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix football-fanbot

        ```

    -   **On macOS (requires XQuartz):**

        ```
        docker run -it --rm -e DISPLAY=docker.for.mac.host.internal:0 football-fanbot

        ```

### Customization

To add more questions and answers or to change the chatbot's topic entirely, simply edit the `data/intents.json` file. The file follows a simple structure:

-   **tag:** A unique identifier for a category of questions.

-   **patterns:** A list of example phrases or questions a user might ask. The more examples you provide, the better the bot will understand.

-   **responses:** A list of possible answers the bot can give. It will choose one at random.

```
{
  "intents": [
    {
      "tag": "domestic_cups",
      "patterns": ["Polish domestic football cups", "History of Polish Cup", "Polish Cup winners"],
      "responses": ["The Polish Cup (Puchar Polski) is a national knockout competition. Clubs like Legia Warsaw, Lech Poznań, and Wisła Kraków have won it multiple times."]
    },
  ]
}

```