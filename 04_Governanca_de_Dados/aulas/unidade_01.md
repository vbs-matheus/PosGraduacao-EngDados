# Introdução a Governança de Dados.
A Governança de Dados é a definição de padrões e processos para garantir que os dados sejam utilizados de forma ética, segura e eficiente, atendendo às necessidades da organização e as regulamentações, como a **LGPD** e a **GDPR**.  
É um conjunto de políticas, normas, padrões e práticas que orientam as gestão de dados em todo o seu processo de coleta, uso e eventual descarte. ([***gov.br, 2025***](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/governancadedados#:~:text=%C3%89%20o%20conjunto%20de%20pol%C3%ADticas,%C3%A0s%20necessidades%20institucionais%20e%20regulat%C3%B3rias.))

## **▹ Temáticas da Unidade**
- Definição de Governança de Dados
- Importância da Governança de Dados
- Objetivos e Benefícios da Governança de Dados
- Principais Componentes da Governança de Dados
- Desafios e Barreiras na Governança de Dados
- Modelos de Governança de Dados
- Desenvolvimento de Políticas de Dados
- Padrões e Normas
- Segurança e Privacidade de Dados
- Ferramentas de Administração de Dados


## **Objetivos**

O objetivo é contextualizar o aluno na compreensão e aplicação dos princípios fundamentais da Governança de Dados, reconhecendo sua importância no gerenciamento eficaz de dados dentro de organizações.  
  
Ao final, o aluno será capaz de identificar os componentes essenciais da Governança de Dados, enfrentar desafios comuns, desenvolver políticas de dados e adotar práticas que garantam a segurança, privacidade e qualidade dos dados, alinhando essas práticas às normas e padrões internacionais e às necessidades organizacionais.

---
---

# Aula 01 - Definição de Governança de Dados

Governança de Dados é um processo contínuo de melhoria por iniciativa ativa e demonstrável. Está ligada à esfera executiva de uma empresa.   
  
Gera uma intrutura inter-organizacional para o compartilhamento seguro e para análise de dados entre departamentos. Além de melhorar a qualidade dos dados e a eficiência entre as partes interessadas.

- **Missão**:
  - Definir e alinhar proativamente as regras dados de toda organização.
  - Fornecer proteção de serviços contínups e abrangentes para as partes interessadas em dados.
  - identificar e resolver problemas de dados.
- **Visão**:
  - As informações são tratadas como um ativo de toda a empresa e estão prontamente disponíveis para apoiar as tomadas de decisões baseadas em evidências e a ação informada.
  
A Governança de Dados **NÃO É** necessariamente uma tecnologia, ou seja, ele não é ETL/ELT, nem não faz parte do escopo de limpeza, banco, armazenamento ou gerenciamento dos dados.

# Aula 02 - Importância da Governança de Dados

Dados são ativos de alta importância que precisam ser gerenciados de forma estratégica e eficiente.  
Uma boa governança diminuiu perdas por ineficência, aumenta as decisões data-driven e mantêm as conformidades dos processos de acordo com os regulamentos vigentes.  
  
Em caso de fusão ou compra de uma empresa, uma boa governança auxilia ou até permite a fusão destes dados.  
  
As necessidades de negócios impulsionam as necessidades de informação e, por consequência, as necessidades técnicas. A governança de dados é principalmente uma função de negócio e estratégica, ou seja, ela apoia diretamente os objetivos estratégicos da empresa.

📌![Abrangência da Governança de Dados](https://raw.githubusercontent.com/vbs-matheus/PosGraduacao-EngDados/refs/heads/main/imgs/abrangencia_governanca_dados.png)

# Aula 03 - Objetivos e Benefícios da GD

Integridade, segurança, conformidade com a regulamentação;  
Acesso e controle;
Transparência e rastreabilidade;

# Aula 04 - Principais Componentes da GD

## **▹ Data Literacy**
  
O conceito do Data Literacy é de *Alfabetização em Dados*.  
Se refere à capacidade dos colaboradores de uma organização ler, compreender, analisar e utilizar dados de maneira eficaz.

📌![Data Literacy](https://raw.githubusercontent.com/vbs-matheus/PosGraduacao-EngDados/refs/heads/main/imgs/data_literacy.png)
  
Compõe-se, dentro da previsão da alfabetização em dados, o desenvolvimento ou fornecimento de treinamentos para os funcionários.  
Os funcionários bem alfabetizados em data contibuiem para boa governança, pois são capaz de identificar e corrigir problemas de eficiência, qualidade ou até regulatórios durante o dia a dia.  
  
Os Quatro Pilares da ***Alfabetização em Dados*** são:   
1. **Exploração dos Dados**: É o mapeamento dos dados na instituição. Onde eles estão guardados e como estão sendo disponibilizados.

2. **Gerenciamento dos dados**: Envolve identificar e coletar dados necessários para abordar questões prioritárias.
   
3. **Uso dos dados**: Os dados após coletados precisam ser analizados, interpretados para decisões.

4. **Reflexões e Melhoria**: A revisitação dos processos de forma constante para identificar pontos de possível melhoria na governança.

# Aula 05 - Desafios e Barreiras da GD

Quando tentamos implementar Governança de Dados em uma empresa, é possível encontrar diversas barreiras/resistências durante o processo.
  
- Resistência à Mudança: Funcionários, inclusive líderes e gestores, muito acostumados com processos antigos e não se vêem dispostos à adaptar-se aos processos novos.
- Falta de Recursos e orçamento: A implementação da Governança vai necessitar de tecnologias, funcionários qualificados e treinamento. Muitas vezes é algo incessível para a maioria das empresas.
- Dados não estruturados.
- Problemas na qualidade dos dados.
- Conformidade regulatória.
- Definição de papéis e responsabilidades.
- Cultura organizacional
- Escalabilidade e Manutenção
- Privacidade e Segurando 

# Aula 06 - Modelo de Governança de Dados.

- **Modelo Centralizado**: a governança de dados é controlada por uma equipe centralizada.  
  Essa equipe que vai ser responsável pela decisão e políticas relacionadas aos dados. Tem como vantagem uma consistência e padronização maior. A desvantagem é ser menos ágil, ser mais lento nas respostas. 

- **Modelo Descentralizado**: é o inverso do centralizado. A responsabilidade pela governança de dados é distribuída entre diferentes unidades de negócio ou departamentos.  
    Cada unidade gerencia seu próprio dado, a partir de diretrizes gerais federadas.  
    **Vantagens** - permite que a área de negócio se adapte às práticas de governança e se adapte às necessidades específicas; aumenta a agilidade.  
    **Desvantagem** - maior inconsistência por falta de padrão centralizado.  

- **Modelo Híbrido**: Combinação entre o modelo centralizado com o modelo descentralizado. Mais complexo de definir.  
  Uma equipe central que define políticas e diretrizes gerais, enquanto as unidades de negócios têm uma certa autonomia na implementação local dessas diretrizes. Busca-se a vantagem do equilíbrio e a desvantagem de ser mais desafiador.

- **Modelo Federado**: Envolve a criação de uma rede de governança de dados com várias partes, departamentos, unidades de negócio, todo mundo trabalhando em conjunto e observando regras práticas comuns.  
  Tem a flexibilidade, a colaboração entre diferentes partes da organização,mas pode haver uma dificuldade na coordenação, por ser uma rede de governança de dados divida em várias partes.

# Aula 07 - Desenvolvimento de Política de Dados.

O desenvolvimento de políticas de dados é essencial para a governança eficaz. Essas políticas definem regras para a coleta, armazenamento, uso, compartilhamento e proteção dos dados na organização.

É preciso alinhar essas políticas aos objetivos do negócio, considerando requisitos regulatórios e de compliance. O escopo deve abranger qualidade, segurança, privacidade, acesso e uso dos dados, especificando os departamentos e tipos de dados envolvidos.

As diretrizes devem garantir que os dados sejam precisos, completos e atualizados, definindo práticas de limpeza, validação e proteção contra acessos não autorizados, perda ou vazamento. Além de assegurar conformidade com leis como GDPR e LGPD.

Deve haver participação das partes interessadas — TI, jurídico, compliance e negócios para construir políticas robustas, que devem ser revisadas regularmente com base em feedbacks.

A implementação exige treinamento adequado e comunicação clara sobre responsabilidades e procedimentos, usando canais eficientes como reuniões, e-mails e intranet. Isso ajuda a monitorar o cumprimento das políticas por meio de auditorias e ferramentas, além de estabelecer mecanismos para tratar violações.

Métricas, como dados incompletos, ajudam a monitorar a aderência e identificar problemas que impactam a qualidade dos dados.

Por fim, as políticas devem ser atualizadas constantemente para refletir mudanças regulatórias, tecnológicas e estratégicas.

### Exemplos práticos
- Políticas de qualidade para garantir precisão e integridade.
- Políticas de segurança para proteção contra ameaças internas e externas.
- Políticas de privacidade alinhadas a legislações vigentes.
- Políticas de retenção definindo armazenamento e descarte de dados.

---
---

# Aula 08 - Padrões e Normas

Nesta aula, discutimos os principais padrões e normas relevantes para governança de dados. Entre eles, destacam-se:

O **ISO/IEC 27001**, que estabelece requisitos para sistemas de gestão de segurança da informação, focando na implementação, manutenção e melhoria contínua da segurança dos dados, alinhada a padrões internacionais.

O **ISO/IEC 38500** trata da governança de TI, fornecendo princípios e diretrizes para uma boa gestão e conformidade das políticas de TI.

O **ISO/IEC 27018** orienta sobre a proteção de dados pessoais em nuvens públicas, especialmente importante para organizações que utilizam serviços públicos de nuvem.

No âmbito regulatório, temos o **GDPR** (General Data Protection Regulation), regulamento europeu que define regras rigorosas para coleta, armazenamento e tratamento de dados pessoais, exigindo conformidade das organizações que atuam na União Europeia.

No Brasil, a **LGPD** é equivalente ao GDPR, regulando a proteção de dados pessoais para empresas que operam no país.

A **CCPA** (California Consumer Privacy Act) é uma legislação da Califórnia que protege a privacidade dos consumidores locais, sendo relevante para operações nessa região.

O **DAMA-DMBOK** (Data Management Body of Knowledge) é um framework abrangente que cobre as melhores práticas e padrões para gestão de dados, servindo como um guia essencial para governança.

A certificação **CDMP** (Certified Data Management Professional) oferece um padrão de competência para profissionais de dados, ganhando importância no mercado.

Também citamos o **ISO 11179**, norma que orienta a gestão eficaz de metadados e definição de dados.

O **NIST Cyber Security Framework** é um framework focado na gestão de riscos cibernéticos, oferecendo diretrizes para proteção contra ameaças.

Por fim, para instituições financeiras e operações como Open Banking, o padrão **PCI DSS** (Payment Card Industry Data Security Standard) é fundamental para garantir a segurança dos dados de pagamentos, sendo obrigatório para instituições que participam dessas iniciativas.

Falamos ainda sobre o conceito de Open Banking, que permite o compartilhamento controlado de dados bancários entre instituições por meio de APIs, fomentando a concorrência e melhores ofertas, mas também trazendo desafios de privacidade e compliance.

Por fim, destacamos que padrões e normas são diretrizes gerais que devem ser adaptadas às necessidades e contexto da organização, com treinamento, conscientização e auditorias regulares para garantir a conformidade e efetividade dessas políticas.

# Aula 09 - Segurança e Privacidade de Dados

Nesta aula, discutimos práticas essenciais para garantir a segurança e a privacidade dos dados. Entre as medidas de segurança destacam-se a criptografia, controle rigoroso de acessos, uso de firewalls e sistemas de detecção de intrusão, além de backups regulares para recuperação de dados. A segurança física também é importante, protegendo servidores e dispositivos contra acessos não autorizados por meio de controles como catracas e áreas seguras.

O treinamento e a conscientização dos funcionários são pilares fundamentais para a proteção dos dados, garantindo que todos compreendam suas responsabilidades e os procedimentos adequados.

No âmbito da privacidade, conceitos essenciais envolvem a necessidade de consentimento explícito dos indivíduos para a coleta e uso de seus dados pessoais, além da transparência sobre como esses dados são utilizados e por quem. Os titulares dos dados possuem direitos de acesso, correção e exclusão de suas informações pessoais.

Falamos também sobre as principais legislações que regulam a proteção de dados: o GDPR, regulamento da União Europeia; a LGPD, lei brasileira similar ao GDPR; a CCPA, lei da Califórnia que protege a privacidade dos consumidores locais; e o HIPAA, que regula dados de saúde nos Estados Unidos.

Um exemplo prático ilustra a importância dessas leis: em um filme, pessoas foram protegidas contra o uso indevido de seus dados de saúde, o que levou à interrupção de uma ação abusiva. Isso reforça como a LGPD espelha as normas internacionais de privacidade e está na vanguarda do direito sobre dados pessoais.

A LGPD, instituída pela Lei nº 13.709/2018, regulamenta o tratamento de dados pessoais como nome, gênero, preferências, localização e identificadores digitais. Ela se aplica a qualquer empresa ou pessoa que trate esses dados em território brasileiro, abrangendo detentores e operadores, como fornecedores e parceiros.

As penalidades por descumprimento podem chegar a 2% do faturamento anual, limitadas a R$ 50 milhões por infração. Um caso emblemático foi a multa bilionária aplicada ao Facebook pela GDPR por transferir ilegalmente dados de cidadãos europeus para processamento nos EUA.

O controle sobre os dados pessoais é uma conquista importante, pois dados como CPF, RG, telefone e endereço pertencem ao indivíduo, e seu uso indiscriminado pode causar danos.

A LGPD e a GDPR possuem princípios semelhantes, incluindo finalidade, necessidade, transparência, segurança, prevenção e responsabilização. Dados sensíveis, como origem racial, convicções religiosas, saúde e dados de crianças e adolescentes, exigem cuidados especiais.

No âmbito da LGPD, multas podem ser atenuadas conforme o comprometimento da empresa com segurança da informação e treinamento, conforme o artigo 50 da lei.

Por fim, explicamos os conceitos de anonimização — onde os dados são embaralhados para impedir identificação — e pseudoanonimização, que permite reverter o dado ao estado original por meio de uma chave, facilitando o uso seguro de dados pessoais.

# Aula 10 - Ferramentas de Administração de Dados