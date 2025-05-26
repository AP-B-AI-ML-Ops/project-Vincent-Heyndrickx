FROM python:3.11-slim

RUN pip install --upgrade pip setuptools wheel

WORKDIR /opt/orchestration

COPY prefect_server.yaml ./

RUN pip install prefect pendulum

#Juiste poort zetten, prefect server geeft anders problemen
RUN prefect config set PREFECT_API_URL="http://localhost:4200/api"

EXPOSE 4200

CMD ["prefect", "server", "start", "--host", "0.0.0.0", "--port", "4200"]
