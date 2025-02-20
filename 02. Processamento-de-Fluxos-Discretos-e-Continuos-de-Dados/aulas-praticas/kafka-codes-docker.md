# Códigos para ativar e usar o Kafka via Docker

O docker deve estar iniciado e o container do Kafka sendo executado.

## Criando o(s) tópico(s)
1. `docker exec -it kafka bash` - **O terminal executa e entra na máquina do Kafka**  
2. `cd /opt/kafka/bin/` - **acessar o diretório com os shellscripts para a manipulação do Kafka**
3. `./kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic aula` - **Cria um tópico com o nome 'aula'** *(pode criar quantos tópicos quiser, sendo necessário mudar apenas o nome no final)*
4. `./kafka-topics.sh --list --zookeeper zookeeper:2181` - **Lista todos os tópicos criados no kafka**
5. `./kafka-topics.sh --describe --zookeeper zookeeper:2181 --topic aula` - **Obtêm a descrição do tópico apontado apontado**
   
## Criando o(s) Producer(s)
Com o tópico criado agora podemos enviar mensagem ao Kafka

1. `./kafka-console-producer.sh --brocker-list kafka:9092 --topic aula`