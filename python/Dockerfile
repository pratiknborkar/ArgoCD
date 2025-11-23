# Use an official slim Python image
FROM python:3.11-slim

# Create and use app directory
WORKDIR /app

# Install system deps (if any) and upgrade pip
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python deps
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY . .

# Expose port
EXPOSE 8080

# Use a non-root user (optional, but nicer)
RUN useradd --create-home appuser
USER appuser

# Run with gunicorn for production-like behavior
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app", "--workers", "2", "--threads", "4", "--timeout", "120"]
