FROM python:3.8

WORKDIR /fastapi-app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY main.py main.py

CMD ["uvicorn", "main:app" , "--reload", "--host=0.0.0.0"]