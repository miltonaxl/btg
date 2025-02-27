# Use AWS Lambda's Python base image for better compatibility
FROM public.ecr.aws/lambda/python:3.11 as base

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables for AWS Lambda (Port 8080 is required)
ENV PORT=8080

# Expose the correct port for AWS
EXPOSE 8080

# Define Lambda handler
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
