# Códigos para ativar e usar o Kafka via Docker

## Primeiros passos:

1. Ligar o Docker Desktop
2. Subir o containet do Kafka para o Docker, com o código:
`docker compose up -d kafka`

O docker deve estar iniciado e o container do Kafka sendo executado para seguir os demais tópicos.

## Criando o(s) tópico(s)
1. `docker exec -it kafka bash` - **O terminal executa e entra na máquina do Kafka**  
2. `cd /opt/kafka/bin/` - **acessar o diretório com os shellscripts para a manipulação do Kafka**   

    (*Digite `ls` no terminal após a execução do código 2., para garantir que encontrou no diretório **bin** do kafka*)  
    📌  
    ![Arquitetura Kafka](https://raw.githubusercontent.com/vbs-matheus/PosGraduacao-EngDados/refs/heads/main/02.%20Processamento-de-Fluxos-Discretos-e-Continuos-de-Dados/imgs/diretorio-bin_kafka.png)
3. `./kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic aula` - **Cria um tópico com o nome 'aula'** *(pode criar quantos tópicos quiser, sendo necessário mudar apenas o nome no final)*
4. `./kafka-topics.sh --list --zookeeper zookeeper:2181` - **Lista todos os tópicos criados no kafka**
5. `./kafka-topics.sh --describe --zookeeper zookeeper:2181 --topic aula` - **Obtêm a descrição do tópico apontado**
   
## Criando o(s) Producer(s)
Com o tópico criado agora podemos enviar mensagem ao Kafka

1. `./kafka-console-producer.sh --broker-list kafka:9092 --topic aula`  
    Após esse comando o kafka ficará aguardando o envio de mensagens, que podem ser consultadas.    
   1.1 `cd /kafka/kafka-logs-kafka/` - **Acessa o diretório de logs do Kafka**     
    Bastas usar `ls` para listar os logs e os tópicos ficarão listados.     
   1.2 `cd {nome_do_topico}` *->* `ls -ltr`: lista os arquivos salvos dentro do tópico, como index, timeindex e o código do log.      
   1.3 `cat {codigo do log}` - aparece, em padrão kafka, as mensagens salvas

## Criando Consumer
Agora podemos consumir as mensagens dentro dos tópicos.   
No diretório bin do kafka:
1. `./kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic aula`
   - Acessa as mensagens fornecidas ao tópico a partir da criadação do Consumer. Se quiser acessar as mensagens anteriores, precisa incluir no final da linha o trecho `--from-beginning`