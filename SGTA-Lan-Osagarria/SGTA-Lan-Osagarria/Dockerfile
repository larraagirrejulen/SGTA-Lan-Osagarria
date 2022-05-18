FROM python:3.7-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements1.txt requirements1.txt
RUN pip3 install -r requirements1.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]