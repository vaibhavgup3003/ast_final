## Use an official Python image from the Docker Hub
#FROM python:3.9-slim
#
## Set the working directory in the container
#WORKDIR /app
#
## Copy the Python requirements file
#COPY requirements.txt requirements.txt
#
## Install any needed packages specified in requirements.txt
#RUN pip3 install --no-cache-dir -r requirements.txt
#
## Copy the rest of the application code
#COPY . .
#
## Expose the port the app runs on (adjust if necessary)
#EXPOSE 5000
#
## Command to run the server
#CMD ["python", "server/server.py"]
#
## Optionally: add a stage to run tests
## RUN python -m unittest discover unit_tests


# Use an official Python runtime as a parent image
FROM python:3.12.7

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install the dependencies specified in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port the server will run on
EXPOSE 5000

# Command to run the server (assumes `server.py` starts the application)
CMD ["python", "server/server.py"]




