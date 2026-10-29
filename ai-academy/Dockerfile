FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir fastapi==0.115.12 uvicorn==0.34.2
COPY ai-academy/labs /app/labs
COPY ai-academy/data /app/data
RUN useradd --create-home learner
USER learner
ENV PYTHONPATH=/app/labs
EXPOSE 8000
CMD ["python", "-m", "uvicorn", "api:app", "--app-dir", "/app/labs", "--host", "0.0.0.0", "--port", "8000"]
