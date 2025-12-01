FROM ubuntu:22.04
RUN apt update && apt install -y python3 python3-pip
WORKDIR /app
COPY . /app
EXPOSE 8080
CMD ["python3", "-u", "api_server.py"]
