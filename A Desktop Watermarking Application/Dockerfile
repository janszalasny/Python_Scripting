# Use a slim Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies required for Tkinter and GUI applications
# This is crucial for running a GUI app in a Linux-based container
RUN apt-get update && apt-get install -y \
    tk \
    tcl \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project source code and assets into the container
COPY src/ ./src
COPY assets/ ./assets

# Set the DISPLAY environment variable. This tells the GUI library inside the
# container where to send its drawing commands (i.e., to the host's display).
# This variable will be overridden by the docker run command.
ENV DISPLAY=:0

# Command to run the application when the container starts
CMD ["python", "src/main.py"]