<h1 align="center"> Python Pandas </h1>
<div dir="auto" align="center">
  <br>
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg"><img align="center" alt="Gustavo-VSCode" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg" style="max-width: 100%;"></a>
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"><img align="center" alt="Gustavo-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" style="max-width: 100%;"></a>
  <a target="_blank" rel="noopener noreferrer nofollow" href="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg"><img align="center" alt="Gustavo-Pandas" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" style="max-width: 100%;"></a>
</br>
</div>

## Topics
* [Project Description](#project-description) :us:
* [Descrição do Projeto](#descrição-do-projeto) :brazil:
  
## Project Description
<p align="justify">
The project provides a pipeline for processing data from CSV files. It consists of a series of steps to clean, filter, and format the data. The process involves checking for missing values, ensuring correct data types, filtering rows based on certain conditions, parsing JSON data in a specific column, extracting valuable information, and finally combining the processed data to the original DataFrame. This processed data is then saved to a new CSV file. The project is particularly helpful in preparing data for analysis or machine learning tasks, where clean, properly formatted data is crucial for quality results.
</p>

## Code Description
<p align="justify">
The provided script represents an ETL (Extract, Transform, Load) pipeline. It starts by reading data from a CSV file, using a predetermined schema to set data types for each column. The script then filters the DataFrame based on completion status and disease type, as well as event dates later than a given date. The data types of columns are then adjusted as per the pre-set schema. 
<br>
The script also handles JSON data present in the 'answers' column, converting it to a list of dictionaries. It ensures that all values are dictionary types before transforming them into a DataFrame. A series of procedures are executed on this data, extracting specific information based on certain conditions. After this, columns that are completely empty are removed. 
<br>
In the final steps, the 'answers' column is dropped from the original DataFrame, and the processed 'answers' data is joined to it. The resulting DataFrame is then saved as a CSV file. This ETL pipeline is encapsulated in a main function, ensuring a streamlined workflow from extraction to transformation and loading.
</p>

## Getting Started
<p align="justify">
To begin with, ensure that Python is installed in your environment. The script relies heavily on the Pandas library, so make sure to install it using pip: `pip install pandas`. Additionally, JSON handling requires the JSON library. Replace any placeholders in the scripts with your specific paths or credentials. In particular, check for placeholders like '//CREDENTIALS//PATH//file.json', 'USER:PASSWORD@localhost:PORT/DATABASE', etc., and replace them with your actual data.
</p>

## Executing Program
<p align="justify"> 
To execute the program, make sure that this script ('main.py') and the source CSV file ('source_data.csv') are located in the same directory. Navigate to the directory in your terminal, and run the script using the command `python main.py`. Ensure that you have passed the necessary arguments to the main function, which include the input file, output file, and the filter date.
</p>

## Author
<p align="justify"> Gustavo de Souza Pessanha da Costa. 
</p>

## License
<p align="justify"> This project is licensed under the MIT license. 
</p>

:small_orange_diamond: :small_orange_diamond: :small_orange_diamond:

## Descrição do Projeto

<p align="justify">
O projeto fornece um pipeline para processamento de dados de arquivos CSV. Consiste em uma série de etapas para limpar, filtrar e formatar os dados. O processo envolve a verificação de valores ausentes, garantindo tipos de dados corretos, filtrando linhas com base em determinadas condições, analisando dados JSON em uma coluna específica, extraindo informações valiosas e, finalmente, combinando os dados processados com o DataFrame original. Estes dados processados são então salvos em um novo arquivo CSV. O projeto é particularmente útil na preparação de dados para análise ou tarefas de aprendizado de máquina, onde dados limpos e corretamente formatados são cruciais para resultados de qualidade.
</p>

## Descrição do Código
<p align="justify">
O script fornecido representa um pipeline ETL (Extract, Transform, Load). Ele começa lendo dados de um arquivo CSV, usando um esquema predeterminado para definir os tipos de dados para cada coluna. O script então filtra o DataFrame baseado no status de conclusão e tipo de doença, bem como datas de eventos posteriores a uma data fornecida. Os tipos de dados das colunas são então ajustados conforme o esquema pré-definido.
<br>
O script também lida com dados JSON presentes na coluna 'answers', convertendo-os em uma lista de dicionários. Ele garante que todos os valores sejam tipos de dicionário antes de transformá-los em um DataFrame. Uma série de procedimentos são executados nesses dados, extraindo informações específicas com base em certas condições. Depois disso, colunas que estão completamente vazias são removidas.
<br>
Nas etapas finais, a coluna 'answers' é removida do DataFrame original, e os dados 'answers' processados são unidos a ele. O DataFrame resultante é então salvo como um arquivo CSV. Este pipeline ETL é encapsulado em uma função principal, garantindo um fluxo de trabalho simplificado da extração à transformação e carregamento.
</p>

## Iniciando
<p align="justify">
Para começar, certifique-se de que o Python está instalado em seu ambiente. O script depende bastante da biblioteca Pandas, então certifique-se de instalá-la usando o pip: `pip install pandas`. Além disso, o manuseio de JSON requer a biblioteca JSON. Substitua quaisquer espaços reservados nos scripts por seus caminhos ou credenciais específicos. Em particular, verifique espaços reservados como '//CREDENTIALS//PATH//file.json', 'USER:PASSWORD@localhost:PORT/DATABASE', etc., e substitua-os por seus dados reais.
</p>

## Executando o Programa
<p align="justify"> 
Para executar o programa, certifique-se de que este script ('main.py') e o arquivo CSV de origem ('source_data.csv') estão localizados no mesmo diretório. Navegue até o diretório no seu terminal e execute o script usando o comando `python main.py`. Certifique-se de que passou os argumentos necessários para a função principal, que incluem o arquivo de entrada, o arquivo de saída e a data de filtro.
</p>"

## Autor
<p align="justify"> Gustavo de Souza Pessanha da Costa.
</p>

## Licença
<p align="justify"> Este projeto é licenciado sob a licença MIT.
</p>




