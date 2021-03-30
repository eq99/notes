# Install

Step 1: Install Docker Engine and docker-compose

```shell
# https://docs.docker.com/engine/install/ubuntu/

# remove old versions
$ sudo apt-get remove docker docker-engine docker.io containerd runc

$ sudo apt-get update
$ sudo apt-get install docker docker-compose -y

# Manager Docker as a none-root user
# See https://docs.docker.com/compose/install/ for more details
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
$ newgrp docker
```



# docker-compose.yaml Example

Example1: 

```yaml
version: '3'
services:
  neo4j:
    image: neo4j:4.2
    hostname: neo4j
    container_name: neo4j
    ports:
      - "7474:7474"
      - "7687:7687"
    volumes:
      - $HOME/neo4j/data:/var/lib/neo4j/data # host:container <---must be absolute path
      - $HOME/neo4j/logs:/logs

    environment:
      NEO4J_AUTH: neo4j/test
      NEO4J_ACCEPT_LICENSE_AGREEMENT: "yes"
      NEO4J_dbms_logs_debug_level: DEBUG
   
#volumes:
#  data-volume:
```

 Start it:

```sh
$ docker-compose up
```



Example 2:

```yaml
version: '3.8'

x-shared:
  &common
  NEO4J_AUTH: neo4j/foobar  
  NEO4J_ACCEPT_LICENSE_AGREEMENT: "yes"
  NEO4J_causal__clustering_initial__discovery__members: core1:5000,core2:5000,core3:5000 
  NEO4J_dbms_memory_pagecache_size: "100M" 
  NEO4J_dbms_memory_heap_initial__size: "100M" 

x-shared-core:
  &common-core
  <<: *common
  NEO4J_dbms_mode: CORE
  NEO4J_causal__clustering_minimum__core__cluster__size__at__formation: 3

networks: 
  lan:

services:

  core1:
    image: neo4j:4.2-enterprise
    networks:
      - lan 
    ports: 
      - "7474:7474"
      - "7687:7687"
    environment:
      <<: *common-core
      NEO4J_causal__clustering_discovery__advertised__address: core1:5000 
      NEO4J_causal__clustering_transaction__advertised__address: core1:6000 
      NEO4J_causal__clustering_raft__advertised__address: core1:7000 

  core2:
    image: neo4j:4.2-enterprise
    networks:
      - lan
    ports:
      - "7475:7474"
      - "7688:7687"
    environment:
      <<:  *common-core
      NEO4J_causal__clustering_discovery__advertised__address: core2:5000
      NEO4J_causal__clustering_transaction__advertised__address: core2:6000
      NEO4J_causal__clustering_raft__advertised__address: core2:7000

  core3:
    image: neo4j:4.2-enterprise
    networks:
      - lan
    ports:
      - "7476:7474"
      - "7689:7687"
    environment:
      <<:  *common-core
      NEO4J_causal__clustering_discovery__advertised__address: core3:5000
      NEO4J_causal__clustering_transaction__advertised__address: core3:6000
      NEO4J_causal__clustering_raft__advertised__address: core3:7000

  readreplica1:
    image: neo4j:4.2-enterprise
    networks:
      - lan
    ports:
      - "7477:7474"
      - "7690:7687"
    environment:
      <<:  *common
      NEO4J_dbms_mode: READ_REPLICA
      NEO4J_causal__clustering_discovery__advertised__address: readreplica1:5000
      NEO4J_causal__clustering_transaction__advertised__address: readreplica1:6000
      NEO4J_causal__clustering_raft__advertised__address: readreplica1:7000
```



Example 3:

```yaml
version: '3'
services:
  neo4j:
    image: neo4j:4.0.3
    hostname: neo4j
    container_name: neo4j
    ports:
      - "7474:7474"
      - "7687:7687"
    depends_on:
      - kafka
    volumes:
      - ./neo4j/plugins:/plugins
    environment:
      NEO4J_AUTH: neo4j/streams
      NEO4J_dbms_logs_debug_level: DEBUG
      # KAFKA related configuration
      NEO4J_kafka_zookeeper_connect: zookeeper:12181
      NEO4J_kafka_bootstrap_servers: kafka:19092
      NEO4J_streams_source_topic_nodes_neo4j: Person{*}
      NEO4J_streams_source_topic_relationships_neo4j: KNOWS{*}

  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    hostname: zookeeper
    container_name: zookeeper
    ports:
      - "12181:12181"
    environment:
      ZOOKEEPER_CLIENT_PORT: 12181

  kafka:
    image: confluentinc/cp-kafka:latest
    hostname: kafka
    container_name: kafka
    ports:
      - "19092:19092"
    depends_on:
      - zookeeper
    environment:
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:12181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:19092
```

