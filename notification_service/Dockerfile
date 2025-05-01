FROM python:3.11-slim
WORKDIR /app
COPY app /app
RUN pip install flask flask_sqlalchemy kafka-python pyodbc
CMD ["flask", "run", "--host=0.0.0.0", "--port=5002"]
