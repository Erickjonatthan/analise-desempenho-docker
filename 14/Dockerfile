FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3
WORKDIR /app
COPY process.py .
CMD ["python3", "process.py"]