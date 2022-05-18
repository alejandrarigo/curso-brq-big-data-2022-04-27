FROM python:3.9

RUN pip install mysql-connector-python pandas 
#copia todos os archivos da pasta do SO para dentro do container
COPY . .

CMD ["miniproject.py"]
#no container que fique o console aberto para nos em python
ENTRYPOINT ["python"]
