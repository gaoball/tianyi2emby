FROM python:3.11-slim

WORKDIR /app

COPY ./app /app

RUN apt-get update && apt-get install -y curl unzip libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1 libxss1 libgtk-3-0 && \
    pip install -r requirements.txt && \
    python -m playwright install --with-deps

EXPOSE 8000
EXPOSE 8060
CMD ["python", "main.py"]