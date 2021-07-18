FROM python:3.6.14-buster

WORKDIR /

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY / .

CMD ["python", "rain-or-shine.py"]