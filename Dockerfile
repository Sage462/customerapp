<<<<<<< HEAD
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python","app/app.py"]
=======
ROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python","app/app.py"]
>>>>>>> 82c0ee0aa98f2cd0823946b1a8e0b3f1dd295783
