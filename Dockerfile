FROM python:3.9-alpine
MAINTAINER Riddam Jain

ENV PYTHONUNBUFFERED=1


COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./app /app
WORKDIR /app


COPY runner.sh runner.sh
RUN chmod +x runner.sh





CMD ["/bin/sh", "runner.sh"]