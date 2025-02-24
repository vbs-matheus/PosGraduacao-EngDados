from kafka import KafkaConsumer

#Criando um consumidor Kafka
consumer = KafkaConsumer(
    'aula', #Tópico para consumot
    bootstrap_servers='localhost:9092', #Endereço do servidor Kafka
    auto_offset_reset='earliest',  #Garante que o consumir pegue todas as mensagens já enviadas
    group_id='grupo_teste' #Identificador do grupo de consumidores
)

print("Aguardando mensagens...")

#Lendo as mensagens no tópico
for message in consumer:
    print(f"Mensagem recebida: {message.value.decode('utf-8')}")