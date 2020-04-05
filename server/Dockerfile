FROM python:3.6

EXPOSE 8000

WORKDIR /server

COPY requirements.txt /server
RUN pip3 install -r requirements.txt

COPY server.py /server
CMD python3 server.py
