# GERADOR DE CÓDIGO EAN

O cálculo para criar um código de barras depende do tipo de código que você deseja gerar. No Brasil, o tipo mais comum é o EAN-13, que possui 13 dígitos:

### 1. Obtenção dos dígitos:

#### Os primeiros 12 dígitos:
<p><strong>3 dígitos:</strong> identificam o país de origem (no Brasil, 789 ou 790).</p>
<p><strong>5 dígitos:</strong> identificam o fabricante do produto.</p>
<p><strong>4 dígitos:</strong> representam o produto em si.</p>
<p><strong>Dígito verificador:</strong> serve para garantir a validade do código.</p>

### 2. Cálculo do dígito verificador:

<p><strong>Etapa 1:</strong> Multiplique cada dígito ímpar por 3.</p>
<p><strong>Etapa 2:</strong> Some os resultados da etapa 1.</p>
<p><strong>Etapa 3:</strong> Multiplique cada dígito par por 1.</p>
<p><strong>Etapa 4:</strong> Some os resultados da etapa 3.</p>
<p><strong>Etapa 5:</strong> Some os resultados das etapas 2 e 4.</p>
<p><strong>Etapa 6:</strong> Divida o resultado da etapa 5 por 10.</p>
<p><strong>Etapa 7:</strong> Se o resto da divisão da etapa 6 for 0, o dígito verificador é 0. Caso contrário, subtraia o resto da etapa 6 de 10 para obter o dígito verificador.</p>

### 3. Gerando o código de barras:

#### Representação dos dígitos: 
<p>Cada dígito é representado por uma sequência de barras e espaços com diferentes larguras.</p>
<p>Sequência inicial: Começa com duas barras pretas, uma barra branca no meio, e termina com uma barra preta.</p>
<p>Sequência central: Intercala as representações dos 12 dígitos, dividindo-os em dois grupos de 6.</p>
<p>Dígito verificador: Representado após a sequência central.</p>
<p>Sequência final: Igual à sequência inicial.</p>