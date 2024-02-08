FROM python:3.12


RUN apt-get update && apt-get install -y make

RUN mkdir /recipe_bot

COPY . /recipe_bot
WORKDIR /recipe_bot

RUN chmod 777 entry.sh

# Through makefile
CMD sh entry.sh
