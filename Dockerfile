# Use an official Python runtime as the base image
FROM python:3.11-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . /app

# Expose the port on which the Flask app runs
# EXPOSE 5000

# Run the Python application
CMD [ "python", "project.py" ]
