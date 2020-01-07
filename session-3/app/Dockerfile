FROM python:3.6

WORKDIR /app
COPY app.py /app/app.py

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV FLASK_APP /app/app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 5000

CMD flask run