from kafka import KafkaProducer

#Criando um produtor Kafka
producer = KafkaProducer(
    bootstrap_servers='172.18.0.3:9092',
    acks='all', #Garante que a mensagem foi entregue
    )

#Enviar mensagens testes para o tópico 'aula'
for i in range(5):
    message = f"Mensagem {i + 1}".encode('utf-8')
    future = producer.send('aula', message)
    
    try:
        record_metadata = future.get(timeout=5)
        print(f"Mensagem enviada com sucesso para o tópico {record_metadata.topic} na partição {record_metadata.partition} com offset {record_metadata.offset}")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

#Fechar o produtor
producer.flush()
producer.close()