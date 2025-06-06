FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set environment variables for MySQL connection (these will be overridden at runtime)
ENV MYSQL_HOST=localhost \
    MYSQL_USER=flaskuser \
    MYSQL_PASSWORD=your_password_here \
    MYSQL_PORT=3306

# Copy the Docker-ready app.py
COPY app_docker.py app.py

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]