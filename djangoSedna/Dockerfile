FROM python:2.7
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:1234"]

WORKDIR /app/sednafiles/sedna/bin

CMD [se_gov]
CMD [se_sm sdb]