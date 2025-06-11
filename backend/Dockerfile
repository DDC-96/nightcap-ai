# backend/Dockerfile

FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app/backend

# Copy the dependcies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt 

# Copy the contenr of the local src directory to the working directory
COPY . .

# Run the application
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]