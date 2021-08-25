# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /my_app

# copy the dependencies file to the working directory
COPY requirements.txt .

# set env variables
ENV MONGO_USERNAME=""
ENV MONGO_PASSWORD=""
ENV MONGO_DB_NAME=""
ENV MONGO_DB_IP=""


# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY / .

# command to run on container start
CMD [ "gunicorn", "run:app", "-w", "2", "--threads", "2", "-b", "0.0.0.0:8000" ]