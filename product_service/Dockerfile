FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*
COPY pyproject.toml ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
    "fastapi>=0.136.1,<0.137.0" \
    "uvicorn[standard]>=0.46.0,<0.47.0" \
    "httpx>=0.28.1,<0.29.0"
COPY src/app ./app
EXPOSE 8001
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
