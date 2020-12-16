# base image
FROM python:3.7

# add files from your current directory
COPY . /app

# set workdir
WORKDIR /app

# run some bash command
RUN pip install -r requirements.txt

# port number the container should expose to outside
EXPOSE 5000

# run the application
ENTRYPOINT python run.py
