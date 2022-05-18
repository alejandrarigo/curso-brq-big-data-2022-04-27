from kafka import KafkaConsumer
from json import loads
import mysql.connector

con=mysql.connector.connect(host='mysql',user='root', 
    password='root',port=3306,database='brq_python')# ṕara criar uma coneção com o banco de dados esse é o IP do container do mysql
my_cursor=con.cursor()
my_cursor.execute('CREATE TABLE IF NOT EXISTS nova_tabela( valores int, madia decimal(6,2))')

consumer= KafkaConsumer(
    'meu-topico-legal',
    bootstrap_servers=['singlenode_kafka_1:29092'],#ip da rede single_node
    value_deserializer= lambda x: loads( x.decode('utf-8') )
)

sum=0
cont=0
try: 
    for msg in consumer:
        cont+=1
        sum+=msg.value
        media=sum/cont
        valor=msg.value
        insert='Insert into nova_tabela(valores,madia) values ({},{})'.format(valor,media)
        #'Insert into nova_tabela(valores,madia) values ({valor},{media})'da ppppara poner asi
        my_cursor.execute(insert)
        con.commit()
except KeyboardInterrupt:
    print('Fechando a conexão')
    my_cursor.close() #é muito importante fechar a conexão para outros usar o banco