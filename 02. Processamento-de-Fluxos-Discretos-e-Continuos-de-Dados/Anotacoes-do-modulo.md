# **Temáticas da unidade**

Abordaremos os conceitos sobre fluxos contínuos de dados, IoT, IPV6 e outros. Veremos exemplos de aplicações que utilizam essa abordagem, e a parte inicial de uma arquitetura online para trabalhar com esse tipo de aplicação.

---
---

## **Revisão Rápida - Big Data: Os 4 V’s**

Os dados gerados no mundo seguem quatro principais características, conhecidas como os **4 V’s do Big Data**:

### 1. Volume (Escala dos Dados)
- Refere-se à quantidade massiva de dados gerados diariamente.
- Estima-se que **2,5 quintilhões de bytes** sejam criados por dia.
- Em 2020, projetou-se que o total de dados criados chegaria a **40 zetabytes**.
- **Exemplo**: Bolsas de valores capturam **1TB de informações por transação**.

### 2. Velocidade (Análise de Dados em Fluxo)
- Dados são gerados e processados em tempo real.
- O crescimento da conectividade global acelera esse fluxo.
- **Exemplo**: Dispositivos IoT possuem **sensores para monitoramento constante**.

### 3. Variedade (Diferentes Formatos de Dados)
- Dados podem vir de diversas fontes e em múltiplos formatos (**estruturados e não estruturados**).
- **Exemplo**: Redes sociais geram **bilhões de postagens diariamente**.

### 4. Veracidade (Confiabilidade dos Dados)
- Qualidade e precisão dos dados são fundamentais.
- Dados imprecisos ou incompletos podem levar a decisões erradas.
- **Exemplo**: **1 em cada 3 líderes empresariais** não confia nos dados usados para tomada de decisões.

### **Conclusão**
Big Data é um conceito essencial para tecnologias de **Processamento de Fluxos de Dados**, pois permite analisar grandes volumes de dados em tempo real, otimizando processos e gerando insights estratégicos.

---
---

## **Fluxos Contínuos de Dados – O que é?**

- Dados fluem continuamente ao longo do tempo.
- Chamados de **Fluxos Contínuos de Dados (Data Streams)** ou **FCDs**.
- Processam dados que chegam em **sequência**, sem a necessidade de armazenar grandes volumes antes do processamento.
- O **modelo Batch** não é adequado para problemas com **natureza dinâmica**, pois exige processamento em blocos previamente definidos.

## Características

### **Propriedades Fundamentais**
- Dados chegam **de forma contínua**, em **alta velocidade**.
- O fluxo de dados pode ser **muito grande ou infinito**, tornando inviável seu armazenamento completo em memória.
- Os dados gerados podem **variar na distribuição**, tornando o processamento mais desafiador.
- **Algoritmos tradicionais de mineração de dados** não são eficientes para FCDs.

### **Relação com Machine Learning**
- Historicamente, **Machine Learning** foi baseado em aprendizado **batch**, utilizando **dados históricos** para treinar modelos.
- O aprendizado de máquina para FCDs precisa de **dados representativos** e adaptáveis em tempo real.
- O processamento contínuo gera **modelos de decisão para predições futuras**.

## Fatores que contribuem para a adoção de FCDs

- **Aplicações do mundo real** trabalham cada vez mais com fluxos contínuos de dados.
- O fenômeno da **Internet das Coisas (IoT)** impulsionou essa demanda.
- **Grande tendência** com diversas aplicações emergentes.
- **IPv6** deve **aumentar a adoção** desse tipo de processamento, possibilitando mais conexões simultâneas e melhor desempenho na comunicação de dispositivos.

---

### **Conclusão**
O processamento de Fluxos Contínuos de Dados é essencial para cenários onde **dados são gerados constantemente e precisam ser processados em tempo real**. Modelos tradicionais de armazenamento e aprendizado batch não são adequados, sendo necessária uma abordagem dinâmica e escalável.

---
---

## **Fluxos Contínuos de Dados e a Internet das Coisas (IoT)**

### O que é a Internet das Coisas (IoT)?
- A **Internet das Coisas (IoT)** é uma revolução tecnológica que conecta dispositivos físicos à internet.
- Permite que itens do cotidiano **se comuniquem e compartilhem dados automaticamente**.
- Dispositivos como eletrodomésticos, sensores, veículos e vestuário inteligente fazem parte desse ecossistema.

### Relação entre IoT e Fluxos Contínuos de Dados
- Dispositivos IoT geram **dados constantemente**, exigindo processamento contínuo.
- Sensores transmitem informações em **tempo real**, como temperatura, consumo de energia e localização.
- O modelo tradicional de processamento em batch não é eficiente para lidar com esse fluxo dinâmico.

### **Conclusão**
A IoT expande a conectividade para objetos do dia a dia, transformando-os em **fontes de dados contínuos**. Esse cenário demanda **modelos avançados de processamento** para lidar com a grande quantidade de informações geradas em tempo real.

---
---
## **Características de Algoritmos e Desafios**

### **Características desejáveis para algoritmos**
- Devem ser capazes de **se adaptar a novos dados** continuamente.
- Devem funcionar de forma **incremental**, sem precisar reprocessar todo o conjunto de dados.
- A **atualização constante do modelo** garante que os dados mais recentes sejam considerados.

### **O desafio de trabalhar com Fluxos Contínuos de Dados (FCDs)**
- Avanços tecnológicos em **hardware e software** permitiram a coleta massiva de dados.
- **Gerenciar grandes volumes de dados** em tempo real é um dos principais desafios.
- Os conceitos e padrões dentro dos FCDs **podem mudar com o tempo**, exigindo flexibilidade nos algoritmos.

### **Dificuldades associadas ao trabalho com FCDs**
- **Extrair conhecimento útil** de fluxos contínuos de dados é um processo desafiador.
- A maioria dos **modelos tradicionais de Machine Learning** assume que os dados são estáticos, o que não se aplica aos FCDs.
- **Manter a acurácia dos modelos ao longo do tempo** é difícil, pois os padrões de dados podem mudar dinamicamente.

### **Tipos de variações na distribuição dos dados**
- **Repentina ou abrupta**: Mudanças drásticas e imediatas nos padrões de dados.
- **Incremental**: Pequenas variações ao longo do tempo.
- **Gradual**: Mudanças suaves e progressivas.
- **Recorrente**: Padrões que se repetem periodicamente.
- **Outlier**: Dados que fogem da tendência geral e podem indicar eventos excepcionais.

### **Conclusão**
Os desafios do processamento de Fluxos Contínuos de Dados exigem **algoritmos adaptáveis, escaláveis e eficientes**. O uso de modelos incrementais e técnicas específicas para lidar com variações na distribuição dos dados é essencial para garantir a qualidade das análises e previsões.

---
---

## **Arquiteturas de Big Data para Fluxos Contínuos de Dados (FCDs)**

### **Definição de Arquitetura para FCDs**
Uma arquitetura eficiente para o processamento de **Fluxos Contínuos de Dados (FCDs)** deve atender a grandes demandas de volume, velocidade e variedade. O desenvolvimento de uma arquitetura eficaz requer a adoção de alguns passos fundamentais:

- **Coleta de Dados:** Captura de informações a partir de diversas fontes.
- **Processamento:** Tratamento e transformação dos dados para análise.
- **Armazenamento:** Organização dos dados em bancos ou sistemas distribuídos.
- **Definição de Pipelines:** Automação do fluxo de dados entre diferentes etapas.
- **Visualização:** Exibição dos dados de maneira acessível para análise.

### **Fluxo da Arquitetura**
O fluxo de trabalho em arquiteturas de Big Data para FCDs geralmente segue um modelo estruturado com os seguintes componentes:

1. **Ingestão dos Dados:** Captura e entrada dos dados no sistema.
2. **Processamento:** Transformação e análise dos dados em tempo real ou em lote.
3. **Armazenamento/Serving Layer:** Armazena os dados processados para recuperação e uso posterior.
4. **Visualização:** Geração de dashboards e relatórios para facilitar a interpretação dos dados.

### **Ferramentas para Ingestão de Dados**
Para lidar com a ingestão de grandes volumes de dados em tempo real, diversas ferramentas são utilizadas. Uma das principais abordadas foi o **Apache Flume**.

#### **Apache Flume**
- Criado pela **Cloudera**, o **Flume** é um sistema distribuído e confiável para **coletar, agregar e transferir grandes volumes de dados**.
- Utilizado para mover dados de múltiplas fontes para armazenamento centralizado ou sistemas de mensageria.
- Em 2012, tornou-se um projeto **top level da Apache Foundation**.

#### **Arquitetura do Flume**
A estrutura do Flume é baseada em três componentes principais:
1. **Source:** Captura dados de diferentes fontes (web servers, logs, eventos).
2. **Channel:** Armazena temporariamente os dados antes do processamento.
3. **Sink:** Envia os dados processados para o destino final, como o HDFS.

---

### **Conclusão**
As arquiteturas de Big Data para FCDs devem ser altamente escaláveis e eficientes, garantindo ingestão contínua, processamento distribuído e armazenamento otimizado. Ferramentas como o **Apache Flume** são fundamentais para a ingestão de dados em tempo real, permitindo que empresas lidem com grandes volumes de informações de maneira estruturada.

---
---
## **Arquiteturas de Big Data para FCDs**

### **Ferramentas para Coleta de Dados**
- **Apache Kafka**  
  - Plataforma distribuída de mensagens e streaming que armazena temporariamente grandes volumes de dados de streams antes que eles sejam processados. Ele atua como um *buffer*, permitindo que sistemas consumidores processem os dados conforme sua capacidade, evitando perda de informações em casos de sobrecarga.  
  - Funciona através de um sistema de tópicos onde mensagens são produzidas e consumidas.
   - Muito utilizado na **ingestão de dados**

- **Apache Flume**  
  - Criado pela Cloudera, projetado para coletar, agregar e mover grandes quantidades de dados de diferentes fontes para um destino centralizado, como um sistema de armazenamento distribuído (ex: HDFS). 
  - Atua na etapa de **ingestão de dados**, sendo responsável por trazer os dados para o pipeline de processamento e armazenamento de Big Data.
  - Pode ser usado em conjunto com Kafka, formando a arquitetura conhecida como **Flafka**.

#### **Funcionamento Básico do Kafka**
- Um **produtor** gera uma mensagem.
- A mensagem é armazenada em um **tópico**.
- Um **consumidor** lê e processa a mensagem armazenada.

---

### **Caso do LinkedIn**
- **Problema**  
  - O LinkedIn enfrentava dificuldades para comunicar diferentes pipelines e serviços.  
  - A estrutura existente era complexa, com muitas conexões diretas entre serviços.

- **Solução**  
  - Criaram o **Kafka**, permitindo centralizar a comunicação entre os serviços.  
  - Todos os serviços passaram a se comunicar por mensagens em tópicos do Kafka.

- **Impacto**  
  - O Kafka se tornou o **núcleo dos pipelines do LinkedIn**.  
  - Processa cerca de **1,4 trilhão de mensagens** com **1.400 brokers**.  
  - Possui alta escalabilidade e funciona de forma totalmente distribuída.  
  - Suporta **particionamento** de dados para otimizar o processamento.

---

### **Conclusão**
- **Apache Kafka e Flume são ferramentas fundamentais para arquiteturas de Big Data**.  
- **A implementação do Kafka no LinkedIn resolveu problemas complexos de comunicação**, permitindo escalabilidade e eficiência no processamento de mensagens.

---
---

## **Ferramentas para Processamento de Dados em Tempo Real**

---

### **Introdução**
- O processamento de dados em tempo real é essencial para aplicações que exigem resposta imediata, como monitoramento de redes sociais, detecção de fraudes financeiras e IoT (Internet das Coisas).
- Neste módulo, são abordadas duas ferramentas amplamente utilizadas para essa finalidade: **Apache Storm** e outras soluções de processamento contínuo.

---

### **Apache Storm**
Apache Storm é um sistema distribuído para o processamento de dados em tempo real. Criado por **Nathan Marz** na BackType (posteriormente adquirida pelo Twitter), a ferramenta se destaca pela capacidade de processar grandes volumes de dados de forma escalável.

#### **Características principais do Apache Storm**
- **Baixa latência** – Projetado para responder rapidamente a eventos em tempo real.  
- **Alta escalabilidade** – Distribui processamento entre múltiplas máquinas.  
- **Tolerância a falhas** – Reinicializa componentes em caso de falhas.  
- **Facilidade de integração** – Pode trabalhar com várias fontes de dados, como **Kafka, bancos de dados, APIs e arquivos de texto**.

---

#### **Arquitetura do Apache Storm**
A arquitetura do Storm é composta por dois principais componentes:

  1. **Spouts**  
     - São as **fontes de dados** no Apache Storm.  
     - Responsáveis por coletar informações de diferentes origens, como **bancos de dados, serviços web, tópicos do Kafka e arquivos de texto**.  
     - Exemplos de uso: leitura de mensagens do Kafka, eventos de sensores IoT ou transações financeiras.

  2. **Bolts**  
     - Realizam o **processamento e transformação dos dados**.  
     - Aplicam regras de negócio, agregações, filtros ou análises avançadas.  
     - Podem alimentar outros bolts ou armazenar os resultados em bancos de dados e data warehouses.

---

#### **Fluxo de Processamento no Storm**
- Os **Spouts** enviam os dados para os **Bolts**.
- Os **Bolts** processam os dados em tempo real, transformando-os conforme necessário.
- O resultado final pode ser armazenado ou enviado para outros sistemas.

#### **Exemplo de Arquitetura do Apache Storm**
A imagem abaixo ilustra o fluxo de processamento dentro do Apache Storm, destacando os Spouts (fontes de dados) e os Bolts (unidades de processamento):

📌 **Referência Visual da Arquitetura do Storm**:  
![Arquitetura do Apache Storm](https://storm.apache.org/images/storm-flow.png)

---

#### **Exemplos de Aplicações do Apache Storm**
- **Monitoramento de redes sociais** – Processamento contínuo de tweets para detectar tendências.  
- **Análise de logs em tempo real** – Detectar falhas ou padrões de uso anômalos em servidores.  
- **Detecção de fraudes bancárias** – Identificação de transações suspeitas em tempo real.  
- **IoT e Smart Cities** – Processamento de dados de sensores conectados.

---

## **Conclusão**
O **Apache Storm** é uma das ferramentas mais robustas para o processamento contínuo de fluxos de dados. Ele desempenha um papel fundamental em sistemas de Big Data que exigem **baixa latência, alta escalabilidade e confiabilidade**. Sua arquitetura modular permite integrar diferentes fontes de dados e realizar diversas transformações antes de armazenar ou repassar os resultados.

*Outras ferramentas como Apache Flink e Spark Streaming também desempenham papéis similares, mas o Storm é amplamente reconhecido por sua arquitetura baseada em fluxos contínuos e processamento distribuído.*

### **Apache Spark Streaming**

### **O que é o Apache Spark Streaming?**
- Extensão do **Apache Spark**, projetada para **processamento distribuído de dados em tempo real**.  
- Desenvolvido pelo **AMPLab da Universidade da Califórnia, Berkeley**, com código aberto desde 2010 na **Apache Foundation**.  
- Permite que aplicações em clusters **Hadoop** executem tarefas **até 100 vezes mais rápido na memória** e **10 vezes mais rápido em disco**.  
- Suporta desenvolvimento em **Java, Scala e Python**.

---

#### **Funcionamento do Spark Streaming**
- Trabalha com a estrutura de **microbatches**, onde pequenos pacotes de dados são processados rapidamente.  
- Esse modelo gera uma noção de **Real Time** ou **Near Real Time**, pois o processamento acontece em intervalos curtos.  
- **Comparação com Apache Storm**:  
  - **Storm** processa eventos **um a um**, conforme chegam.  
  - **Spark Streaming** processa dados em **lotes pequenos (microbatches)**.  

📌 **Arquitetura Comparativa**
![Fluxo de Microbatches no Spark Streaming](https://spark.apache.org/docs/latest/img/structured-streaming-model.png)

---

#### **Arquitetura de uma Aplicação com Spark Streaming**
- **Fontes de dados (Streaming e estáticas)**  
  - Kafka, Amazon Kinesis, Akka, Flume, etc.  
  - Bancos de dados relacionais e NoSQL (MySQL, Cassandra, PostgreSQL, MongoDB).  
- **Módulos do Spark Streaming**  
  - **MLlib**: Treinamento de modelos de **Machine Learning** com dados ao vivo.  
  - **Spark SQL**: Análises e consultas interativas com **DataFrames**.  
- **Destinos de dados**  
  - ElasticSearch, Cassandra, MemSQL, HBase, Kafka.

---

### **DStreams e Processamento por Janelas de Tempo**
- O **fluxo de dados** no Spark Streaming ocorre através de **DStreams (Discretized Streams)**.  
- DStreams podem ser processados de duas formas:  
  1. **Microbatches fixos**: Pequenos pacotes de dados processados em intervalos curtos.  
  2. **Janelas de tempo (Windowing)**: Permite acumular pacotes dentro de um intervalo maior antes do processamento.


---

## **Conclusão**

O **Apache Storm** é uma ferramenta robusta para processamento contínuo de fluxos de dados, ideal para sistemas de Big Data que exigem **baixa latência, alta escalabilidade e confiabilidade**. Sua arquitetura modular permite integração com diversas fontes de dados e transformações antes de armazenar ou repassar resultados.   

Enquanto isso, o **Apache Spark Streaming** se destaca no processamento distribuído de fluxos em **tempo real**, utilizando um modelo de **microbatches** que facilita operações analíticas em tempo real. Ambas as ferramentas são amplamente utilizadas, com o Storm sendo reconhecido por seu processamento contínuo e o Spark Streaming por sua abordagem baseada em lotes.

---
---

## **Tipos de Dados e Fontes de Informação**

### Tipos de dados

#### **Dados Estruturados**
- Muito utilizado.
- Dados organizados e padronizados.
- Segue um modelo baseado em **linhas e colunas**.
- Possui vários formatos, como **bancos de dados relacionais e arquivos CSV**.
- Facilmente armazenado e consultado através de **SQL**.

---

#### **Dados Não Estruturados**
- Representam **a maior parte dos dados atuais**.
- Não seguem um formato de linhas e colunas.
- Não possuem um modelo de dados fixo.
- Mais difícil de analisar e processar.
- **IA** pode ser utilizada para facilitar o processamento.
- Exemplos: **vídeos, fotos, textos, áudio, redes sociais**.

---

#### **Dados Semi-Estruturados**
- Mistura características de **dados estruturados e não estruturados**.
- Possui uma **estrutura flexível**.
- Inclui **metadados** que ajudam a organizar as informações.
- Fácil entendimento e leitura automatizada.
- Muito utilizado na web, com formatos como **JSON e XML**.

---

### Fontes de Dados
- **Dados Internos**: Informações geradas dentro da organização.
- **Dados de Parceiros**: Compartilhados entre empresas.
- **Dados Externos**: Obtidos de terceiros.
- **Social**: Redes sociais, interações de usuários.
- **Dados Públicos**: Disponíveis em repositórios governamentais e acadêmicos.
- **IoT**: Sensores conectados e dispositivos inteligentes.

#### **APIs (Application Programming Interfaces)**
  - **REST API**: Modelo mais utilizado para integração.
  - **Representational State Transfer (REST)**: Comunicação via requisições HTTP.
  - **Integração por rede**, permitindo sistemas se comunicarem de forma padronizada.
  - **Baixa curva de aprendizado**.
  - **Transmissão de dados entre diferentes ferramentas**.

---

#### **Protocolo FTP (File Transfer Protocol)**
  - Método **tradicional** para **transferência de arquivos**.
  - Utilizado para **arquivos de texto e binários**.
  - Suporta conexão **segura (SFTP)**.
  - Ainda amplamente usado, mas considerado **legado**.
  - Pode ser **interno (intranet) ou externo (servidores remotos)**.

---

#### **File Server**
- Servidores dedicados para **armazenamento de arquivos em rede**.
- Utilizado para **compartilhamento temporário** de informações.
- Modelo **antigo**, sendo substituído por **soluções baseadas em nuvem**.
- Exemplo: Empresas que armazenam arquivos de ERP em servidores internos.

---

#### **Database (Bancos de Dados)**
- **Banco de Dados Relacional**: SQL Server, Oracle, MySQL, PostgreSQL.
- **Banco de Dados NoSQL**: MongoDB, Cassandra, Redis, Neo4j.
- Suporta **processamento em Batch ou Real Time**.
- Oferece **diferentes abordagens**, dependendo da necessidade.
- **Facilita integração**, mas pode gerar **overhead** se mal dimensionado.

---

#### **Mensageria e Processamento de Eventos**
- Arquitetura **orientada a eventos**.
- Processamento **assíncrono** para maior eficiência.
- Suporte para **dados em tempo real (Real Time)**.
- Muito utilizado em **IoT e Data Flow**.
- Suporte a vários formatos e **frameworks populares** como:
  - **Apache Kafka**.
  - **RabbitMQ**.
  - **Amazon Kinesis**.
  - **Google Cloud Pub/Sub**.
  - **ActiveMQ**.
  - **Azure Event Hubs**.

---

#### **Web Scraping e Dados Semi-Estruturados**
- **Coleta de dados automatizada na web (Crawling)**.
- Técnica de **extração de dados** ("Raspagem" de sites).
- Utiliza ferramentas para capturar **HTML, JSON, APIs públicas**.
- Pode simular navegação humana.
- **Polêmico** devido a questões de privacidade e segurança.
- **CAPTCHA** foi criado para dificultar a automação de scraping.

---

## **Conclusão**
- Existem **três principais categorias de dados**: **Estruturados, Não Estruturados e Semi-Estruturados**.
- **APIs e FTP** são métodos fundamentais para troca de informações entre sistemas.
- **Mensageria e Web Scraping** são técnicas avançadas para processamento de dados em tempo real.
- **Bases de Dados** oferecem suporte tanto para **consultas transacionais quanto análises complexas**.
- A escolha da tecnologia **depende do tipo de dado e da necessidade do sistema**.

---
---

## Tipos de Ingestão de Dados

A ingestão de dados é o processo de coleta e carregamento de dados de diversas fontes para um sistema centralizado, como um banco de dados, data lake ou plataforma analítica. Existem diferentes tipos de ingestão, cada um adequado a um cenário específico.

---

### Ingestão Batch

A ingestão batch processa grandes volumes de dados de forma periódica, armazenando-os antes de serem processados.  

- **Dados estáticos**: os dados não mudam frequentemente.
- **Cargas agendadas**: execução em intervalos predefinidos (diário, semanal, mensal).
- **Grande fluxo de dados**: adequado para processamento de grandes volumes de dados de uma só vez.
- **Arquivos ou banco de dados**: dados podem ser provenientes de arquivos CSV, JSON ou bancos de dados relacionais.
- **Muito utilizado para BI**: essencial para relatórios analíticos e dashboards.
- **Também utilizado em Big Data**: integração com sistemas distribuídos como Hadoop e Spark.

---

### ETL (Extract, Transform, Load)

O **ETL** é um processo tradicional para ingestão e transformação de dados antes do carregamento no sistema de destino.

- **Extract, Transform e Load**: extrai dados de fontes diversas, aplica transformações e carrega no destino.
- **Ampla adoção**: utilizado em diversas indústrias.
- **Abordagem tradicional**: comum em Data Warehouses.
- **Fácil utilização**: diversas ferramentas disponíveis, como Talend, Informatica e Pentaho.
- **Cargas batch**: normalmente utilizado com processamento em lotes.
- **Processamento massivo**: ideal para grandes volumes de dados.
- **Pouca flexibilidade após o load**: qualquer alteração requer novo processamento.

---

### ELT (Extract, Load, Transform)

O **ELT** é uma abordagem moderna que inverte a sequência do ETL, primeiro carregando os dados no destino e aplicando transformações posteriormente.

- **Mudança no fluxo de dados**: primeiro os dados são armazenados e depois transformados.
- **Maior flexibilidade**: permite diferentes tipos de processamento sem necessidade de recarregar os dados.
- **Trabalha com dados brutos**: armazenados sem modificação inicial.
- **Alternativa moderna ao ETL**: utilizado em data lakes e plataformas em nuvem.
- **Redução do tempo de carga**: mais eficiente para grandes volumes de dados.

---

### Ingestão em Tempo Real (Real-Time)

A ingestão **real-time** permite a coleta e processamento contínuo de dados à medida que eles são gerados.

- **Dados em tempo real**: processamento instantâneo de eventos conforme ocorrem.
- **Permite tomada de decisão rápida**: utilizado para monitoramento e análise em tempo real.
- **Fluxo contínuo de dados**: processamento imediato sem necessidade de armazenamento prévio.
- **Distribuído no tempo**: eventos chegam de forma assíncrona ao sistema.
- **Streaming**: baseado em frameworks como Apache Kafka, Apache Flink e Spark Streaming.
- **Orientado a eventos**: essencial para sistemas de monitoramento, IoT e análise preditiva.

---
---

## **Arquiteturas Baseadas em Eventos**
- Todo dado é tratado como um **evento ou mensagem**.
- Comunicação **assíncrona** entre sistemas.
- Dados distribuídos por **sistemas de mensageria** como **Kafka**.
- **Alta escalabilidade** e eficiência para aplicações distribuídas.

---

### **Arquitetura Lambda**
- Combina **Batch e Streaming** para garantir tolerância a falhas.
- Mantém **dois fluxos de processamento** (lote e tempo real).
- Possui **alto custo de manutenção** e **processamento**.
- Duplica a lógica dos dados para garantir consistência.

### **Arquitetura Kappa**
- Utiliza um **único fluxo de dados** em tempo real.
- Reprocessamento ocorre a partir dos **eventos** recebidos.
- **Elimina a necessidade de Batch Processing**.
- Simplifica a **gestão, infraestrutura e código**.

📌**Comparação entre arquiteturas**
![Arquitetura Lambda](https://media.geeksforgeeks.org/wp-content/uploads/20240117220316/Layer-of-Lambda-Architecture.jpg)
![Arquitetura Kappa](https://www.kai-waehner.de/wp-content/uploads/2021/09/Kappa-Architecture-with-one-Pipeline-for-Real-Time-and-Batch-1024x442.png)

---

## **Evolução das Arquiteturas de Ingestão**
A ingestão de dados evoluiu com o tempo, começando com abordagens tradicionais como **ETL e Batch**, passando para **arquiteturas orientadas a eventos** e atualmente para **streaming em tempo real**. Tecnologias como **Hadoop, Spark, Kafka e Flink** desempenham papéis fundamentais nesse cenário.

### **Ingestão em um Data Lake**

A ingestão de dados em um **Data Lake** envolve a coleta de informações de diferentes fontes e sua armazenagem sem uma estrutura rígida. Isso permite que os dados sejam analisados e processados conforme necessário, tornando-se uma solução flexível para Big Data.

#### **Fontes de Dados para um Data Lake**
Os dados podem vir de diversas fontes, incluindo:

- **OLTP (Online Transaction Processing) ou ODS (Operational Data Store)**  
  - Sistemas de banco de dados transacionais que armazenam informações operacionais.

- **Enterprise Data Warehouse (EDW)**  
  - Bancos de dados estruturados usados para análises empresariais.

- **Logs e Dados Não Estruturados**  
  - Arquivos de logs de sistemas, sensores, redes sociais e outras fontes não convencionais.

- **Cloud Services**  
  - Dados armazenados em serviços de nuvem como AWS S3, Google Cloud Storage e Azure Blob Storage.

- **Formatos de Ingestão**  
  - **File Data:** Arquivos CSV, JSON, XML, Parquet, entre outros.
  - **DB Data:** Extração direta de bancos de dados relacionais.
  - **ETL Extracts:** Processos que transformam e carregam dados no Data Lake.
  - **Streaming:** Fluxos de dados contínuos vindos de sensores, IoT e eventos de aplicativos.
  - **APIs:** Integração com sistemas externos via chamadas API.

---

#### **Fluxo da Ingestão no Data Lake**
1. **Transient Loading Zone (Zona de Carregamento Transitória)**  
   - Os dados chegam e são armazenados temporariamente antes do processamento.

2. **Raw Data (Dados Brutos)**  
   - Os dados são armazenados em sua forma original, sem alteração.

3. **Refined Data (Dados Refinados)**  
   - Processamento para padronização, limpeza e agregação de dados.
 
4. **Trusted Data (Dados Confiáveis)**  
   - Informações validadas, referenciadas e organizadas para análises.

5. **Discovery Sandbox**  
   - Ambiente exploratório para cientistas de dados e analistas realizarem experimentos.

6. **Consumption Zone (Zona de Consumo)**  
   - Área onde os dados são disponibilizados para **analistas, pesquisadores e cientistas de dados**.

📌 
![Fluxo da Ingestão no Data Lake](https://dataladder.com/wp-content/uploads/2021/09/5066752-screen-shot-2017-04-24-at-111511-am-3783ixy9uk06tqzjcrmi2o.png)
---

### **Governança e Qualidade dos Dados**
Para garantir um Data Lake eficiente, são adotadas práticas como:
- **Metadados** para organização dos dados.
- **Garantia da qualidade dos dados** com processos de validação.
- **Catálogo de Dados** para facilitar a busca e descoberta de informações.
- **Segurança** para controle de acessos e proteção contra vazamentos.

---

## **Onde Trabalhar?**
A escolha entre **On-Premise e Cloud** depende de fatores como:
- **On-Premise:** Controle total sobre infraestrutura, maior segurança, custos fixos elevados.
- **Cloud:** Escalabilidade, menor custo inicial, manutenção simplificada.

📌 **Principais Provedores de Cloud:** AWS, Google Cloud Platform (GCP), Microsoft Azure.

---

## **Comparação de Soluções de Ingestão**
### **AWS**
- Serviços principais: **Kinesis, Glue ETL, Redshift, QuickSight**.
- Ideal para **processamento escalável e análise de dados**.

### **GCP**
- Serviços principais: **Pub/Sub, DataFlow, BigQuery, Data Studio**.
- Focado em **análises avançadas e Machine Learning**.

### **Azure**
- Serviços principais: **Azure Data Lake, Event Hub, Power BI**.
- Excelente para **integração com ambientes corporativos**.

### **Open Source**
- Ferramentas principais: **Kafka, Apache Spark, Flink, Airflow, NiFi**.
- Alternativa **flexível e de baixo custo** para ingestão e processamento distribuído.

---

## **Ferramentas ETL Mais Utilizadas**
- **Talend**
- **Pentaho**
- **Oracle Data Integrator**
- **Informatica PowerCenter**
- **SQL Server Integration Services (SSIS)**
- **IBM InfoSphere DataStage**

---

## **Conclusão**
A escolha do tipo de ingestão de dados depende dos requisitos de latência, escalabilidade e volume de dados:
- **Batch:** Melhor para grandes cargas de dados em intervalos regulares.
- **Streaming:** Ideal para aplicações que necessitam de dados em tempo real.
- **Arquitetura Lambda:** Combina batch e streaming, mas tem custo elevado.
- **Arquitetura Kappa:** Mais simplificada e eficiente para ingestão em tempo real.

Cada abordagem possui suas vantagens e desafios, sendo essencial escolher a estratégia correta para garantir eficiência no processamento e análise de dados.