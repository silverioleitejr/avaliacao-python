EXERCÍCIO
=========
Supondo que o cliente X enviou uma base de dados (dataset.csv) e necessitaremos de uma API com 
os seguintes requisitos:
I.	1 rota que retornará o valor médio de todos os carros baseados no fabricante (coluna car_make agrupada pela média dos valores da coluna car_value);
II.	1 rota que retornará o valor médio de um fabricante de carro passado como parâmetro no request (Após o cálculo de I, pode-se filtrar apenas o valor requerido);
III.	1 rota que que retornará o valor médio de todos os carros baseados nas cidades correspondentes (coluna city agrupada pela média dos valores da coluna car_value);
IV.	1 rota que retornará o valor médio dos carros de uma cidade passada como parâmetro no request (Após o cálculo de III, pode-se filtrar apenas o valor requerido);

Notas:
======
- A API deve conter um basic auth;
- Os tópicos I e II devem ser desenvolvidos utilizando Pandas;
- Os tópicos III e IV devem ser desenvolvidos utilizando Spark;
- Deve ter um README.md que de um overview do projeto, juntamente com os comandos para rodar no servidor e 
  os comandos para subir a aplicação em docker;
- Criar uma documentação simples da API utilizando um gerador de sua escolha, lembrando que uma rota
  deve renderizar o html da documentação;
