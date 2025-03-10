FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY backend/ ./backend/
COPY frontend/ ./frontend/

EXPOSE 8000
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t canastae-python:1.0.0 .
# docker run -d -p 8000:8000 --name canastae-python canastae-python:1.0.0

# all:
# docker build -t canastae-python:1.0.0 . && docker rm -f canastae-python && docker run -d -p 8000:8000 --name canastae-python canastae-python:1.0.0
 