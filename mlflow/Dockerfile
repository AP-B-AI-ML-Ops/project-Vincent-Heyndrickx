FROM python:3.11-slim

RUN pip install mlflow psycopg2-binary

EXPOSE 5000

CMD ["mlflow", "server", "--host", "0.0.0.0","--port", "5000","--backend-store-uri", "postgresql://postgres:postgres@postgres:5432/mlflow_db","--default-artifact-root", "file:/mlflow-artifacts"]