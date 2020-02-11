# Buster base image that contains python 3.7
FROM python:3.7-buster

#person in charge/author
MAINTAINER Yacine Boukhelif b.yacine.pro@gmail.com

# define the directory to work in
WORKDIR /app

# copy the requirements.txt file to the work directory
COPY requirements.txt .

# Install some system deps in a virtual environment named .build-deps

# install pip dependencies in the same layer

RUN  pip install -r requirements.txt

# copy rest of the source code
COPY main.py /app
COPY settings.py /app
COPY SparseArray.py /app
COPY utils.py /app

#COPY ../logs/app.log /app
RUN mkdir /app/logs
RUN touch /app/logs/app.log


# EXPOSE the needed ports
#EXPOSE 0.0.0.0:5000:5000

#set ENV for STRINGS
ENV STRINGS "ab,ab,abc,abc,abc,abc"

# Running Command or Entry Point
ENTRYPOINT ["python", "main.py"]