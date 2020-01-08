FROM python:3.6

WORKDIR /app
COPY requirements.txt requirements.txt
COPY data.csv /data/data.csv
RUN pip install -r requirements.txt

COPY train.py train.py

CMD python train.py