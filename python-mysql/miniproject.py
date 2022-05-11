#executa comando de mysql desde python
import mysql.connector
db=mysql.connector.connect(host='mydb',user='root', 
    password='root',port=3306)# ṕara criar uma coneção com o banco de dados esse é o IP do container do mysql

my_cursor=db.cursor()
my_cursor.execute('DROP database IF EXISTS brq') #deleta o banco se existe
my_cursor.execute('CREATE DATABASE IF NOT EXISTS brq_python') #cria esse novo banco de dados SE NÃO EXISTE
my_cursor.execute('USE brq_python')
my_cursor.execute('CREATE TABLE IF NOT EXISTS feras_brq( nome varchar(255), email varchar(255))')
my_cursor.execute('INSERT INTO feras_brq (nome,email) VALUES ("Joao", "j@j.com" )')

#para commitar o banco de datos e funcionar tudo
db.commit()
#para fechar a coneção depois de fazer
my_cursor.close()