# BigData-MapReduce
Projeto desenvolvido durante a disciplina de BigData do curso de Arquitetura de Software Distribuído


Cada arquivo neste diretório possui a seguinte estrutura:
journals/cl/SantoNR90:::Michele Di Santo::Libero Nigro::Wilma 
Russo:::Programmer- Defined Control Abstractions in Modula-2.

Cada uma das linhas pode ser entendida como:
  I. Informação bibliográfica;
  II. autores separados por '::';
  III. Título da obra
  paper-id:::author1::author2::.... ::authorN:::title
  
A tarefa é fazer o cálculo de quantas vezes cada termo (no título da obra) acontece por autor; Por exemplo para o autor 'Alberto Pettorossi' os seguinte termos acontecem (considerando todos os documentos): program:3, transformation:2, transforming:2, using:2, programs:2, and logic:2.

Observe os seguintes itens:
1. O separador de campos é “:::” e separador de autores é “::”;
2. Cada autor pode ter escrito múltiplas obras, que por sua vez podem estar em vários arquivos;
3. Existe um lista de palavras que não serão consideradas. Utilize o arquivo
stopword.py do exercício prático: exclua todas estas palavras para os autores;
4. Se possível faça a exclusão de pontuações também, de forma que a palavra logic e logic. sejam tratadas como se fossem uma única palavra;
5. Entregue a implementação do seu grupo;
6. Responda quais são as duas palavras que mais acontecem para os seguintes autores:
  a- “Grzegorz Rozenberg”
  b- “Philip S. Yu”
