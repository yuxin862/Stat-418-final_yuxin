# Use Python 3.10 slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Upgrade pip and install requirements
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# Expose port (Cloud Run default is 8080)
EXPOSE 8080

# Set entrypoint to run Flask app
CMD ["python", "app.py"]
