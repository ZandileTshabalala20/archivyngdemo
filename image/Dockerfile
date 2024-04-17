# Use Python 3.11.5 as base image
FROM python:3.11.5

# Update package lists
RUN apt-get update && apt-get install -y python3-pip

# Install Flask
RUN pip3 install Flask

# Set the working directory in the container
WORKDIR /app

# Copy application files from the host to the container
COPY . .

# Command to run the Flask application
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]