FROM python:3.6

EXPOSE 5000

WORKDIR /client

COPY requirements.txt /client
RUN pip3 install -r requirements.txt

COPY app.py /client
CMD python3 app.py

