# Nomes Significativos
Um código é algo que será compartilhado com diversos indivíduos de um mesmo grupo. Apesar de existir todo um modo pessoal de 'codar',
o desenvolvedor deve pensar sempre no todo, em como outro entenderia seu código, tal qual uma redação é redigida varias vezes, não é diferente 
com um código.
## Nomes que revelem seu propósito
Escolher bons nomes pode auxilia o leitor a entender o contexto do problema, é um processo que leva mais tempo que escolher uma variável aleatória, porém
este é economizado em tempo de manutenção e/ou customização do mesmo.
## Faça Distinções Significativas
Faça distinções das variáveis para que fique claro o propósito específico de cada uma, deve se evitar a repetição, pois ela pode levar ao erro.
## Use Nomes Pronunciáveis
É mais fácil lidar com nomes faláveis do que com acrônimos criados, os acrônimos podem fazer sentido para o criado durante o momento da criação, porém
é muito mais intuitivo usar nomes pronunciáveis, tanto para procura quanto para rápido entendimento do que está sendo feito.
## Use Nomes Passíveis de Busca
Essa é importante, ao refatorar/customizar um código essa é uma dica valiosíssima. Procurar e fazer `replace` por letras independentes num código pode gerar a maior confusão.
Usar nomes passíveis de busca acelera alterações e a facilidade de encontrar trechos específicos que precisam ser trabalhados.
Imagine ter que procurar por uma letra específica, `o`,  `a`, `i`, não é uma boa jogada. Esse tempo economizado na escolha da variável certamente terá grandes chances de virar débito
técnico no futuro.
## Evite Codificações
No caso, combinações específicas de palavras que explicam um significado exclusivo. Opte sempre por uma variável maior com mais detalhamento.
## Evite Mapeamento Mental
Usar variáveis com letras específicas denominando variáveis por conta do contexto do código ser `lógico` não é uma boa ideia, novamente caímos na mesma.
A pessoa, poderá até entender o que foi dito com algum esforço mental, mas não seria melhor se fosse um texto preciso ? A exemplo, todos, com alguma instrução sobre, são
capazes de entender um código morse, mas não é muito mais fácil falar em texto plano ? 
## Use Nomes a partir do Domínio da Solução ou Problema
Os nomes devem remeter ao contexto da solução, é esperado que a próxima pessoa que atue no código tenha noção das regras da implementação.
Nomes inerentes a essas regras devem ser usados, assim facilita muito para os novos leitores.