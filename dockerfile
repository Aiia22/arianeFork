# Use a Python runtime matching the Django requirement
FROM python:3.10-slim

# Set environment variables to prevent Python from writing pyc files to disc (optional) and buffer stdout and stderr (important)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /ariane

# Install dependencies
COPY requirements.txt /ariane/
RUN pip install -r requirements.txt

# Copy the rest of your project
COPY . /ariane/
