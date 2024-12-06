from confluent_kafka import Producer

producer = Producer(
    {
        "bootstrap.servers": "kafka1:9092,kafka2:9093,kafka3:9094",
    }
)


def delivery_report(err, msg):
    if err:
        print(f"Erro ao enviar mensagem: {err}")
    else:
        print(
            f"Mensagem enviada para o tópico '{msg.topic()}', partição {msg.partition()}"
        )


try:
    print("Enviando mensagem para o Kafka...")
    producer.produce("topicoMM", value="Hello Kafka!", callback=delivery_report)
    producer.flush()
    print("Mensagem enviada com sucesso.")
except Exception as e:
    print(f"Erro: {e}")
