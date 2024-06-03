FROM debian:stable-slim
COPY main.py main.py
COPY books/ books/
RUN apt update
RUN apt upgrade -y
RUN apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
RUN wget https://www.python.org/ftp/python/3.12.3/Python-3.12.3.tgz
RUN tar -xf Python-3.12.*.tgz
RUN cd Python-3.12.3 && ./configure --enable-optimizations && make && make altinstall
CMD ["python3.12", "main.py"]

