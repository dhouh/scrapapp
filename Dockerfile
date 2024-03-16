# Use the official Python image as base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the parent directory into the container
COPY .. .

# Install MongoDB and FastAPI dependencies
RUN apt-get update && apt-get install -y docker.io
RUN pip install -r requirements.txt

# Expose the port that your FastAPI app is running on
EXPOSE 8000

# Command to run the FastAPI application and MongoDB service
CMD service mongod start && uvicorn main:app --host 0.0.0.0 --port 8000



