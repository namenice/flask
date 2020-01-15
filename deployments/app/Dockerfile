FROM python:3.7
ADD app/ /app
WORKDIR /app
RUN apt-get update
RUN pip install -r requirements.txt

CMD python app.py
