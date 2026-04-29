FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt


COPY . .

RUN mkdir -p /var/log


CMD ["python","app.py"]



