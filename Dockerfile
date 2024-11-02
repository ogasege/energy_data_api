# Use the appropriate base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Command to run your FastAPI app (adjust according to your app structure)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]