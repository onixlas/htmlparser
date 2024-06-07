FROM dh-mirror.gitverse.ru/library/python:3.10

WORKDIR /app

COPY requirements.txt app.py /app/
RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]
