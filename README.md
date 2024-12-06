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
Se estiver com as 3 imagens listadas, o docker compose funcionará corretamente.

---

## Criação do Ambiente

1. Inicializar docker-compose:

```
docker compose up -d
```
Com isso, evidencia-se a execução do docker-compose.yml.

![img](imgs/01.png)

Visto que há containers funcionando, os nodos e brokers estão funcionando corretamente. 

Agora, para criar um tópico e mandar mensagens, é necessário colocar o seguinte comando no bash:

```
docker exec -it kafka1 kafka-topics --create --topic topicMM --bootstrap-server kafka1:9092 --partitions 3 --replication-factor 3
```

```
docker exec -it kafka1 kafka-topics --list --bootstrap-server kafka1:9092
```

![img](imgs/02.png)

Para mandar as mensagens, usa-se o código abaixo:

```
docker exec -it kafka1 kafka-console-producer --topic topicMM --bootstrap-server kafka1:9092
```
E para visualizá-las após, este:

```
docker exec -it kafka1 kafka-console-consumer --topic topicMM --bootstrap-server kafka1:9092 --from-beginning
```
![img](imgs/03.png)

---

## Derrubar um Nodo

Para derrubar um nodo do cluster, utiliza-se um docker stop, e o nome do nodo que deseja parar.

Mesmo com um dos nodos derrubados, o Produtor e o Consumidor não deixam de funcionar.

![img](imgs/04.png)



## Interface Gráfica - Kafka UI

Para acessar a interface gráfica, basta acessar o localhost:8080 no seu navegador.
```
http://localhost:8080/
```
![img](imgs/kafka_ui.png)
![img](imgs/kafka_ui2.png)
![img](imgs/kafka_ui3.png)
