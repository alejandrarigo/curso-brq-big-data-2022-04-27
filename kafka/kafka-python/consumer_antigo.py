from kafka import KafkaConsumer

from json import loads

consumer= KafkaConsumer(
    'meu-topico-legal',
    bootstrap_servers=['localhost:9092'],
    value_deserializer= lambda x: loads( x.decode('utf-8') )
)

sum=0
i=0
for msg in consumer:
    i+=
    sum+=msg.value
    media=sum/i
    print("A media é:",media)
    print(msg.value)
    