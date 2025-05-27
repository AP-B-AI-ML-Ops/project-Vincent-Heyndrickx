FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

RUN prefect config set PREFECT_API_URL=http://orchestration:4200/api
RUN chmod +x start_workers.sh

CMD ["bash", "start_workers.sh"]