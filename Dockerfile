FROM python:3.7-alpine
MAINTAINER Kyle Harrison <kyle90adam@hotmail.com>

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# install build/runtime dependencies inside the container
RUN pip install --no-cache-dir pipenv

# install language-level dependencies inside the container
COPY Pipfile Pipfile.lock /usr/src/app/
RUN pipenv install --deploy --dev --ignore-pipfile --system

# copy the application source into the container
COPY . /usr/src/app
