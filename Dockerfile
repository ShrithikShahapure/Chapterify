# Use Ubuntu as the base image
FROM ubuntu:latest

# Set the working directory inside the container
WORKDIR /app

# Install Python 3 and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip3 install -r requirements.txt

# Copy all files and folders from the current directory to the container
COPY . /app

# Expose port 8051 for running web applications
EXPOSE 8051


# Run the Streamlit application
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
