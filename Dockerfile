# Use official Python slim image
FROM python:3.9-slim

# Set environment variables for clean and optimized installs
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (if needed for MySQL clients)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libmariadb-dev \
 && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the codebase
COPY . .

# Overwrite app.py with Docker-specific version
COPY app_docker.py app.py

# Set default environment variables (can be overridden)
ENV MYSQL_HOST=localhost \
    MYSQL_USER=flaskuser \
    MYSQL_PASSWORD=your_password_here \
    MYSQL_PORT=3306

# Expose the app's port
EXPOSE 5000

# Set the entry point to Python running your app
ENTRYPOINT ["python", "app.py"]

# Default arguments (can be overridden at runtime)
CMD ["--host=0.0.0.0"]
