FROM python:3.12


RUN apt-get update && apt-get install -y make

RUN mkdir /recipe_bot

COPY . /recipe_bot
WORKDIR /recipe_bot

# Through makefile
CMD make run_as_script
