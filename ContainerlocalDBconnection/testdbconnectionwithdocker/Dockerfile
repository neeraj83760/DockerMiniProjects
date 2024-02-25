# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

RUN pip install pymysql

# Make port 3306 available to the world outside this container
EXPOSE 3306

#
CMD ["python", "./app.py"]
