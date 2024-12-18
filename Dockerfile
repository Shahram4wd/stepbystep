# Base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY . /app/

# Collect static files
#RUN python manage.py collectstatic --no-input

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["gunicorn", "agilemetrics.wsgi:application", "--bind", "0.0.0.0:8000"]
