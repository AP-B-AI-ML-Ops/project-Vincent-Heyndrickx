FROM python:3.11-slim

WORKDIR /api

COPY ["requirements.txt", "app.py", "./"]

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "app.py"]