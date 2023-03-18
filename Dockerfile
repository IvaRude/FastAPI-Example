FROM snakepacker/python:3.11

# install system-wide deps for python and node
RUN apt-get -yqq update
RUN apt-get -yqq install python3-pip
RUN pip install --upgrade pip

WORKDIR /app
# copy our application code
COPY . .
RUN pip install -r requirements.txt

# expose port
EXPOSE 8000

# start app
CMD [ "python3", "main.py" ]