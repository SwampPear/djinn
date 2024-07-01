# Use an existing base image
FROM ubuntu:latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update packages and install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt --break-system-packages

# Copy your application code into the container
COPY . .

# Expose the port on which your Flask app runs (default is 5000)
EXPOSE 5000

# Specify the command to run when the container starts
CMD ["python", "djinn.py"]
