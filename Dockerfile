FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt requirements-dev.txt /code/
RUN pip install -r requirements-dev.txt
ADD . /code/
