# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
# (Even though this is a GUI app, this is good practice for other apps)
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
# Note: For a GUI app, you'd typically need an X server,
# but this Dockerfile is for demonstration of containerization.
# To run a GUI app in Docker, you would need to mount the X11 socket.
# For example:
# docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix chatbot-app
CMD ["python", "main.py"]
