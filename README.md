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
Uma consulta pode ser feita da seguinte forma.
Usar a tag /consulta, seguido de uma query. Se quiser pesquisar mais de uma palavra, separa-las por espaço.

    http://localhost:8888/consulta?query=school

    http://localhost:8888/consulta?query=school dance

Consultas interessates seriam:
 1) http://localhost:8888/consulta?query=fight, que me retorna 10 resultados, infrmando que tenho muitos mangás com essa temática.

 2) http://localhost:8888/consulta?query=chicken, que me retorna menos de 10 resultados, o que era esperado (mas ainda assim bem impressionante teer mangás com galinha dentro da descrição)

 3) http://localhost:8888/consulta?query=strawhat, que não me retorna nada, o que é bem impressionante e inesperado, tendo em vista que o mangá mais vendido nos últimos anos fala de um pirata conhecido como StrawHat Luffy, mostrando que o dataset não está tão completo quanto esperado.

Observação importante: Existe um limite de similaridade mínimo de 0.1 para indicação do mangá. Caso a similaridade for menor que isso, não será mostrado.
