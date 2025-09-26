FROM python:3.13.2-alpine3.21

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYDEVD_DISABLE_FILE_VALIDATION=1

# Install netcat for postgres health check
RUN apk add --no-cache netcat-openbsd

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/entrypoint.sh .
RUN chmod +x entrypoint.sh

EXPOSE 8000
EXPOSE 5678
EXPOSE 5679

CMD ["sh", "entrypoint.sh"]