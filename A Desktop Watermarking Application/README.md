A Desktop Watermarking Application
==================================

This is a desktop GUI application built with Python for applying text and image-based watermarks to images. It features a clean, modern interface and a flexible, object-oriented architecture designed for scalability. The entire application is containerized with Docker, allowing it to run consistently in any environment.

* * * * *

Key Features
------------

-   **Dual Watermark Modes**: Seamlessly switch between applying text or image-based watermarks.

-   **Real-time Preview**: Instantly view the applied watermark on the base image before saving.

-   **Rich Customization**:

    -   Adjust the watermark's opacity with a simple slider.

    -   Choose from nine distinct positions on the image (e.g., top-left, center, bottom-right).

    -   Select custom colors for text watermarks.

    -   Scale image watermarks relative to the size of the base image.

-   **Modern UI**: Built using the CustomTkinter library for a professional and contemporary look and feel.

-   **Containerized Deployment**: Includes a `Dockerfile` for easy and repeatable deployment, demonstrating modern software engineering practices.

* * * * *

Technical Architecture and Design
---------------------------------

This project was built with a strong emphasis on clean code, scalability, and professional software design patterns.

### Core Technologies

-   **Python 3.10+**

-   **CustomTkinter**: For the graphical user interface.

-   **Pillow (PIL Fork)**: For all backend image processing and manipulation tasks.

-   **Docker**: For containerization of the application.

### Object-Oriented Programming (OOP)

The application is architected using OOP principles to ensure a clear separation of concerns:

-   **`App`**: The main GUI class that handles the user interface, event handling, and state management.

-   **`ImageProcessor`**: A backend class responsible for loading, processing, and saving images. It acts as the context for the Strategy pattern.

-   **`WatermarkStrategy`**: An abstract base class defining the interface for all watermarking algorithms. This promotes polymorphism and modularity.

-   **`ConfigManager`**: A Singleton class that provides a centralized point of access for application-wide settings.

### Design Patterns Implemented

Two key design patterns were implemented to enhance the application's structure and flexibility:

1.  **Strategy Pattern**: This pattern is central to the application's design. It allows the watermarking algorithm to be selected and changed at runtime.

    -   **Why**: To decouple the `ImageProcessor` from the specific implementation details of how a watermark is applied. This makes it easy to add new watermark types (e.g., tiled, diagonal) in the future without modifying the existing `ImageProcessor` or GUI code.

    -   **How**: An abstract `WatermarkStrategy` class defines a common `apply` method. Concrete classes like `TextWatermarkStrategy` and `ImageWatermarkStrategy` provide specific implementations for that method. The `ImageProcessor` is configured with one of these strategy objects to perform the watermarking task.

2.  **Singleton Pattern**: The `ConfigManager` class is implemented as a Singleton.

    -   **Why**: To ensure that there is only one instance of the configuration object throughout the application's lifecycle. This provides a global, consistent point of access to settings like default fonts, colors, and paths.

    -   **How**: A generic `SingletonMeta` metaclass is used, ensuring a thread-safe, single-instance creation logic that can be applied to any class.

* * * * *

Project Structure
-----------------

The codebase is organized into a modular structure to separate concerns and improve maintainability.

```
AquaMark/
├── assets/
│   └── fonts/
│       └── Roboto-Bold.ttf
├── src/
│   ├── app/
│   │   └── gui.py
│   ├── core/
│   │   ├── image_processor.py
│   │   └── watermark_strategies.py
│   ├── patterns/
│   │   └── singleton.py
│   ├── utils/
│   │   └── config.py
│   └── main.py
├── Dockerfile
└── requirements.txt

```

* * * * *

Setup and Installation
----------------------

You can run the application either locally using a Python virtual environment or within a Docker container.

### 1\. Local Environment Setup

1.  **Clone the repository**:

    Bash

    ```
    git clone <repository_url>
    cd AquaMark

    ```

2.  **Create and activate a virtual environment**:

    Bash

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    ```

3.  **Install the required dependencies**:

    Bash

    ```
    pip install -r requirements.txt

    ```

4.  **Run the application**:

    Bash

    ```
    python src/main.py

    ```

### 2\. Running with Docker

Running a GUI application in Docker requires forwarding the host's display server.

1.  **Build the Docker image**:

    Bash

    ```
    docker build -t aquamark-app .

    ```

2.  **Run the container** (command varies by OS):

    -   **On Linux**:

        Bash

        ```
        docker run --rm -it\
               -e DISPLAY=$DISPLAY\
               -v /tmp/.X11-unix:/tmp/.X11-unix\
               aquamark-app

        ```

    -   **On macOS** (Requires XQuartz to be installed and running):

        Bash

        ```
        # First, allow connections from network clients in XQuartz
        # Then, run the container:
        docker run --rm -it -e DISPLAY=host.docker.internal:0 aquamark-app

        ```

    -   **On Windows** (Requires an X Server like VcXsrv to be installed and running):

        Bash

        ```
        # First, launch VcXsrv with access control disabled
        # Then, run the container:
        docker run --rm -it -e DISPLAY=host.docker.internal:0.0 aquamark-app
        ```


<img width="1194" height="790" alt="Image" src="https://github.com/user-attachments/assets/9e2052f7-8abb-4269-975f-49a7e15dc80f" />

