#partindo da imagem Ubuntu
FROM ubuntu:latest
#run um comando shell script o -y é para que ele responda 
#y quando perguntar se quiser instalar sem parar a execução 
# \ para quebrar a linha no shell script
RUN apt-get update && apt-get install python3-pip -y \
    && apt-get install nano -y


# essa pasta está dentro del container. quando o container é deletado então todo é deletado
RUN mkdir /nova-pasta    
#Ao iniciar o container, o mesmo 
ENTRYPOINT ["/bin/bash"] 

#isso aqui se executa no terminal na pasta onde está o archivo
#docker build -t minha-imagem .

#docker run --name mi -it minha-imagem para fazer o run e ele corre uma consola ai, para sair: exit