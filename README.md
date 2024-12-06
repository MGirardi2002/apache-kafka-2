# Trabalho 5
## Matheus Girardi e Maiara Zucco

---

# Passo a passo de instalação
1. Certificar de instalar o Docker Desktop na máquina pelo site;

2. Verificação se o docker está instalado, usando bash:

```
docker --version
```

3. Instalação das imagens com docker pull:

```
docker pull confluentinc/cp-kafka:latest &
docker pull confluentinc/cp-zookeeper:latest &
docker pull provectuslabs/kafka-ui:latest &
```

4. Verificação das imagens:

```
 docker images
```

## Criação do Ambiente

1. Inicializar docker-compose:

```
docker compose up -d
```

```
docker exec -it kafka1 kafka-topics --create --topic topicMM --bootstrap-server kafka1:9092 --partitions 3 --replication-factor 3
```

8. Clicando em Topic no http://localhost:8080/ é possível vizualizar o tópico criado.
  

9. Novidade: Utilizar uma interface gráfica para vizualização de envio de mensagens e consumo, para isso inserimos o seguinte comando:

```
docker exec -it kafka1 kafka-topics --list --bootstrap-server kafka1:9092
```

10. Envio de mensagem pelo terminal, inserir o seguinte comando:

```
docker exec -it kafka1 kafka-console-producer --topic topicMM --bootstrap-server kafka1:9092
```

11. Pra consumir mensagem pelo terminal, vizualização das mensagens enviador, inserir o seguinte comando:

```
docker exec -it kafka1 kafka-console-consumer --topic topicMM --bootstrap-server kafka1:9092 --from-beginning
```

## Interface Gráfica - Kafka UI

Para acessar a interface gráfica, basta acessar o localhost:8080 no seu navegador.
```
http://localhost:8080/
```

