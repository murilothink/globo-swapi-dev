# Star Wars Data Pipeline

Este projeto consiste em um conjunto de pipelines para coletar e processar dados da API do Star Wars. As pipelines estão divididas em três etapas: bronze, silver e gold.

## Instalação

Para utilizar este projeto, siga as instruções abaixo:

1. Clone este repositório para sua máquina local:

```
git clone https://github.com/seuusuario/star-wars-data-pipeline.git
```

2. Instale as dependências necessárias:

```
pip install -r requirements.txt
```

## Uso

Este projeto possui três pipelines principais, cada uma responsável por uma etapa do processo de processamento de dados:

1. **STARWARS_BRONZE**: Coleta dados brutos da API do Star Wars.
2. **STARWARS_SILVER_AND_DATABASE**: Processa e transforma os dados coletados para um formato adequado para análise.
3. **STARWARS_GOLD_AND_DATABASE**: Realiza análises avançadas nos dados processados e os prepara para consumo final.

Para executar uma determinada pipeline, utilize o seguinte comando:

```
python main.py NOME_DA_PIPELINE
```

Substitua `NOME_DA_PIPELINE` por uma das seguintes opções: `STARWARS_BRONZE`, `STARWARS_SILVER_AND_DATABASE` ou `STARWARS_GOLD_AND_DATABASE`.

Exemplo:

```
python main.py STARWARS_BRONZE
```

Este comando iniciará o processo de coleta de dados brutos da API do Star Wars.
a

## Estrutura das Etapas

O processamento dos dados é realizado em três etapas principais:

### Bronze

Na etapa bronze, os dados brutos são coletados da API do Star Wars. Esta etapa é responsável por capturar todas as informações disponíveis na API.

### Silver

Na etapa silver, os dados coletados são processados e transformados em um formato adequado para análise. Aqui, são realizadas transformações e preparações dos dados para a etapa final.

### Gold

Na etapa gold, são realizadas análises avançadas nos dados processados e preparados na etapa prata. Isso inclui a geração de insights, visualizações e preparação dos dados para consumo final.

## Uso do Banco de Dados

Este projeto utiliza o banco de dados SQLite para armazenar os dados processados em cada etapa. Os arquivos de banco de dados para as etapas silver e gold são gerados nos seguintes diretórios:

- `silver_files_db`: Contém o banco de dados da etapa prata.
- `gold_files_db`: Contém o banco de dados da etapa ouro.

### Download Dbvier 

Para realizar a conexão do SQLite, faça o download do Dbvier ou qualquer ferramenta de gerenciamento de banco de dados.

Link: [Download Dbvier](https://dbeaver.io/download/)

### Conexão Dbivier

1. Abra o Dbvier.
2. Clique em "Nova Conexão".
3. Escolha o banco de dados SQLite e clique em "Avançar".
4. Clique em "Abrir".
5. Vá até o projeto `globo-swapi-dev` e escolha o arquivo que deseja ver nas pastas abaixo:
   - `silver_files_db`: Contém o banco de dados da etapa prata.
   - `gold_files_db`: Contém o banco de dados da etapa ouro.

## Perguntas Frequentes


#### Por que utilizamos o SQLite e não Docker Container?

O SQLite foi utlizado nesse projeto devido às suas características de fácil configuração, baixa sobrecarga de administração, portabilidade e eficiência.

### Por que usamos o Pandas em vez do Spark?

Optei pelo Pandas neste projeto por sua configuração mais simples e pelo fato de lidarmos com conjuntos de dados menores. Como estamos trabalhando principalmente em um ambiente de desenvolvimento individual e não em um cluster, o Pandas oferece a eficiência e a portabilidade necessárias. Embora reconheça que o Spark seria mais apropriado em ambientes distribuídos com grandes conjuntos de dados, para este projeto, o Pandas atende às nossas necessidades atuais de forma satisfatória.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir um *issue* ou enviar um *pull request*.

