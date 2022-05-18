FROM python:3.9

RUN pip install mysql-connector-python pandas json kafka-python

COPY . .

CMD ["consumer_v2.py"]
#CMD ["sleep 5"]
#CMD ["producer.py"]
#no container que fique o console aberto para nos em python
ENTRYPOINT ["python"]
