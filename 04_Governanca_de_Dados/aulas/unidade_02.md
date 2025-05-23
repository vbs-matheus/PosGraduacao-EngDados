# **Unidade 02 - Operacionalização da Governança de Dados**

Nessa unidade, vamos explorar conceitos de Governança de Dados, começando pela definição de papéis e responsabilidades essenciais para garantir a gestão eficiente dos dados em uma organização.  

Veremos como implementar estruturas de Governança de Dados, monitoramento e auditoria.  
  
Abordaremos questões de metadados, dados mestres e catalogação de dados para a acessibilidade das informações para a organização.  

Por fim, introduziremos frameworks de Governança de Dados e o Data Management Maturity Model (DMM), que auxiliam no amadurecimento dos processos de gerenciamento de dados dentro das empresas.

## ▹ Temáticas da Unidade:

- Definição de Papéis e Responsabilidades
- Implementação de Estruturas de GD
- Monitoramento e Auditoria
- Qualidade de Dados
- Metadados e Dados Mestres
- Catalogação de Dados
- Introdução a Frameworks de GD
- Introdução ao Data Management Maturity Model - DMM

## ▹ Objetivos:

Capacitação para compreender a importância da definição clara de papéis e responsabilidades dentro da Governança de Dados (GD), assim como explorar a implementação de estruturas organizacionais eficazes para suportar essa governança.  

Aprender sobre processos e de monitoramentos e auditoria, como aplicá-los para assegurar conformidade de dados e a maturidade da gestão de dados de uma organização.

---
---

# Aula 01 - Definição de Papéis e Responsabilidades

Definir claramente papéis e responsabilidades é essencial para garantir que todos na organização saibam o que se espera no gerenciamento, proteção e uso dos dados. Uma estrutura bem definida promove consistência, conformidade e eficácia nas práticas de governança.

Os papéis podem variar em nome, mas suas funções costumam ser similares. 

Destacam-se:

### **Data Owner**: 
Proprietário dos dados, geralmente um executivo ou líder responsável pelo controle geral dos dados. Define políticas e diretrizes, assegura alinhamento com objetivos estratégicos, aprova acessos e compartilhamentos, e garante conformidade regulatória. Interage com Data Providers (que coletam e geram dados) e Data Consumers (que utilizam os dados).  

![Data Owner](https://raw.githubusercontent.com/vbs-matheus/PosGraduacao-EngDados/refs/heads/main/imgs/data_owner.png)

### **Data Steward**: 

Administrador dos dados, responsável pela gestão diária, implementação das políticas e manutenção da qualidade dos dados — integridade, precisão e consistência. Monitora práticas de governança, facilita integração e compartilhamento, e gerencia o ciclo de vida dos dados, incluindo retenção e descarte.

![Data Steward](https://raw.githubusercontent.com/vbs-matheus/PosGraduacao-EngDados/refs/heads/main/imgs/data_steward.png)

### **Data Custodian**: 
Responsável pela segurança física e digital dos dados, geralmente ligado a TI ou operações. Implementa controles de segurança, gerencia armazenamento e infraestrutura, garantindo disponibilidade e integridade, além de monitorar e responder a incidentes.

![Data Custodian](https://raw.githubusercontent.com/vbs-matheus/PosGraduacao-EngDados/refs/heads/main/imgs/data_custodian.png)

### **Data Architect**: 
Especialista que projeta e mantém a arquitetura de dados, incluindo modelos, padrões e infraestrutura. Garante integração, interoperabilidade, escalabilidade e performance da arquitetura, considerando dados estruturados, semi e não estruturados, além de diferentes formatos e latências (batch e streaming).

![Data Architect](https://raw.githubusercontent.com/vbs-matheus/PosGraduacao-EngDados/refs/heads/main/imgs/data_architect.png)


### **Data Analyst**: 
Responsável por analisar dados e gerar insights para a tomada de decisão.

### **Data Governance Council**: 
Conselho formado por representantes de diversas áreas, que supervisiona e direciona iniciativas de governança, define e revisa políticas, resolve conflitos, monitora eficácia e facilita a comunicação.

### **Data Governance Manager**: 
Coordena e gerencia as iniciativas diárias de governança, implementa e monitora programas e políticas, coordena atividades de stewards e custodians, gerencia projetos e oferece treinamentos e suporte.

### **Compliance Officer**: 
Garante a conformidade com regulamentações e políticas, como a LGPD.

### **End Users / Consumers**: 
Usuários dos dados para suas atividades, especialmente na tomada de decisão. Devem seguir políticas de uso e proteção, reportar problemas e participar de treinamentos em segurança e privacidade.

Muitas vezes, esses papéis já são desempenhados na empresa, mas não de forme declarada ou definida.  
Ter esses papéis bem definidos facilita a implementação e operação da governança de dados, aproveitando responsabilidades já existentes e garantindo clareza na gestão dos dados.


# Aula 02 - Implementação de Estruturas de GD

  
Implementar uma estrutura de governança de dados envolve várias etapas estratégicas e práticas para garantir uma gestão eficaz dos dados na organização.

O primeiro passo é definir uma visão clara para a governança de dados, alinhada aos objetivos estratégicos da organização. Essa visão deve direcionar objetivos específicos, como melhorar a qualidade dos dados, garantir conformidade e otimizar o uso dos dados.

Em seguida, é importante formar um Conselho de Governança de Dados, composto por membros representando diversas áreas da organização, como executivos, gerentes e especialistas. Esse conselho será responsável por estabelecer papéis e responsabilidades claras relacionadas à governança.

O desenvolvimento de políticas e diretrizes é fundamental, contemplando aspectos como qualidade, segurança e privacidade dos dados, além de definir normas para coleta, armazenamento, uso e compartilhamento.

A modelagem de dados e metadados é outro componente essencial. Devem ser implementados modelos conceituais, lógicos e físicos para dados estruturados e não estruturados, contemplando bancos relacionais, sistemas de arquivos distribuídos e suas inter-relações. O gerenciamento dos metadados, que funcionam como um dicionário explicativo dos dados, deve ser realizado por meio de sistemas específicos.

Procedimentos para garantir a qualidade dos dados devem ser desenvolvidos, com processos para monitoramento, medição e auditorias regulares para identificar e corrigir problemas.

É necessário definir e implementar controles de acesso e segurança, estabelecendo quem pode acessar os dados e sob quais condições. Ferramentas e técnicas devem ser adotadas para proteger os dados contra acessos não autorizados e vazamentos.

A educação e o treinamento dos funcionários são vitais para criar uma cultura organizacional voltada para a governança. Campanhas de conscientização reforçam a importância das políticas e práticas estabelecidas.

O monitoramento e a avaliação contínua das práticas e políticas garantem sua eficácia. Processos regulares de revisão devem ser implementados para ajustar e melhorar a governança.

Quanto à tecnologia, a seleção e implementação de ferramentas adequadas suportam a gestão dos dados, qualidade e metadados. Como ferramentas completas podem ser caras, é comum iniciar com processos e ferramentas manuais que adequem-se ao orçamento disponível.

Por fim, a documentação detalhada dos procedimentos e uma comunicação constante sobre atualizações e mudanças são essenciais para o sucesso da governança de dados.

# Aula 03 - Monitoramento e Auditoria

O monitoramento é um processo fundamental dentro da governança de dados. Para implementá-lo, é necessário definir métricas e indicadores que permitam avaliar a eficácia das políticas adotadas.

As métricas são valores numéricos que refletem aspectos como qualidade dos dados, conformidade e desempenho dos sistemas. A partir dessas métricas, estabelecem-se os KPIs (Key Performance Indicators), que ajudam a medir o progresso rumo aos objetivos da governança.

Relatórios periódicos de monitoramento devem apresentar o estado dos dados, o nível de conformidade com as políticas e eventuais problemas identificados. Painéis de visualização em tempo real (dashboards) são úteis para acompanhar métricas e KPIs.

As revisões de conformidade são avaliações regulares para garantir que as práticas de governança estejam sendo seguidas e que os processos estejam performando adequadamente.


É essencial utilizar ferramentas específicas para monitorar a qualidade dos dados, identificando problemas como duplicidade, inconsistência e erros. Além disso, sistemas de gerenciamento de metadados são importantes para rastrear e manter informações precisas e atualizadas sobre os dados.

Para garantir a qualidade dos dados, auditorias planejadas e regulares devem ser realizadas. Essas auditorias avaliam os dados conforme critérios específicos e geram relatórios detalhados com achados, conformidade ou não conformidade, e recomendações para melhorias. Com base nas auditorias, ações corretivas são implementadas, documentadas e comunicadas aos stakeholders, garantindo a melhoria contínua da governança de dados.

Outro aspecto essencial é o plano de resposta a incidentes, que define procedimentos para lidar com violações de segurança, falhas de qualidade, vazamento de dados, entre outros. A investigação das causas raiz desses incidentes é necessária para implementar correções e prevenir sua recorrência, configurando uma gestão eficaz de riscos.
  
# Aula 04 - Qualidade dos Dados

A qualidade dos dados é um componente crítico para a gestão e governança eficazes, pois impacta diretamente a precisão, confiabilidade e utilidade das informações. Investir em dados de baixa qualidade representa desperdício de recursos e perda de confiança por parte dos consumidores desses dados.

Para avaliar a qualidade dos dados, consideram-se aspectos fundamentais:

### **Precisão**: 
Os dados devem refletir fielmente a realidade que representam. Por exemplo, informações cadastrais de clientes precisam corresponder a fontes confiáveis, evitando dados fictícios ou incorretos.

### **Consistência**: 
Os dados devem ser uniformes e não apresentar conflitos entre diferentes sistemas e fontes. Um endereço, por exemplo, deve ser o mesmo em todas as bases de dados.

### **Completude**: 
Todos os dados necessários devem estar presentes, sem lacunas significativas. Formulários e cadastros devem ser preenchidos integralmente, sem campos obrigatórios em branco.

### **Atualidade**: 
Os dados devem estar atualizados, refletindo o estado mais recente, como contratos e seus aditivos.

### **Acuracidade**: 
Os dados precisam ser exatos, livres de erros que possam distorcer informações importantes, como valores financeiros incorretos que podem causar prejuízos significativos.

### **Relevância**: 
Os dados devem ser pertinentes e úteis para os propósitos a que se destinam.

### **Confiabilidade**: 
É fundamental que os dados sejam obtidos de fontes verificadas e confiáveis para garantir a integridade das análises.

No gerenciamento da qualidade, políticas claras precisam ser definidas, junto a processos e ferramentas que monitoram e avaliam continuamente os dados. O *data profiling* — análise das características dos dados — é essencial para identificar problemas e manter a qualidade.

Medir e monitorar regularmente a qualidade dos dados, realizar auditorias e promover uma cultura organizacional focada na importância dos dados são práticas indispensáveis. O engajamento da alta gestão é decisivo para que as práticas de qualidade sejam adotadas e sustentadas em toda a organização.

# Aula 05 - Metadados e Dados Mestres

Metadados são os dados que descrevem outros dados, fornecendo informações sobre a origem, estrutura, conteúdo e contexto dos dados em uma organização. Eles são essenciais para organizar e gerenciar dados de forma eficiente.

![Master Data Management](https://raw.githubusercontent.com/vbs-matheus/PosGraduacao-EngDados/refs/heads/main/imgs/master_data_management.png)

Dentro do contexto de governança de dados, **dados mestres** (Master Data) desempenham um papel crucial. São dados fundamentais e comuns a toda a organização, usados e compartilhados por diversos sistemas. Exemplos de dados mestres incluem informações sobre clientes, produtos, fornecedores, funcionários e locais. Esses dados são essenciais para o funcionamento do negócio, pois representam entidades-chave para a operação da organização.

Perder dados mestres, como a base de clientes, pode ter um impacto devastador. Por isso, esses dados exigem uma atenção especial e uma estratégia de contingência robusta, que pode incluir backups frequentes — talvez até a cada hora, dependendo da criticidade dos dados.

**Master Data Management (MDM)** é o conjunto de práticas, processos e ferramentas para gerenciar e garantir a qualidade dos dados mestres. O MDM é um processo contínuo que envolve criação, manutenção, integração e governança dos dados mestres. Ele assegura que esses dados sejam precisos, confiáveis, consistentes e que possam ser compartilhados adequadamente entre sistemas, departamentos e aplicativos.

As principais características do MDM incluem:

- **Consistência**: Garante que os dados mestres sejam uniformes em toda a organização.
- **Precisão**: Certifica-se de que os dados mestres reflitam corretamente a realidade do negócio.
- **Integração**: Facilita a integração dos dados mestres em diferentes sistemas e plataformas.
- **Governança**: A governança de dados mestres é uma parte crítica da governança de dados em toda a organização, garantindo que esses dados sejam geridos de forma eficaz e estejam alinhados com as políticas organizacionais.

O ciclo de vida dos dados mestres deve ser cuidadosamente gerido. Embora todos os dados na organização tenham um ciclo de vida, os dados mestres exigem atenção especial, pois não podemos simplesmente expurgá-los sem a devida análise. O gerenciamento de dados mestres assegura que esses dados sejam sempre atualizados, e que a organização tenha uma visão única, confiável e precisa deles.

O MDM é particularmente importante em organizações com múltiplos sistemas e bancos de dados, como é comum na atualidade. Ele facilita a análise, a colaboração entre equipes e setores, e garante que a tomada de decisão seja baseada em dados precisos e consistentes.

# Aula 06 - Catalogação de Dados


A catalogação de dados é um processo fundamental para gerenciar e governar os ativos de dados de uma organização. Trata-se de uma abordagem sistemática para organizar e documentar informações sobre os dados, criando uma visão única e consistente para toda a empresa.

O catálogo de dados funciona como um repositório centralizado de metadados — informações que descrevem os dados. Esses metadados incluem a origem, estrutura, qualidade, definições e relacionamentos dos dados, além do papel que desempenham na governança. Essa organização permite que usuários e partes interessadas acessem, descubram, compreendam e utilizem facilmente os dados disponíveis.

Um dos maiores desafios é inventariar dados dispersos em diferentes formatos e locais, como arquivos de texto, planilhas e bancos de dados. Para isso, é necessário gerenciar os fluxos de dados e mapear a linhagem dos dados, que mostra a trajetória e as transformações do dado desde sua entrada até seu uso final.

Além disso, é fundamental identificar dados confidenciais, priorizando sua proteção para garantir conformidade com legislações aplicáveis. A catalogação deve abranger dados estruturados, semi-estruturados e não estruturados — como documentos livres, páginas web, mídias sociais, imagens, áudio e vídeo — estes últimos demandando atenção especial devido à sua complexidade.

Uma boa prática é atribuir nomes e descrições claras e detectáveis aos dados, criando uma ontologia que facilite o entendimento e a gestão. No caso de data lakes, que armazenam dados brutos em diferentes formatos, a catalogação e classificação dos dados se tornam ainda mais importantes para evitar que o ambiente se torne um “data swamp” — um pântano de dados desorganizados e inúteis.

![Catalogação de Dados](https://raw.githubusercontent.com/vbs-matheus/PosGraduacao-EngDados/refs/heads/main/imgs/catalogo_dados.png)


A qualidade dos dados deve ser monitorada continuamente, aproveitando técnicas como aprendizado de máquina para automatizar a catalogação diante do grande volume de dados tratado atualmente. Ferramentas de machine learning auxiliam na identificação dos tipos de dados e seus relacionamentos, facilitando o processo.

As principais funções do catálogo de dados incluem a descoberta dos dados, a facilitação da governança, o suporte à colaboração entre equipes e o rastreamento da linhagem dos dados. Esta última é especialmente importante para compreender a origem, as transformações e o uso dos dados ao longo do tempo.

Em resumo, o catálogo de dados é uma peça-chave na infraestrutura de gestão de dados moderna, permitindo que os usuários acessem e utilizem os dados de forma autônoma e consciente, fundamentada em descrições claras e processos estruturados.

# Aula 07 - Introdução a Frameworks de GD

![Framework de GD](https://raw.githubusercontent.com/vbs-matheus/PosGraduacao-EngDados/refs/heads/main/imgs/dg_framework.png)
