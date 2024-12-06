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

