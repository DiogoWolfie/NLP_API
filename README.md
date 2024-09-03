# NLP_API

## Sobre o DataSet

Foi escolhido o dataset mangaverse, sendo possível obtê-lo no link: https://www.kaggle.com/datasets/shreyasur965/mangaverse

Suas especificações podem ser encontradas também no mesmo link. 

Ultimamente, o universo dos animes e mangás foi adotado por todos. Inúmeras plataformas de streamming já possuem vários títulos, existindo uma própria plataforma apenas para animes e mangás, a Crunchroll. 
Os animes e mangás movimentam muito a economia mundial, com eventos, vendas de produtos, sendo usados como referência até mesmo nas olimpíadas, com muitos atletas monstrando seus gostos com movimentos característicos dos animes.
Com isso, essa API foi criada para os fãns. Se a pessoa quiser achar uma nova paixão pelas próximas semanas, essa API vai ser bastante útil para achar um novo mangá, bastando pesquisar por temática. 

### Rodando o código
Rode o comando abaixo no terminal:
    unicorn main:app --host 0.0.0.0 --port 8888 

### Acessando a API
Acesse no seu navegador a url:
    http://localhost:8888/

### Fazendo consultas
Uma consulta pode ser feita de duas formas:
1)  Usar a tag /consulta, seguido de uma query. Se quiser pesquisar mais de uma palavra, separa-las por espaço.
    http://localhost:8888/consulta?query=school
    http://localhost:8888/consulta?query=school dance

2) Usar a mesma estrutura anterior acrescentando um limite de relevância.
    http://localhost:8888/consulta?query=school?limite_relevancia=0.3
    Caso o limite não seja específicado, ele é definido como sendo 0.0, e o resultado trará os 10 mais relevantes, nunca ultrapassando isso.

